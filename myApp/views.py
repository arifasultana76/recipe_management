from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import *
# Create your views here.


@login_required
def homePage(request):
    return render(request,'home.html')

def signupPage(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        Confirm_Password=request.POST.get('Confirm_Password')
        user_types=request.POST.get('user_types')

        user_exist=CustomUser.objects.filter(username=username).exists()
        if user_exist:
            messages.warning(request, 'Username Already exist')
            return redirect('signup')
        if password==Confirm_Password:

            CustomUser.objects.create_user(
                full_name=full_name,
                username=username,
                email=email,
                password=password,
                user_types=user_types,
            )
            messages.success(request, "Account Created")
            return redirect('login')
        else:
            messages.warning(request, 'Password Didnot match')
            return redirect('signup')
    return render(request, 'auth/signup.html')

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Succesfully Login')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'auth/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def changepassword(request):
    if request.method=="POST":
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')

        if check_password(old_password, request.user.password):
            if new_password==confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Succesfully Changed password")
                return redirect('home')
    return render(request, "auth/changepassword.html")

@login_required
def categoryPage(request):
    categories=Category.objects.all()
    return render(request, 'category/category.html',{'categories':categories})

@login_required
def addcategoryPage(request):
    if request.method=="POST":
        Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        messages.success(request, "Succesfully Added data")
        return redirect('category')
    return render(request, 'category/addcategory.html')

@login_required
def editcategoryPage(request, id):
    category=Category.objects.get(id=id)
    if request.method=="POST":
        category.name=request.POST.get('name')
        category.description=request.POST.get('description')
        category.save()
        messages.success(request, "Succesfully Added data")
        return redirect('category')
    return render(request, 'category/editcategory.html', {'category':category})

@login_required
def deletecategoryPage(request, id):
    Category.objects.get(id=id).delete()
    return redirect('category')

@login_required
def viewcategoryPage(request, id):
    view=Category.objects.get(id=id)
    return render(request, 'category/viewcategory.html',{'view':view})

@login_required
def recipiePage(request):
    recipies=Recipie.objects.all()
    return render(request, 'recipie/recipie.html',{'recipies':recipies})


@login_required
def addrecipiePage(request):
    cate=Category.objects.all()
    
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        image=request.FILES.get('image')
        category_id=request.POST.get('category')
        category=Category.objects.get(id=category_id)
        user=request.user

        Recipie.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            image=image,
            category=category,
            created_by=user,
        )
        messages.success(request, 'Succsesfully Added Recipie')
        return redirect('recipie')
    return render(request, 'recipie/addrecipie.html',{'cate':cate})


@login_required
def editrecipiePage(request, id):
    recipie=Recipie.objects.get(id=id)
    cate=Category.objects.all()
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        ingredients=request.POST.get('ingredients')
        instructions=request.POST.get('instructions')
        image=request.FILES.get('image')
        category_id=request.POST.get('category')

        category=Category.objects.get(id=category_id)
        recipie.title=title
        recipie.description=description
        recipie.ingredients=ingredients
        recipie.instructions=instructions
        if image:
            recipie.image=image
        recipie.category=category
        recipie.save()
        messages.success(request, 'Succsesfully Added Recipie')
        return redirect('recipie')

    return render(request, 'recipie/editrecipie.html', {'recipie':recipie, 'cate':cate})


@login_required
def deleterecipiePage(request, id):
    Recipie.objects.get(id=id).delete()
    return redirect('recipie')


@login_required
def RecipeDetails(request, id):
    Recipe_Details=Recipie.objects.get(id=id)
    return render(request, 'recipie/recipiedetails.html',{'Recipe_Details':Recipe_Details})

