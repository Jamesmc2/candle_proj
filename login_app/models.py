from django.db import models
import bcrypt
import re
from datetime import datetime


class UserManager(models.Manager):
    def basic_validator_reg(self,postData):
        errors ={}
        user = User.objects.filter(email = postData['email'])
        if user:
            errors['unique'] = 'This Email already has an account'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):             
            errors['email'] = "Invalid email address!"
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must contain at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last'] = 'Last name must contain at least 2 characters'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must contain at least 8 characters'
        if postData['password'] != postData['confirm_password'] :
            errors['confirm_password'] = 'Make sure your password field matches your confirm password field'
        if not len(postData['birthday']) == 0:
            birthday = datetime.fromisoformat(postData['birthday'])
            delta=((datetime.now()-birthday).days)/365
            if delta < 13:
                errors['birthday'] = 'You must be 13 years of age to create an account'
        else:
            errors['birthday'] = "please enter a valid birthday"
        return errors
    def basic_validator_login(self,postData):
        errors = {}
        user=User.objects.filter(email=postData['email'])
        if len(user) < 1:
            errors['no_email'] = 'There is no registered user with this Email'
            return errors
        if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors['wrong_password'] = 'Password is incorrect'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


