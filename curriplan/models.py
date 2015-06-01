from django.db import models
from django.db import models

class people(models.Model):
    firstName=models.CharField(max_length=30)
    lastName= models.CharField(max_length=30)
    gender=models.CharField(max_length=1)
    phone= models.PositiveIntegerField()
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    state=models.CharField(max_length=15)
    zip=models.PositiveIntegerField()
    email=models.CharField(max_length=50)

class course(models.Model):
    courseName=models.CharField(max_length=15)
    courseDesc=models.CharField(max_length=150)
    courseFee=models.PositiveIntegerField()
    courseStartdate=models.DateField()
    courseEnddate=models.DateField()

class lesson(models.Model):
    lessonName=models.CharField(max_length=15)
    lessonDesc=models.CharField(max_length=150)

class comment(models.Model):
    commenttext=models.CharField(max_length=1000)
    commentapproved=models.BooleanField()
    commentFlagged=models.BooleanField()
    commentparentID=models.PositiveIntegerField()

class roles(models.Model):
    roleName=models.CharField(max_length=10)
    roleDescription=models.CharField(max_length=150)

class peopleRoles(models.Model):
    peopleRolesPeopleID=models.ForeignKey(people)
    peopleRolesRolesID=models.ForeignKey(roles)
    peopleRolesApproval=models.BooleanField()


# Create your models here.
