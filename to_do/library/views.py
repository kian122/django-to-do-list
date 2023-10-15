from django.shortcuts import render , redirect
from .models import Todo
from .forms import ToDoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserCreate
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import can_database_get

# Create your views here.

def index(request):
    # define

    if request.user.is_authenticated:
        if can_database_get(request) != False:
            database = Todo.objects.get( created_by = request.user )
        else:
            return HttpResponse("nothing")
        context = {
            "database":database,
        }
        return render(request , "library/main.html" , context)
    else:
        return HttpResponse('<a href="/create_user"> first please sign up </a>')

def create_index(request):
    #define
    form = ToDoForm( request.POST or None )

    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/error")

    context = {
        "database":form,
    }


    return render(request , "library/create.html" , context)

def update_view(request , pk):
    # define

    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Todo, id = pk)
 
    # pass the object as instance in form
    form = ToDoForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form

    return render(request , 'library/update.html' , context)

def delete_index(request , pk):
 
    # fetch the object related to passed id
    obj = get_object_or_404(Todo, id = pk)
 
    # pass the object as instance in form
 
    # save the data from the form and
    # redirect to detail_view
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
 
    # add form dictionary to context

    return render(request , 'library/delete.html')
    
def create_user(request):
    #define
    form = UserCreate()

    if request.method == "POST":
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("/")

    else:
        form = UserCreate()

    context = {
        "form":form
    }

    if not request.user.is_authenticated:
        return render(request , "library/create_user.html" , context)
    else:
        return HttpResponse('you are signed no need for another one <a href="/"> link to the home page </a>')

def error(request):
    return HttpResponse( "<p> please sign up for the create to do </p> <a href='/create_user'><button> sign up page</button> </a>" )

