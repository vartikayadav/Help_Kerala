from django.views.generic import TemplateView
from django.shortcuts import render
from details.models import details
class TestPage(TemplateView):
    template_name="index.html"

class ThanksPage(TemplateView):
    template_name="thanks.html"
# class IndexPage(TemplateView):
#     template_name="index.html"
def index(request):
    context={
    'details':details
    }
    
    return render(request,"index.html",context)
