from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .Forms import SignUpForm, AddUserRecordForm, AddSpecialismRecordForm, AddDoctorRecordForm, AddHospitalRecordForm
from.models import Record, Hospital_Record, Doctor_Record, Doctor_Specialism

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
	
def list_hospitals(request):
	list_hospitals = Hospital_Record.objects.all()
	return render(request, 'list_hospitals.html', {'list_hospitals':list_hospitals})

def list_doctors(request):
	list_doctors = Doctor_Record.objects.all()
	return render(request, 'list_doctors.html', {'list_doctors':list_doctors})

def list_specialisms(request):
	list_specialisms = Doctor_Specialism.objects.all()
	return render(request, 'list_specialisms.html', {'list_specialisms':list_specialisms})

def add_specialism(request):
		form = AddSpecialismRecordForm(request.POST or None)
		if request.user.is_authenticated:
			if request.method == "POST":
				if form.is_valid():
					add_specialism = form.save()
					messages.success(request, "Specialism Record Added")
					return redirect('list_specialisms')
			return render(request, 'add_specialism.html', {'form':form})
		else:
			messages.success(request, "You have to be logged in to make a new specialism")
			return redirect('home')

def add_doctor(request):
		form = AddDoctorRecordForm(request.POST or None)
		if request.user.is_authenticated:
			if request.method == "POST":
				if form.is_valid():
					add_doctor = form.save()
					messages.success(request, "Doctor Record Added")
					return redirect('list_doctors')
			return render(request, 'add_doctor.html', {'form':form})
		else:
			messages.success(request, "You have to be logged in to add a new Doctor")
			return redirect('home')
		
def add_hospital(request):
		form = AddHospitalRecordForm(request.POST or None)
		if request.user.is_authenticated:
			if request.method == "POST":
				if form.is_valid():
					add_hospital = form.save()
					messages.success(request, "Hospital Record Added")
					return redirect('list_hospitals')
			return render(request, 'add_hospital.html', {'form':form})
		else:
			messages.success(request, "You have to be logged in to add a new Hospital")
			return redirect('home')

def record_doctor(request, pk):
	if request.user.is_authenticated:
		record_doctor = Doctor_Record.objects.get(id=pk)
		return render(request, 'record_doctor.html', {'record_doctor':record_doctor})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def record_specialism(request, pk):
	if request.user.is_authenticated:
		record_specialism = Doctor_Specialism.objects.get(id=pk)
		return render(request, 'record_specialism.html', {'record_specialism':record_specialism})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')	

def record_hospital(request, pk):
	if request.user.is_authenticated:
		record_hospital = Hospital_Record.objects.get(id=pk)
		return render(request, 'record_hospital.html', {'record_hospital':record_hospital})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')	

def list_doctors_by_hospital(request, hospital_id):
	if request.user.is_authenticated:
            hospital = get_object_or_404(Hospital_Record, pk=hospital_id)
            doctors = hospital.hospital_doctors.all()
            return render(request, 'list_doctors_by_hospital.html', {'hospital': hospital, 'doctors':doctors})

def update_specialism(request, pk):
	if request.user.is_authenticated:
		current_specialism_record = Doctor_Specialism.objects.get(id=pk)
		form = AddSpecialismRecordForm(request.POST or None, instance=current_specialism_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Specialism Record has been updated")
			return redirect('home')
		return render(request, 'update_specialism.html', {'form':form})
	else:
		messages.success(request, "You have to be logged in")
		return redirect('home')
	
def update_hospital(request, pk):
	if request.user.is_authenticated:
		current_specialism_record = Hospital_Record.objects.get(id=pk)
		form = AddHospitalRecordForm(request.POST or None, instance=current_specialism_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Hospital Record has been updated")
			return redirect('home')
		return render(request, 'update_hospital.html', {'form':form})
	else:
		messages.success(request, "You have to be logged in")
		return redirect('home')	
	
def update_doctor(request, pk):
	if request.user.is_authenticated:
		current_specialism_record = Doctor_Record.objects.get(id=pk)
		form = AddDoctorRecordForm(request.POST or None, instance=current_specialism_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Doctor Record has been updated")
			return redirect('home')
		return render(request, 'update_doctor.html', {'form':form})
	else:
		messages.success(request, "You have to be logged in")
		return redirect('home')	
	
def delete_specialism(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_specialism = Doctor_Specialism.objects.get(id=pk)
		delete_specialism.delete()
		messages.success(request, "You have deleted this Specialism")
		return redirect('home')
	else:
		messages.success(request, "You have to be logged in to delete this")
		return redirect('home')
	
def delete_hospital(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_hospital = Hospital_Record.objects.get(id=pk)
		delete_hospital.delete()
		messages.success(request, "You have deleted this Hospital")
		return redirect('home')
	else:
		messages.success(request, "You have to be an admin in to delete this")
		return redirect('home')
	
def delete_doctor(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_doctor = Doctor_Record.objects.get(id=pk)
		delete_doctor.delete()
		messages.success(request, "You have deleted this Doctor")
		return redirect('home')
	else:
		messages.success(request, "You have to be logged in to delete this")
		return redirect('home')