from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm, InventoryForm
from .models import StoreProfile, Inventory


def home(request):
    logout(request)
    if request.user.is_authenticated:
        store_list = StoreProfile.objects.filter(user=request.user)
        inventory_list = Inventory.objects.filter(store_profile__user=request.user)
    else:
        store_list = StoreProfile.objects.all()
        inventory_list = Inventory.objects.all()
    
    return render(request, 'home.html', {'store_list': store_list, 'inventory_list': inventory_list})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect logged-in users to the dashboard
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the newly registered user
            
            # Create a StoreProfile object for the user
            StoreProfile.objects.create(user=user, store_name='', address='', zip_code='', phone='', email_address='', description='')
            
            messages.success(request, 'Account was created successfully')
            return redirect('loginPage')  # Redirect to the dashboard page after registration
    
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect logged-in users to the dashboard
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if a StoreProfile object exists for the user
            if not StoreProfile.objects.filter(user=user).exists():
                StoreProfile.objects.create(user=user, store_name='', address='', zip_code='', phone='', email_address='', description='')
            
            return redirect('dashboard')  # Redirect to the dashboard page after login
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    return render(request, 'login.html')


@login_required(login_url='loginPage')
def dashboard(request):
    store_profile = StoreProfile.objects.get(user=request.user)
    products = Inventory.objects.filter(store_profile=store_profile)

    if request.method == 'POST':
        if 'store_name' in request.POST:
            # Save Store Profile
            store_profile.store_name = request.POST.get('store_name')
            store_profile.address = request.POST.get('address')
            store_profile.zip_code = request.POST.get('zip_code')
            store_profile.phone = request.POST.get('phone')
            store_profile.email_address = request.POST.get('email_address')
            store_profile.description = request.POST.get('description')
            store_profile.save()
        elif 'product_name' in request.POST:
            # Add new product
            product_name = request.POST.get('product_name')
            product_description = request.POST.get('product_description')
            price = request.POST.get('price')
            Inventory.objects.create(store_profile=store_profile, product_name=product_name, product_description=product_description, price=price)
        return redirect('dashboard')

    context = {
        'store_profile': store_profile,
        'products': products
    }
    return render(request, 'dashboard.html', context)



def add_product(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.store_profile = StoreProfile.objects.get(user=request.user)
            product.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InventoryForm()
    
    return render(request, 'add_product.html', {'form': form})



def delete_product(request, product_id):
    # Retrieve the product instance
    product = get_object_or_404(Inventory, pk=product_id)
    
    # Check if the user owns the product (optional, if needed)
    if product.store_profile.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this product.")

    # Delete the product
    product.delete()

    # Redirect back to the dashboard or any other appropriate page
    return redirect('dashboard')

def edit_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('edit_product_name')
        product_description = request.POST.get('edit_product_description')
        price = request.POST.get('edit_price')

        # Retrieve the product instance
        product = Inventory.objects.get(pk=product_id)

        # Update the product details
        product.product_name = product_name
        product.product_description = product_description
        product.price = price
        product.save()

        # Return a JSON response indicating success
        return redirect('dashboard')

