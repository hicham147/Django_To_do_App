from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=400)
    complit = models.BooleanField(default=False)
    creted = models.TimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complit']