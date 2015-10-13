from django.shortcuts import render
from .models import Blog, Message
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from django.http import HttpResponse
import json

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['date']
        
def main(request):
    form = {}
    response = 'You message has been submitted'
    response2 = 'All fields have to be filled'
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name != "" and subject != "" and email != "" and message != "":
            m = Message(name=name, subject=subject, email=email, message=message)
            m.save()
            
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            return HttpResponse(json.dumps(response2), content_type="application/json")
    else:
        form = MessageForm()
    return render(request, 'index.html', {'form':form})
    

def posts(request):
    posts = Blog.objects.all().order_by("-date")
    paginator = Paginator(posts, 4)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
        
    return render(request, "blog.html", dict(posts=posts))
    
def detail(request, pk):
    post = Blog.objects.get(pk=int(pk))
    return render(request, "detail.html", dict(post=post))

    