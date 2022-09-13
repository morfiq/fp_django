from django.db import models
from django.urls import reverse
from django.db.models import JSONField

# Create your models here.
class fpuserdata(models.Model):
    userid = models.IntegerField()
    id1 = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=400)
    # class Meta:
    #     db_table = "FinPeer_app_fpuserdata"

class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100, unique=True)
    phoneNum = models.CharField(blank=True, null=True, max_length = 20)
    password = models.CharField(max_length=30)
    # profilePic = models.ImageField(upload_to='profile_pics',
    #                                default="default.jpeg")

    def get_absolute_url(self):
        return reverse('userdetail', kwargs={'pk': self.pk})