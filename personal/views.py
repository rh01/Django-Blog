from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')


def contact(request):
	return render(request,'personal/basic.html',{'content':['If you like my website,Please email me!','heng960509@gmail.com']})