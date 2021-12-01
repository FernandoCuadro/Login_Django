from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request, 'main/inicio.html',{})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"El usuario {nombre_usuario} ah sido creado")
            login(request, usuario)
            messages.info(request, f"Bienvenido: {nombre_usuario}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, "main/registro.html", {"form":form})   

def logout_request(request):
        logout(request)
        messages.info(request, f"Hasta luego!")
        return render(request, 'main/inicio.html',{})

def login_request(request):
    
    if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contraseña = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=contraseña)

                if user is not None:
                    login(request, user)
                    messages.info(request, f"Estas logueado como {usuario}")
                    return redirect("main:homepage")
                
                else:
                    messages.error(request, "Usuario o contraseña incorrecta")

            else:
                messages.error(request, "Usuario o contraseña incorrecta")

        

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form":form})
       
