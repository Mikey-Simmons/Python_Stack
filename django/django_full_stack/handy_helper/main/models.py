from django.db import models
import re 

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name needs to be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last name needs to be at least 3 characters"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['invalid_password'] ="Passwords do not match!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors
    def login_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class JobManager(models.Manager):
    def job_validator(self,postData):
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = "Title must be more than 5 characters"
        if len(postData['desc']) < 5:
            errors['desc'] = "Description must be more than 5 characters"
        if len(postData['location']) < 5:
            errors['location'] = "Location must be more than 5 characters"
        
        return errors

class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    location = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name="jobs_uploaded",on_delete = models.CASCADE)
    user_to_do_job = models.ManyToManyField(User,related_name="users_jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
