from django.db import models
from doctors_add import do_work

# Create your models here.
class Process_Task(models.Model):
    enable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(Process_Task, self).save(*args, **kwargs)
        do_work()
