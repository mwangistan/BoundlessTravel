from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=90)
    body = RichTextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="%Y")
    
    def __unicode__(self):
        return self.title
    
class Message(models.Model):
    subject = models.CharField(max_length=150)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.subject
    