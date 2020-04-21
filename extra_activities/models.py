from django.db import models

# Create your models here.
from employee.models import Employee


class Extra(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name='Employee ID',on_delete=models.PROTECT)
    title = models.CharField("Name",max_length=100)
    department = models.CharField("Department",max_length=100)
    level = models.CharField("Level",max_length=100)
    details = models.CharField("Details",max_length=100)
    year = models.CharField("Year",max_length=4)
    month = models.CharField("Month",max_length=10)
    role = models.CharField("Role", max_length=100,blank=True, null=True)


    class Meta:
        db_table = 'extras'
