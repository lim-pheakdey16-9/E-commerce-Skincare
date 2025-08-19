from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password 
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import brands
from .models import type
from .models import color
from .models import size
from .models import product

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
             
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                if user.is_superuser == 1:
                    return redirect('dashboard')
                else:
                    messages.success(request, "Login successful!")
                    return redirect('home')
            else:
                messages.error(request, "Account is not active.")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            username = request.POST.get('username', '').strip()
            email = request.POST.get('email', '').strip()
            password = request.POST.get('password', '').strip()
            con_password = request.POST.get('con_password', '').strip()

            # Validate fields
            if not all([first_name, last_name, username, email, password, con_password]):
                raise ValidationError("All fields are required.")

            # Validate email format
            validate_email(email)

            # Check if passwords match
            if password != con_password:
                raise ValidationError("Passwords do not match.")

            # Validate password strength
            validate_password(password)

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                raise ValidationError("Username already taken.")
            
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already registered.")

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            auth_login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('home')  

        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")

    return render(request, 'accounts/register.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

 
def home(request):
    return render(request, 'accounts/index.html')


@login_required
def dashboard(request):
    return render(request, 'accounts/admin/index.html')

def test(request):
    return render(request, 'accounts/admin/test.html')


def card(request):
    return render(request, 'accounts/web/card.html')

def shop(request):
    return render(request, 'accounts/web/shop.html')


def about(request):
    return render(request, 'accounts/web/about.html')

def contact(request):
    return render(request, 'accounts/web/contact.html')





def brand_list(request):
    brand = brands.objects.all().order_by('order')
 
    return render(request, 'accounts/admin/brand/index.html', {'brand': brand})

def create(request):
    if request.method == 'POST':
        name_kh = request.POST.get('name_kh')
        name_en = request.POST.get('name_en')
        order  = request.POST.get('order') 
        is_active = True if request.POST.get('is_active') else False
        image = request.POST.get('image')

        brands.objects.create(
            name_kh = name_kh, 
            name_en = name_en, 
            order  = order,
            is_active = is_active,
            image   = image,
        )
        return redirect('brand')
    return render(request, 'accounts/admin/brand/create.html')


def edit(request):

    return render(request, 'accounts/admin/brand/edit.html')


def delete(request):

    return redirect('index')





def type_list(request):
    types = type.objects.all().order_by('order')
    return render(request, 'accounts/admin/type/index.html', {'types': types})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        order = request.POST.get('order')

        type.objects.create( 
            name=name,
            order=order,
        )
        return redirect('type')
    return render(request, 'accounts/admin/type/create.html')
 




def product_list(request):
 
    return render(request, 'accounts/admin/product/index.html' )


def create(request):
    types = type.objects.all()
    brand = brands.objects.all()
    colors = color.objects.all()
    sizes = size.objects.all()
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            order = request.POST.get('order')
            type_id = request.POST.get('type_id')
            brand_id = request.POST.get('brand_id')
            color_id = request.POST.get('color_id')
            size_id = request.POST.get('size_id')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            
            # Validate required fields
            if not all([name, type_id, brand_id, price, image]):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('create')
            
            # Create the product
            new_product = product(
                name=name,
                order=order,
                type_id=type.objects.get(id=type_id),
                brand_id=brands.objects.get(id=brand_id),
                color_id=color.objects.get(id=color_id) if color_id else None,
                size_id=size.objects.get(id=size_id) if size_id else None,
                price=price,
                image=image
            )
            new_product.save()
           
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
        except Exception as e:
            messages.error(request, f'Error creating product: {str(e)}')
            return redirect('product')
    

    return render(request, 'accounts/admin/product/create.html', {
    'types': types,
    'brands': brand,
    'colors': colors,
    'sizes': sizes
    })