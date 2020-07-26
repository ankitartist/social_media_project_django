from django.db import models
from django.contrib import auth


#creating model for accounts that uses predefined django's User
class Usr(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

