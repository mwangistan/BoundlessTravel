from django.contrib import admin
from .models import Blog, Message
from ckeditor.fields import RichTextField

class BlogAdmin(admin.ModelAdmin):
    body = RichTextField()
    filter = ( 'title')
    search_fields = ['title']
    
    class Meta:
        model = Blog
        
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ['subject', 'name', 'email', 'message', 'date']
    filter = ('date')   
    search_field = ['subject', 'name']
     
admin.site.register(Blog, BlogAdmin)
admin.site.register(Message, MessageAdmin)