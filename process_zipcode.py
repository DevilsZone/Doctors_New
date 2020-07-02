import requests
import pgeocode
from fake_user_agent import give_fake_headers
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def download_data(zip_code, radius=5):
    nomi = pgeocode.Nominatim('us')
    api_key = "ade07974-778f-8441-a98a-2888b073fa32"
    zip_code = str(zip_code)
    xy = nomi.query_postal_code(zip_code)
    lat = str(xy['latitude'])
    lon = str(xy['longitude'])
    print("Latitude = {}, Longitude = {}".format(lat, lon))
    url = "https://galdermahcprestservice.intouchsol.net/api/PhysicianLocator/Search?apikey={}&latitude={" \
          "}&longitude={}&skip=0&take=100&CarriesDysport=true&radius={" \
          "}&specialty=&doctorName=&sortBy=default&password=&input-cityStateOrZip={}".format(api_key, lat, lon, radius,
                                                                                             zip_code)
    session = requests.session()
    r = session.get(url, headers=give_fake_headers())
    x = r.json()
    n_results = x['TotalCount']
    if n_results > 0:
        return x['Results']
    else:
        return None

def process_all_zips(zip_codes, df_1):
    list_df = []
    try:
        for i in zip_codes:
            temp = download_data(i)
            try:
                if temp:
                    list_df += temp
                else:
                    pass
            except Exception as j:
                print("Exception Occurred Here!")
                print(j)
    except Exception as e:
        print("Exception Occurred There!")
        print(e)
    try:
        df = pd.DataFrame.from_records(list_df)
        df['Zip'] = df['Zip'].apply(lambda x: x.split("-")[0])
        df.drop_duplicates(subset='Id', keep="first", inplace=True)
        df['X'] = df['PracticeName'] + ", " + df['Address'] + ", " + df['City']
        choices = df['X'].tolist()
        df_1['X'] = df_1['company_name'] + ", " + df_1['shipping_address_1'] + ", " + df_1['shipping_city']
        results = []
        indexes = []
        for j in range(len(df_1)):
            matcher = df_1['X'].iloc[j]
            if not pd.isnull(matcher):
                y = process.extract(matcher, choices, scorer=fuzz.token_set_ratio)
                best_matches = [yy for yy in y if yy[1] > 80]
                if len(best_matches) > 0:
                    best_match = best_matches[0][0]
                    indexes.append(j)
                    results.append(best_match)
        unique_data_from_scrapped_data = df[-df['X'].isin(list(set(results)))]
        unique_data_from_scrapped_data.drop(columns=['X'], axis=1, inplace=True)
        return unique_data_from_scrapped_data.drop(columns=['PracticeURL'], axis=1, inplace=True)
    except Exception as e:
        print(e)
        print("Exception Occurred Nowhere!")
