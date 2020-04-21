from django.db import models

# Create your models here.
from employee.models import Employee


class Awards(models.Model):
    employee = models.ForeignKey(to=Employee, related_name='employee_awards', verbose_name='Employee ID', on_delete=models.PROTECT)
    title = models.CharField("Title",max_length=100)
    awardType = models.CharField("awardType",max_length=100)
    organisation = models.CharField("Organization",max_length=100)
    month = models.CharField("Month",max_length=100)
    year = models.CharField("Year",max_length=4)

    class Meta:
        db_table = 'awards'
