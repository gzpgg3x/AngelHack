from django.db import models
from django.contrib.auth.models import User
import hashlib

# class Ribbit(models.Model):
#     content = models.CharField(max_length=140)
#     user = models.ForeignKey(User)
#     creation_date = models.DateTimeField(auto_now=True, blank=True)





class bookPasser(models.Model):
    content = models.CharField(max_length=40,blank=True)
    location = models.CharField(max_length=100,blank=True)
    message = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=18,blank=True)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Shout(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)
    author = models.CharField(max_length=40,blank=True)
    message = models.TextField()
    zip = models.CharField(max_length=15,blank=True)
    address = models.CharField(max_length=100,blank=True)
    count = models.CharField(max_length=5,blank=True)
    book = models.CharField(max_length=60,blank=True)
    branchname = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=40,blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s: %s" % (self.author, self.message[:20])
        #return "%s: %s" % (self.author, self.message, self.a[:100])

class Branch(models.Model):
    branchname = models.CharField(max_length=80, blank=True)
    branchaddress = models.CharField(max_length=100,blank=True)
    branchphone = models.CharField(max_length=14,blank=True)