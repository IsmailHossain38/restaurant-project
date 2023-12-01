from django.shortcuts import render

# Create your views here.
def aboutUs(request,ide):
    return render(request,'about/abouts.html',{'ide' : ide})
