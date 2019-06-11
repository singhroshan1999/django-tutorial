from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
#####
def index(request):
    return render(request,'first_app/index.html')

def form_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            print("VALIDATION SUCCESSFUL")
            print(request.POST)
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: '+form.cleaned_data['email'])
            print('text: '+form.cleaned_data['text'])
    return render(request,'first_app/form.html',context={'form':form})

def add_user(request):
    form = forms.NewUsers()
    if request.method == 'POST':
        form = forms.NewUsers(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('add_user ERROR')
            
    return render(request,'first_app/user_form.html',context={'form':form})

def relative_path(request):
    return render(request,'first_app/relative_path.html')

def template_filter(request):
    context_dict = {'hw':"hello world!",'num':128}
    return render(request,'first_app/template_filters.html',context_dict)