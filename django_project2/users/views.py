from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # By doing this form data is getting saved in the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})