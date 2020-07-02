from background_task import background
from process_zipcode import process_all_zips
from backend.models import DoctorData, ZipCode, OldData
from django.core.mail import send_mail
import pandas as pd

@background()
def do_work():
    print("Do work Started!")
    zip_code = [i.zip_code for i in ZipCode.objects.all()]
    df = pd.DataFrame(list(OldData.objects.all().values()))
    final_df = process_all_zips(zip_code, df)
    data_set = final_df.to_dict('records')
    for data in data_set:
        d1 = DoctorData(practice_name=data['PracticeName'], first_name=data['FirstName'],
                        last_name=data['LastName'],
                        address=data['Address'], city=data['City'], state=data['State'], zip=data['Zip'],
                        phone=data['Phone'], speciality=data['Specialty'], lat=data['Latitude'],
                        long=data['Longitude'], distance=data['Distance'], doctors=data['Specialists'])
        d1.save()
    print("Do Work Ends!")
    subject = "Your File is ready for download -> Doctors APP"
    message = "Login through Admin Portal to download the data with your credentials. " \
              "Kindly delete existing data after download"
    recipient_list = ['akashkumarqoou1997@gmail.com']
    from_email = "akashkumarqoou1997@gmail.com"
    try:
        send_mail(subject=subject, message=message, recipient_list=recipient_list, from_email=from_email,
                  fail_silently=False)
    except Exception as e:
        print(e.args)
    print("Mail Sent!")
