from django.db import models

class person(models.Model):
    name = models.CharField(max_length=250)
    sex_choices = [('M','Male'),('F','Female'),('O','others')]
    sex = models.CharField(choices=sex_choices,max_length=1)

    def sex_name(self):
        if self.sex == 'M' :
             return 'مرد'
        elif self.sex == 'F': 
             return 'زن'
        elif self.sex == 'O' :
             return 'سایر'



class tasks(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    done = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    assigned = models.ForeignKey(person,on_delete=models.SET_NULL , blank=True, null=True)
    def __str__(self):
        return self.title             


# Create your models here.
