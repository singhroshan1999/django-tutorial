from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# from first_app.forms import User as UserForm

# login imports

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST)
        user_portfolio = forms.UserPortfolioForm(data = request.POST)
        
        if user_form.is_valid() and user_portfolio.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hashing password
            user.save() 
            
            profile = user_portfolio.save(commit = False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,user_portfolio.errors)
    else:
        user_form = forms.UserForm()
        user_portfolio = forms.UserPortfolioForm()
    
    return render(request,'first_app/registration.html',{'registered':registered,'user_form':user_form,'port_f':user_portfolio})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userr = authenticate(username = username,password = password)
    
        if userr:
            if userr.is_active:
                login(request,userr)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('USER NOT ACTIVE')
        else:
            print('username or password incorrect')
            return HttpResponse('username or password incorrect')
    else:
        return render(request,'first_app/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def only_login_user_can_see(request):
    return HttpResponse("Youre loged in")
