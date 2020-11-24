from django.db import models

class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] =  "Title should be more than 2 characters"
        return errors  

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=10, default ="01/01/2020")
    desc = models.CharField(max_length=500)
    network = models.CharField(max_length=100)
    objects = TVShowManager()
