from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse     # or we can import HttpResponse from django.http
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm     # importing signup form and login form
from django.contrib.auth import authenticate, login as loginUser, logout
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.

#def home(request):     
#    print('Hello World.. this is home')    # browser will request to server then print() in server
#    return HttpResponse("Response from views file")     # If successfuly returned then server will send response to browser


@login_required(login_url='login')    # This Decorater  --> If we are not login then then function should not work!!
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')   # It will fetch all todos in home page
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})   # render will read all the html from index.html file and return it to home 

    
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()     # created object here
        context = {
        "form" : form
        }                        # we pass context to dictionary
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')    # cleaned_data is a dictionary from it we will get username
            password = form.cleaned_data.get('password')   
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request,user)    # To store our information in server session once we login  # loginuser is imported from django.contrib.auth
                return redirect('home')

        else:   # return login page
            context = {
            "form" : form
            }                        
            return render(request, 'login.html', context=context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()    # created object here
        context = {
        "form" : form
        }                      # context is use to insert data in html form     
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)   # we will get all the data from browser to server.
        context = {
        "form" : form
        }
        if form.is_valid():    # Form validation is been checked by Django only by its form api
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')    # redirect(name of url)
        else:    
            return render(request, 'signup.html', context=context)    # return signup page

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})


def delete_todo(request, id):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('login')

