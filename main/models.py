from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):

    title = models.CharField("Название", max_length=200)

    date = models.DateTimeField('дата создания')


    def __str__(self):
        return self.title

class Aim(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField('Описание')
    date = models.CharField("Дата", max_length=200)
    taskAim = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    taskCur =  models.CharField("1-в процессе,2-просрочено, 3-сделано", max_length=200,null=True)
    def __str__(self):
        return self.title



# class Aim(models.Model):
#     title = models.CharField("Название", max_length=200)
#     description = models.TextField('Описание')
#     date = models.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=models.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
