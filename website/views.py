from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .Forms import SignUpForm, AdminUpdateUserPasswordForm, AddSpecialismRecordForm, AddDoctorRecordForm, AddHospitalRecordForm, UpdateUserForm, UpdateUserPasswordForm
from.models import Hospital_Record, Doctor_Record, Doctor_Specialism

# Home Page View and Login View

def home(request):
	# Log user in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			# Log valid user in
			login(request, user)
			messages.success(request, "You Have Been Logged In Successfully.")
			return redirect('home')
		else:
			# Deny invalid access attempts
			messages.success(request, "There Was An Error Logging In, Please Try Again.")
			return redirect('home')
	else:
		return render(request, 'home.html')
	
#Custom 404 Error Pages

def custom_404(request, exception):
    return render(request, 'error_templates/404.html', status=404)

def custom_500(request):
	return render(request, 'error_templates/500.html', status=500)


# Logout a Logged in user

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out Successfully.")
	return redirect('home')

# Create a new system user

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

# List Record Views

def list_hospitals(request):
	list_hospitals = Hospital_Record.objects.all()
	return render(request, 'hospital_templates/list_hospitals.html', {'list_hospitals':list_hospitals})

def list_doctors(request):
	list_doctors = Doctor_Record.objects.all()
	return render(request, 'doctor_templates/list_doctors.html', {'list_doctors':list_doctors})

def list_specialisms(request):
	list_specialisms = Doctor_Specialism.objects.all()
	return render(request, 'specialism_templates/list_specialisms.html', {'list_specialisms':list_specialisms})

def list_users(request):
	if request.user.is_authenticated and request.user.is_superuser:	
		list_users = User.objects.filter(is_superuser=False)
		return render(request, 'admin_templates/list_users.html', {'list_users':list_users})
	else:
		messages.success(request, "You have to be an Admin to view the Admin Portal")
		return redirect('home')

# Add Record Views

def add_specialism(request):
		form = AddSpecialismRecordForm(request.POST or None)
		if request.user.is_authenticated:
			if request.method == "POST":
				if form.is_valid():
					add_specialism = form.save()
					messages.success(request, "Specialism Record Added")
					return redirect('list_specialisms')
			return render(request, 'specialism_templates/add_specialism.html', {'form':form})
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
			return render(request, 'doctor_templates/add_doctor.html', {'form':form})
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
			return render(request, 'hospital_templates/add_hospital.html', {'form':form})
		else:
			messages.success(request, "You have to be logged in to add a new Hospital")
			return redirect('home')
		
def add_user(request):
		form = SignUpForm(request.POST or None)
		if request.user.is_authenticated and request.user.is_superuser:
			if request.method == "POST":
				if form.is_valid():
					add_user = form.save()
					messages.success(request, "User Added")
					return redirect('list_users')
			return render(request, 'admin_templates/add_user.html', {'form':form})
		else:
			messages.success(request, "You have to be an admin in to add a New User from inside the Portal")
			return redirect('home')

# Record Views

def record_doctor(request, pk):
	if request.user.is_authenticated:
		record_doctor = Doctor_Record.objects.get(id=pk)
		return render(request, 'doctor_templates/record_doctor.html', {'record_doctor':record_doctor})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def record_specialism(request, pk):
	if request.user.is_authenticated:
		record_specialism = Doctor_Specialism.objects.get(id=pk)
		return render(request, 'specialism_templates/record_specialism.html', {'record_specialism':record_specialism})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')	

def record_hospital(request, pk):
	if request.user.is_authenticated:
		record_hospital = Hospital_Record.objects.get(id=pk)
		return render(request, 'hospital_templates/record_hospital.html', {'record_hospital':record_hospital})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')	
	
def record_user(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		record_user = User.objects.get(id=pk)
		return render(request, 'admin_templates/record_user.html', {'record_user':record_user})
	else:
		messages.success(request, "You must be an Admin to view this page")
		return redirect('home')


def list_doctors_by_hospital(request, hospital_id):
	if request.user.is_authenticated:
            hospital = get_object_or_404(Hospital_Record, pk=hospital_id)
            doctors = hospital.hospital_doctors.all()
            return render(request, 'doctor_templates/list_doctors_by_hospital.html', {'hospital': hospital, 'doctors':doctors})

# Update Record Views

def update_specialism(request, pk):
	if request.user.is_authenticated:
		current_specialism_record = Doctor_Specialism.objects.get(id=pk)
		form = AddSpecialismRecordForm(request.POST or None, instance=current_specialism_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Specialism Record has been updated")
			return redirect('home')
		return render(request, 'specialism_templates/update_specialism.html', {'form':form})
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
		return render(request, 'hospital_templates/update_hospital.html', {'form':form})
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
		return render(request, 'doctor_templates/update_doctor.html', {'form':form})
	else:
		messages.success(request, "You have to be logged in")
		return redirect('home')

def update_user(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        current_user_record = User.objects.get(id=pk)
        form = UpdateUserForm(request.POST or None, instance=current_user_record)
        if form.is_valid():
            form.save()
            messages.success(request, "User Record has been updated")
            return redirect('list_users')
        return render(request, 'admin_templates/update_user.html', {'form': form})
    else:
        messages.success(request, "You have to be an admin to update a user")
        return redirect('home')

# Update Password Views

def update_user_password(request, pk):
    if request.user.is_authenticated:
        current_user_record = User.objects.get(id=pk)
        form = UpdateUserPasswordForm(request.POST or None, instance=current_user_record)
        if form.is_valid():
            form.save()
            messages.success(request, "User Password has been updated")
            return redirect('list_users')
        return render(request, 'update_user_password.html', {'form': form})
    else:
        messages.success(request, "You have to be logged to update a password")
        return redirect('home')

def admin_update_user_password(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        user = User.objects.get(pk=pk)
        form = AdminUpdateUserPasswordForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User Password has been updated")
            return redirect('list_users')
        return render(request, 'admin_templates/admin_update_user_password.html', {'form': form})
    else:
        messages.success(request, "You have to be a superuser to update a user's password")
        return redirect('home')

# Deletion Views

def delete_specialism(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_specialism = Doctor_Specialism.objects.get(id=pk)
		delete_specialism.delete()
		messages.success(request, "You have deleted this Specialism Record")
		return redirect('list_specialisms')
	else:
		messages.success(request, "You have to be logged in to delete a Specialism Record")
		return redirect('list_specialisms')
	
def delete_hospital(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_hospital = Hospital_Record.objects.get(id=pk)
		delete_hospital.delete()
		messages.success(request, "You have deleted this Hospital Record")
		return redirect('list_hospitals')
	else:
		messages.success(request, "You have to be an admin in to delete a Hospital Record")
		return redirect('list_hospitals')
	
def delete_doctor(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_doctor = Doctor_Record.objects.get(id=pk)
		delete_doctor.delete()
		messages.success(request, "You have deleted this Doctor Record")
		return redirect('list_doctors')
	else:
		messages.success(request, "You have to be logged in to delete a Doctor Record")
		return redirect('list_doctors')
	
def delete_user(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		delete_user = User.objects.get(id=pk)
		delete_user.delete()
		messages.success(request, "You have deleted this User Record")
		return redirect('list_users')
	else:
		messages.success(request, "You have to be an Admin to delete a User Record")
		return redirect('home')