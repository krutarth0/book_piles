from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . form import UserRegForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators	import login_required


# Create your views here.

def reg(request):
	if request.method=='POST':
		form=UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}, you are now able to sign in!')
			return redirect('login')
	else:
		form=UserRegForm()
	return render(request,'users/reg.html',{'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		u_updateForm = UserUpdateForm(request.POST,instance =request.user)
		p_updateForm = ProfileUpdateForm(request.POST,
											request.FILES,
											instance =request.user.profile)

		if u_updateForm.is_valid() and p_updateForm.is_valid():
			u_updateForm.save()
			p_updateForm.save()
			messages.success(request,f'Profile is updated')
			return redirect('profile')

	else:
		u_updateForm = UserUpdateForm(instance =request.user)
		p_updateForm = ProfileUpdateForm(instance =request.user.profile)

	contex = {
		'u_form' :u_updateForm,
		'p_form' :p_updateForm
	}

	return render(request,'users/profile.html',contex)

