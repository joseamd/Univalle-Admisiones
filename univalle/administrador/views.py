# -*- coding: utf-8 -*- 
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from univalle.administrador.forms import *
from univalle.administrador.models import *
from univalle.home.models import *
from django.core.mail import EmailMultiAlternatives #Enviamos html
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage#paginacion de Django
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned


# creamos nuestras vistas

def administrador_view(request):
	if request.user.is_authenticated():
		return render(request,'index_admin.html')
	else:
		return HttpResponseRedirect('/login')
	
def register_user_view(request):
	info="inicializado"
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=username, email=email, password=password_one)
			u.save()#guarda el usuario
			return render(request,'thanks_register.html')
		else:
			info = "Información con Datos incorrectos"
			ctx = {'form':form}
			return render(request,'registro_usuarios.html',ctx)

	ctx	= {'form':form}
	return render(request,'registro_usuarios.html', ctx)
	
def listar_usuario_view(request):
	if request.user.is_authenticated():
		return render(request,'listar_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def register_carrera_view(request):
	mensaje=""
	llamarMensaje=""
	form = CarreraForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = CarreraForm(request.POST)
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				nombre = form.cleaned_data['nombre']
				try:
					p = programasAcademico.objects.get(codigo=codigo)
				except programasAcademico.DoesNotExist:
					p = programasAcademico() #creo una instancia de la clase inscripcion
					p.codigo = codigo
					p.nombre = nombre
					p.save() #guardar inscripcion
					llamarMensaje= "Registro"
					mensaje= "Registro Satisfactorio!!!!!!"
					form = CarreraForm()
				else:
					llamarMensaje="NoRegistro"
					mensaje="Código de carrera ya existe"
			else:
				mensaje = "Datos erróneos"

		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_carreras.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def editar_carrera_view(request,codigo=None):
	mensaje = ""
	llamarMensaje=""
	p = programasAcademico.objects.get(codigo=codigo)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarCarreraForm(request.POST)
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				nombre = form.cleaned_data['nombre']
				p = programasAcademico() #creo una instancia de la clase inscripcion
				p.codigo = codigo
				p.nombre = nombre
				p.save() #guardar inscripcion
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				mensaje = "Datos erróneos"

		if request.method == "GET":
			form = EditarCarreraForm(initial={
				'codigo': p.codigo,
				'nombre': p.nombre,
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'editar_carreras.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def listar_carreras_view(request,pagina):
	if request.user.is_authenticated():
		lista_carr = programasAcademico.objects.filter(status=True)
		paginator = Paginator(lista_carr,10)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			carreras = paginator.page(page)
		except:
			carreras = paginator.page(paginator.num_pages)
			
		ctx = {'carreras':carreras}
		return render(request, 'listar_carreras.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
		
		
		
		
		
		
		
	
	