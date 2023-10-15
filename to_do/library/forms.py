from .models import Todo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def can_database_get( request):
    try:
        return Todo.objects.get( created_by = request.user )
    except Todo.DoesNotExist:
        return False

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'name',
            'description',
        ]

class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]