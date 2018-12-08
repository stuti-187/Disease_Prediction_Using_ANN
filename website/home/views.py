from django.http import HttpResponse
from django.template import loader,Context

def home(request):
    template = loader.get_template('home/home.html')
    context=Context({})
    return HttpResponse(template.render(context))

# Create your views here.
