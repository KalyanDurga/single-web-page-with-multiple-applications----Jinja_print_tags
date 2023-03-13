from django.shortcuts import render

# Create your views here.
def rcb(request):
    d={'name1':'KOHILI:THE KING ','name2':'ABD : MR 360','name3':'MAXWELL: The LEGEND'}
    return render(request,'csk.html',context=d)
