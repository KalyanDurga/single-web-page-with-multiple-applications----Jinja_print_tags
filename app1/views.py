from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name1':'DHONI : The FINISHER','name2':'RAINA : MR IPL','name3':'BRAVO : The CHAMPION'}
    return render(request,'csk.html',context=d)