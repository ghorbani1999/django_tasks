from django.db import models

class tasks(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    done = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.title

class person(models.Model):
    name = models.CharField(max_length=250)
    sex_choices = [('M','Male'),('F','Female'),('O','others')]
    sex = models.CharField(choices=sex_choices,max_length=1)

# Create your models here.
