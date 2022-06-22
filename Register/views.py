from django.shortcuts import render
from form import my_form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

def view(request):
    form=my_form(request.POST)
    if request.method == "POST":
        form = my_form(request.POST)
        if form.is_valid():
            form.save()
#    if form.request=='POST':
#        form=AuthenticationForm(request, data=request.POST)
#        if form_is.valid():
#            form.save()
#            username=form.get.cleaned_data['username']
#            password=form.get.cleaned_data['password']
#            user=authenticate( username=username, password=password)
#            if user is not none:
#               login(request, user)
#               messages.info(request, f"You are now logged in as {username}.")
#               return render(request, 'home.html')
#           else:
#                
#                messages.error(request,"Invalid username or password.")
#        else:
#			messages.error(request,"Invalid username or password.")
#	form = AuthenticationForm()
#            
    return render(request,'signup.html',{'form': form})  

def prof(request):
    form=my_form(request.POST)
    name=my_form.objects.get('username')
    return render(request, 'profile.html', {'name':name})
    

def ciew(request):
	form = AuthenticationForm(request, data=request.POST)
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, 'post.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	return render(request,'login.html',{'login':form})