from django.shortcuts import render
from . import stat
# Create your views here.
def statistics(request):
    p,q,r,s,t=stat.records()
    context={
    'p':p,
    'q':q,
    'r':r,
    's':s,
    't':t
    }
    return render(request,"record/rout.html",context)
