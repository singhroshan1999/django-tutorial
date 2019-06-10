from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage,AccessRecord

# Create your views here.
#####
def index(request):
    webp = AccessRecord.objects.order_by('date')
    my_dict = {'acc_rec':webp}
    return render(request,'first_app/index.html',context=my_dict)