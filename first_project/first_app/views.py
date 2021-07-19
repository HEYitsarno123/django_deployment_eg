from django.shortcuts import render
from first_app.forms import UserForm,UserProfileInfoForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request,'first_app/index.html');


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Youa are logged in ,Nice!")



def register_view(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request,"first_app/registration.html",context={"registered":registered,"user_form":user_form,"profile_form":profile_form});





def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        test = True
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')
        else:
            print("Someone tried to login and failed!")
            print("Usename: {} and password {}".format(username,password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request,'first_app/login.html',{})
