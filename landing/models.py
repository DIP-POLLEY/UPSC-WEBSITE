from django.db import models

# Create your models here.
class Practice1(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)

class Practice2(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)






class GS1_static(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)

class GS1_Current(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)







class GS2_static(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)

class GS2_Current(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)






class GS3_static(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)

class GS3_Current(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)






class GS4_static(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)

class GS4_Current(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)







class Essay(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)







class Sociology_static(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)

class Sociology_current(models.Model):
    topic_name = models.CharField(max_length=1000)
    File = models.FileField(upload_to='media')
    check_if_image = models.BooleanField(default=False)
    check_if_pdf = models.BooleanField(default=False)
