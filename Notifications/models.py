import datetime
from django.db import models


# Create your models here.
class Category(models.Model):
    cid = models.IntegerField('Category_ID', primary_key=True)
    name = models.CharField('Category Name', max_length=50)

    def __str__(self):
        return self.name


class Notice(models.Model):
    nid = models.IntegerField('Notice_ID', primary_key=True)
    title = models.CharField('Title', max_length=140)
    branch = models.CharField('Branch', max_length=30, null=True, blank=True)
    course = models.CharField('Course', max_length=50, null=True, blank=True)
    sem = models.IntegerField('Semester', null=True, blank=True)
    year = models.IntegerField('Year', null=True, blank=True)
    date = models.DateTimeField('Date', default=datetime.datetime.today)
    time = models.TimeField('Time', default=datetime.datetime.now)
    cid = models.ForeignKey(Category, on_delete=models.CASCADE)
    notice_image = models.ImageField('Notice Image', upload_to='static/Notifications/Notice_images/')

    def __str__(self):
        return self.title
