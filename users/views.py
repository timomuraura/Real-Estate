from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User

# Display all users
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# Add a new user
def user_create(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')

        User.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            usertype=usertype,
        )
        return redirect('user_list')
    return render(request, 'users/user_form.html')

# Edit an existing user
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.firstname = request.POST.get('firstname')
        user.lastname = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.usertype = request.POST.get('usertype')
        user.save()
        return redirect('user_list')
    return render(request, 'users/user_form.html', {'user': user})

# Delete a user
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list')
