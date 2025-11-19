from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm, InventoryForm
from .models import StoreProfile, Inventory


def home(request):
    # Don't logout automatically - allow guest users to view stores
    if request.user.is_authenticated:
        # Logged in users see all stores but can only edit their own
        store_list = StoreProfile.objects.all()
        inventory_list = Inventory.objects.all()
    else:
        # Guest users can view all stores and products
        store_list = StoreProfile.objects.all()
        inventory_list = Inventory.objects.all()
    
    return render(request, 'home.html', {'store_list': store_list, 'inventory_list': inventory_list})


def logoutPage(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect logged-in users to the dashboard
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the newly registered user
            
            # Create a StoreProfile object for the user (one per user)
            if not StoreProfile.objects.filter(user=user).exists():
                StoreProfile.objects.create(
                    user=user, 
                    store_name='', 
                    address='', 
                    zip_code='', 
                    phone='', 
                    email_address=user.email, 
                    description=''
                )
            
            messages.success(request, 'Account Created Successfully! Let\'s set up your store details.')
            return redirect('dashboard')  # Redirect to the dashboard page after registration
    
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect logged-in users to the dashboard
    
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Validation matching iOS app
        if not email or not password:
            messages.error(request, 'Please enter email and password')
            return render(request, 'login.html')
        
        # Email format validation
        import re
        pattern = r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
        if not re.match(pattern, email, re.IGNORECASE):
            messages.error(request, 'Enter a valid email address')
            return render(request, 'login.html')
        
        email = email.lower().strip()
        
        # Try to find user by email (since we use email as username)
        try:
            user = User.objects.get(email=email)
            # Authenticate using the username (which is the email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            messages.error(request, 'Account not found')
            return render(request, 'login.html')
        
        if user is not None:
            login(request, user)
            
            # Check if a StoreProfile object exists for the user, create if not
            if not StoreProfile.objects.filter(user=user).exists():
                StoreProfile.objects.create(
                    user=user, 
                    store_name='', 
                    address='', 
                    zip_code='', 
                    phone='', 
                    email_address=user.email, 
                    description=''
                )
            
            return redirect('dashboard')  # Redirect to the dashboard page after login
        else:
            messages.error(request, 'Incorrect password')
    
    return render(request, 'login.html')


@login_required(login_url='loginPage')
def dashboard(request):
    # Get or create store profile for the logged-in user
    store_profile, created = StoreProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'store_name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'email_address': request.user.email,
            'description': ''
        }
    )
    
    # Only show products that belong to this user's store
    products = Inventory.objects.filter(store_profile=store_profile)
    
    # Check if store profile is complete (matching iOS app logic)
    def is_store_complete(profile):
        """Check if all required fields are filled and email is valid"""
        import re
        all_fields_filled = (
            profile.store_name and profile.store_name.strip() and
            profile.address and profile.address.strip() and
            profile.zip_code and profile.zip_code.strip() and
            profile.phone and profile.phone.strip() and
            profile.email_address and profile.email_address.strip() and
            profile.description and profile.description.strip()
        )
        # Email format validation
        email_pattern = r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
        email_valid = bool(re.match(email_pattern, profile.email_address or '', re.IGNORECASE))
        return all_fields_filled and email_valid
    
    is_complete = is_store_complete(store_profile)

    if request.method == 'POST':
        if 'store_name' in request.POST:
            # Save Store Profile
            store_profile.store_name = request.POST.get('store_name', '').strip()
            store_profile.address = request.POST.get('address', '').strip()
            store_profile.zip_code = request.POST.get('zip_code', '').strip()
            store_profile.phone = request.POST.get('phone', '').strip()
            store_profile.email_address = request.POST.get('email_address', '').strip()
            store_profile.description = request.POST.get('description', '').strip()
            store_profile.save()
            messages.success(request, 'Store details saved successfully')
            # Refresh to update is_complete status
            return redirect('dashboard')
        elif 'product_name' in request.POST:
            # Add new product - ensure it's linked to this user's store
            product_name = request.POST.get('product_name', '').strip()
            product_description = request.POST.get('product_description', '').strip()
            price = request.POST.get('price')
            
            # Validate price
            try:
                price = float(price)
                if price < 0:
                    messages.error(request, 'Price cannot be negative')
                else:
                    # Check for duplicate product names in this store
                    if Inventory.objects.filter(store_profile=store_profile, product_name__iexact=product_name).exists():
                        messages.error(request, 'Product with this name already exists')
                    else:
                        Inventory.objects.create(
                            store_profile=store_profile,
                            user=request.user,  # Also set user for consistency
                            product_name=product_name, 
                            product_description=product_description, 
                            price=price
                        )
                        messages.success(request, 'Product added successfully')
            except (ValueError, TypeError):
                messages.error(request, 'Invalid price')
        return redirect('dashboard')

    context = {
        'store_profile': store_profile,
        'products': products,
        'is_store_complete': is_complete
    }
    return render(request, 'dashboard.html', context)



@login_required(login_url='loginPage')
def add_product(request):
    # Get the user's store profile
    store_profile = get_object_or_404(StoreProfile, user=request.user)
    
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.store_profile = store_profile
            product.user = request.user  # Also set user for consistency
            
            # Check for duplicate product names in this store
            product_name = product.product_name.strip()
            if Inventory.objects.filter(store_profile=store_profile, product_name__iexact=product_name).exists():
                messages.error(request, 'Product with this name already exists in your store')
            else:
                product.save()
                messages.success(request, 'Product added successfully')
                return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InventoryForm()
    
    return render(request, 'add_product.html', {'form': form})



@login_required(login_url='loginPage')
def delete_product(request, product_id):
    # Retrieve the product instance
    product = get_object_or_404(Inventory, pk=product_id)
    
    # Check if the user owns the product (security check)
    if product.store_profile.user != request.user:
        messages.error(request, "You don't have permission to delete this product.")
        return redirect('dashboard')

    # Delete the product
    product.delete()
    messages.success(request, 'Product deleted successfully')

    # Redirect back to the dashboard
    return redirect('dashboard')

@login_required(login_url='loginPage')
def edit_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('edit_product_name', '').strip()
        product_description = request.POST.get('edit_product_description', '').strip()
        price = request.POST.get('edit_price')

        # Retrieve the product instance
        try:
            product = Inventory.objects.get(pk=product_id)
        except Inventory.DoesNotExist:
            messages.error(request, 'Product not found')
            return redirect('dashboard')

        # Check if the user owns the product (security check)
        if product.store_profile.user != request.user:
            messages.error(request, "You don't have permission to edit this product.")
            return redirect('dashboard')

        # Validate price
        try:
            price = float(price)
            if price < 0:
                messages.error(request, 'Price cannot be negative')
                return redirect('dashboard')
        except (ValueError, TypeError):
            messages.error(request, 'Invalid price')
            return redirect('dashboard')

        # Check for duplicate product names (excluding current product)
        if Inventory.objects.filter(
            store_profile=product.store_profile, 
            product_name__iexact=product_name
        ).exclude(pk=product_id).exists():
            messages.error(request, 'Product with this name already exists in your store')
            return redirect('dashboard')

        # Update the product details
        product.product_name = product_name
        product.product_description = product_description
        product.price = price
        product.save()
        
        messages.success(request, 'Product updated successfully')

        # Return a JSON response indicating success
        return redirect('dashboard')
    
    return redirect('dashboard')

