from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
#from .models import User
from .models import User, Property, PropertyType, View, Features


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

# Add a new property type
@csrf_exempt
def property_type_create(request):
    if request.method == 'POST':
        property_type_name = request.POST.get('property_type_name')

        if not property_type_name:
            return JsonResponse({'error': 'Property type name is required'}, status=400)

        property_type = PropertyType.objects.create(property_type_name=property_type_name)
        return JsonResponse({'id': property_type.id, 'property_type_name': property_type.property_type_name}, status=201)

# List all property types
@csrf_exempt
def property_type_list(request):
    if request.method == 'GET':
        property_types = PropertyType.objects.all()
        data = [{'id': pt.id, 'property_type_name': pt.property_type_name} for pt in property_types]
        return JsonResponse(data, safe=False, status=200)

# Edit an existing property type
@csrf_exempt
def property_type_update(request, pk):
    property_type = get_object_or_404(PropertyType, pk=pk)

    if request.method == 'PATCH':
        # Read JSON data from the body
        data = json.loads(request.body)
        property_type_name = data.get('property_type_name')

        if not property_type_name:
            return JsonResponse({'error': 'Property type name is required'}, status=400)

        property_type.property_type_name = property_type_name
        property_type.save()
        return JsonResponse({
            'id': property_type.id, 
            'property_type_name': property_type.property_type_name
        }, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Delete a property type
@csrf_exempt
def property_type_delete(request, pk):
    property_type = get_object_or_404(PropertyType, pk=pk)

    if request.method == 'DELETE':
        property_type.delete()
        return JsonResponse({'message': 'Property type deleted successfully'}, status=200)

