# Create your views here.

from blog.models import Author, Book
from django.shortcuts import render_to_response
def show_authors(req):
    authors=Author.objects.all()
    books=Book.objects.all()
    return render_to_response('index.html',{'authors':authors,'books':books})
	
