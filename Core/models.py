from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name