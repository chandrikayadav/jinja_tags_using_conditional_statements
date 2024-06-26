from django.shortcuts import render

def jinja_tags(request):
    d={'name':'chandu','age':19}
    return render(request,'jinja_tags.html',context=d)