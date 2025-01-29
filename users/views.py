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

#Create a view
@csrf_exempt
def view_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        view_name = data.get('view_name')

        if not view_name:
            return JsonResponse({'error': 'View name is required'}, status=400)

        view = View.objects.create(view_name=view_name)
        return JsonResponse({'id': view.id, 'view_name': view.view_name}, status=201)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Get the views
@csrf_exempt
def view_list(request):
    views= View.objects.all().values('id', 'view_name')
    return JsonResponse(list(views), safe=False)

#Edit the views
@csrf_exempt
def view_update(request, pk):
    view = get_object_or_404(View, pk=pk)

    if request.method == 'PATCH':
        data = json.loads(request.body)
        view_name = data.get('view_name')

        if not view_name:
            return JsonResponse({'error': 'View name is required'}, status=400)

        view.view_name = view_name
        view.save()
        return JsonResponse({'id': view.id, 'view_name': view.view_name}, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Delete the views
@csrf_exempt
def view_delete(request, pk):
    view = get_object_or_404(View, pk=pk)

    if request.method == 'DELETE':
        view.delete()
        return JsonResponse({'message': 'View deleted successfully'}, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Create feature
@csrf_exempt
def feature_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            feature_name = data.get('features_name')
        except json.JSONDecodeError:
            feature_name = request.POST.get('features_name')

        if not feature_name:
            return JsonResponse({'error': 'Feature name is required'}, status=400)

        feature = Features.objects.create(features_name=feature_name)
        return JsonResponse({'id': feature.id, 'features_name': feature.features_name}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Get feature
@csrf_exempt
def feature_list(request):
    views= Features.objects.all().values('id', 'features_name')
    return JsonResponse(list(views), safe=False)

#Edit Feature
@csrf_exempt
def feature_update(request, pk):
    feature = get_object_or_404(Features, pk=pk)

    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            feature_name = data.get('features_name')
        except json.JSONDecodeError:
            feature_name = request.POST.get('features_name')

        if not feature_name:
            return JsonResponse({'error': 'Feature name is required'}, status=400)

        feature.features_name = feature_name
        feature.save()
        return JsonResponse({'id': feature.id, 'features_name': feature.features_name}, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Delete feature
@csrf_exempt
def feature_delete(request, pk):
    feature = get_object_or_404(Features, pk=pk)
    if request.method == 'DELETE':
        feature.delete()
        return JsonResponse({'message': 'Feature deleted successfully'}, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

#Create new property
@csrf_exempt
def property_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = [
                'type_of_purchase', 
                'property_type_id', 
                'number_of_beds', 
                'price', 
                'area',
                'view_id',
                'reference_number',
                'features_id'
            ]
            
            # Check for required fields
            if not all(field in data for field in required_fields):
                return JsonResponse({
                    'error': f'Missing required fields. Required fields are: {", ".join(required_fields)}'
                }, status=400)
            
            # Validate type_of_purchase
            if data['type_of_purchase'] not in ['sale', 'rent']:
                return JsonResponse({
                    'error': 'type_of_purchase must be either "sale" or "rent"'
                }, status=400)

            # Create new property
            property = Property.objects.create(
                type_of_purchase=data['type_of_purchase'],
                property_type_id=data['property_type_id'],
                number_of_beds=data['number_of_beds'],
                price=data['price'],
                area=data['area'],
                view_id=data['view_id'],
                reference_number=data['reference_number'],
                features_id=data['features_id']
            )
            
            return JsonResponse({
                'id': property.id,
                'type_of_purchase': property.type_of_purchase,
                'property_type': property.property_type.property_type_name,
                'number_of_beds': property.number_of_beds,
                'price': str(property.price),
                'area': property.area,
                'view': str(property.view),
                'reference_number': property.reference_number,
                'features': str(property.features)
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
#Get all properties
@csrf_exempt
def property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        data = [{
            'id': prop.id,
            'type_of_purchase': prop.type_of_purchase,
            'property_type': prop.property_type.property_type_name,
            'number_of_beds': prop.number_of_beds,
            'price': str(prop.price),
            'area': prop.area,
            'view': str(prop.view),
            'reference_number': prop.reference_number,
            'features': str(prop.features)
        } for prop in properties]
        return JsonResponse(data, safe=False)

#Update a property
@csrf_exempt
def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    
    if request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            
            # Validate type_of_purchase if provided
            if 'type_of_purchase' in data and data['type_of_purchase'] not in ['sale', 'rent']:
                return JsonResponse({
                    'error': 'type_of_purchase must be either "sale" or "rent"'
                }, status=400)

            # Update fields if they exist in the request
            updatable_fields = [
                'type_of_purchase',
                'property_type_id',
                'number_of_beds',
                'price',
                'area',
                'view_id',
                'reference_number',
                'features_id'
            ]
            
            for field in updatable_fields:
                if field in data:
                    setattr(property, field, data[field])
            
            property.save()
            
            return JsonResponse({
                'id': property.id,
                'type_of_purchase': property.type_of_purchase,
                'property_type': property.property_type.property_type_name,
                'number_of_beds': property.number_of_beds,
                'price': str(property.price),
                'area': property.area,
                'view': str(property.view),
                'reference_number': property.reference_number,
                'features': str(property.features)
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

#Delete a property
@csrf_exempt
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    
    if request.method == 'DELETE':
        property.delete()
        return JsonResponse({'message': 'Property deleted successfully'})
    property = get_object_or_404(Property, pk=pk)
    
    if request.method == 'DELETE':
        property.delete()
        return JsonResponse({'message': 'Property deleted successfully'})