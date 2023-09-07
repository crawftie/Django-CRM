from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .Forms import SignUpForm, AddUserRecordForm
from.models import Record

# views 
def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In Successfully.")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again.")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out Successfully.")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			# Authenticate user and Login
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have registered")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})

def user_record(request, pk):
	if request.user.is_authenticated:
		user_record = Record.objects.get(id=pk)
		return render(request, 'user_record.html', {'user_record':user_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def delete_user_record(request, pk):
	if request.user.is_authenticated:
		delete_record_user = Record.objects.get(id=pk)
		delete_record_user.delete()
		messages.success(request, "You have deleted this record")
		return redirect('home')
	else:
		messages.success(request, "You have to be logged in to delete this")
		return redirect('home')
	
def add_user_record(request):
		form = AddUserRecordForm(request.POST or None)
		if request.user.is_authenticated:
			if request.method == "POST":
				if form.is_valid():
					add_user_record = form.save()
					messages.success(request, "Record Added")
					return redirect('home')
			return render(request, 'add_user_record.html', {'form':form})
		else:
			messages.success(request, "You have to be logged in to make a new user")
			return redirect('home')
		
def update_user_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddUserRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has been updated")
			return redirect('home')
		return render(request, 'update_user_record.html', {'form':form})
	else:
		messages.success(request, "You have to be logged in")
		return redirect('home')
			