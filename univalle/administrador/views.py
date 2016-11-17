# -*- coding: utf-8 -*- 
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from univalle.administrador.forms import *
from univalle.administrador.models import *
from univalle.home.models import *
from django.core.mail import EmailMultiAlternatives #Enviamos html
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage#paginacion de Django
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
import simplejson
from django.contrib.auth.hashers import check_password#libreria para chequear password actual

# creamos nuestras vistas

def administrador_view(request):
	#muestra el index pero con el formulario de contacto
	nombre = ""
	correo = ""
	asunto = ""
	texto = ""
	mensaje=""
	llamarMensaje=""
	totalUsuarios= User.objects.count()#cuenta la cantidad de usuarios registrados
	totalInscripciones= inscripciones.objects.count()#cuenta la cantidad de usuarios registrados
	totalCarreras= programasAcademico.objects.count()#cuenta la cantidad de programas academicos
	form = CorreoForm()
	
	if request.user.is_authenticated():
		if request.method == "POST":
			form = CorreoForm(request.POST)
			if form.is_valid():
				llamarMensaje= "Registro"
				mensaje= "Mensaje Enviado!!!!!!"
				correo = form.cleaned_data['correo']
				asunto = form.cleaned_data['asunto']
				texto = form.cleaned_data['texto']
				
				#configuracion enviando mensaje via gmail
				to_admin = correo
				html_content ="<b>Asunto:</b> %s<br><br><b>Mensaje:</b><br><br>%s"%(asunto,texto)
				msg = EmailMultiAlternatives("Correo de Contacto",html_content,'from@server.com',[to_admin])
				msg.attach_alternative(html_content,'text/html')#definimos el contenido como HTML
				msg.send()#Enviamos el correo
				form = CorreoForm()
			else:
				llamarMensaje= "NoRegistro"
				mensaje= "Mensaje No Enviado!!!!!!"
				form = CorreoForm()
		ctx = {'form':form,'mensaje':mensaje, 'llamarMensaje':llamarMensaje, 'totalCarreras':totalCarreras,'totalUsuarios':totalUsuarios, 'totalInscripciones':totalInscripciones}
		return render(request,'index_admin.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def register_user_view(request):
	mensaje=""
	llamarMensaje=""
	form = RegistroUsuarioForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = RegistroUsuarioForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				email = form.cleaned_data['email']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
				try:
					u = User.objects.get(username=username)
				except User.DoesNotExist:
					if password_one == password_two:
						u = User.objects.create_user(username=username, email=email, password=password_one)
						u.save()#guarda el usuario
						llamarMensaje= "Registro"
						mensaje= "Registro Satisfactorio!!!!!!"
						form = RegistroUsuarioForm()
					else:
						llamarMensaje="NoRegistro"
						mensaje="Contraseña no coinciden"
				else:
					llamarMensaje="NoRegistro"
					mensaje="Datos incorrectos"
			else:
				llamarMensaje="NoRegistro"
				mensaje = "Correo ya registrado"
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def editar_usuario_view(request,pk=None):
	mensaje = ""
	llamarMensaje=""
	u = User.objects.get(pk=pk)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarUsuarioForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				email = form.cleaned_data['email']
				
				u = User()
				u.pk = pk
				u.username = username
				u.email = email
				u.save() #guardar usuario
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				mensaje = "Datos erróneos"
		#se carga el formulario con los datos del usuario a editar		
		if request.method == "GET":
			form = EditarUsuarioForm(initial={
				'username': u.username,
				'email': u.email,
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'editar_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')
	
def listar_usuario_view(request,pagina):
	#Metodo POST para eliminar usuario
	if request.user.is_authenticated():
		if request.method=="POST":
			if "programa_id" in request.POST:
				try:
					pk = request.POST['programa_id']
					u = User.objects.get(pk=pk)
					mensaje = {"status":"True","programa_id":u.pk}
					u.delete() # Eliminamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
					
	#Metodo  para listar usuarios				
		lista_user = User.objects.filter()
		paginator = Paginator(lista_user,7)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			usuarios = paginator.page(page)
		except:
			usuarios = paginator.page(paginator.num_pages)
			
		ctx = {'usuarios':usuarios}
		return render(request, 'listar_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def register_inscripcion_view(request):
	mensaje=""
	llamarMensaje=""
	form = RegistroInscripcionesForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = RegistroInscripcionesForm(request.POST)
			if form.is_valid():
				cedula = form.cleaned_data['cedula']
				nombre = form.cleaned_data['nombre']
				apellido = form.cleaned_data['apellido']
				snp = form.cleaned_data['snp']
				ref_pago = formulario.cleaned_data['ref_pago']
				programa = str(form.cleaned_data['programas_academicos'])
				try:
					i = inscripciones.objects.get(cedula=cedula)
				except inscripciones.DoesNotExist:
					i = inscripciones() #creo una instancia de la clase inscripcion
					
					i.cedula = cedula
					i.nombre = nombre
					i.apellido = apellido
					i.snp = snp
					i.ref_pago = ref_pago
					i.carrera = programa	
					
					i.save() #guardar inscripcion
					llamarMensaje= "Registro"
					mensaje= "Registro Satisfactorio!!!!!!"
					form = RegistroInscripcionesForm()
				else:
					llamarMensaje="NoRegistro"
					mensaje="Ya existe un usuario con este número de Cédula"
			else:
				mensaje = "Datos erróneos"
				
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def editar_inscripcion_view(request,cedula=None):
	mensaje = ""
	llamarMensaje=""
	i = inscripciones.objects.get(cedula=cedula)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarInscripcionesForm(request.POST)
			if form.is_valid():
				cedula = form.cleaned_data['cedula']
				nombre = form.cleaned_data['nombre']
				apellido = form.cleaned_data['apellido']
				snp = form.cleaned_data['snp']
				ref_pago = form.cleaned_data['ref_pago']
				programa = str(form.cleaned_data['programas_academicos'])#convierto el objeto a string
				
				i = inscripciones() #creo una instancia de la clase inscripcion
				
				i.cedula = cedula
				i.nombre = nombre
				i.apellido = apellido
				i.snp = snp
				i.ref_pago = ref_pago
				i.carrera = programa
				
				i.save() #guardar inscripcion
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				mensaje = "Datos erróneos"

		if request.method == "GET":
			form = EditarInscripcionesForm(initial={
				'cedula': i.cedula,
				'nombre': i.nombre,
				'apellido': i.apellido,
				'snp': i.snp,
				'programas_academicos': i.carrera,
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'editar_inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def listar_inscripciones_view(request,pagina):
	#Metodo POST para eliminar inscripcion
	if request.user.is_authenticated():
		if request.method=="POST":
			if "programa_id" in request.POST:
				try:
					cedula = request.POST['programa_id']
					i = inscripciones.objects.get(cedula=cedula)
					mensaje = {"status":"True","programa_id":i.cedula}
					i.delete() # Eliminamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
					
	#Metodo  para listar inscripciones				
		lista_inscrip = inscripciones.objects.filter(status=True)
		paginator = Paginator(lista_inscrip,7)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			inscripcion = paginator.page(page)
		except:
			inscripcion = paginator.page(paginator.num_pages)
			
		ctx = {'inscripcion':inscripcion}
		return render(request, 'listar_inscripciones.html',ctx)
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
					p = programasAcademico() #creo una instancia de la clase programaAcademico
					p.codigo = codigo
					p.nombre = nombre
					p.save() #guardar programa
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
	#Metodo POST para eliminar programa academico
	if request.user.is_authenticated():
		if request.method=="POST":
			if "programa_id" in request.POST:
				try:
					codigo = request.POST['programa_id']
					p = programasAcademico.objects.get(codigo=codigo)
					mensaje = {"status":"True","programa_id":p.codigo}
					p.delete() # Eliminamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
					
	#Metodo  para listar programas academicos				
		lista_carr = programasAcademico.objects.filter(status=True)
		paginator = Paginator(lista_carr,7)
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
		
def editar_password_view(request,username=None):
	mensaje = ""
	llamarMensaje = ""
	form = EditarPasswordForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarPasswordForm(request.POST)
			if form.is_valid():
				password_actual = form.cleaned_data['password_actual']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
				u = User.objects.get(username=username)
				if check_password(password_actual, u.password):
					print 'Contrasena de usuario coincide'
					if password_one == password_two:
						u.set_password(password_one)
						#u.save()
						llamarMensaje= "Registro"
						mensaje= "Su contraseña se cambió correctamente!!!!!!"
						form = EditarPasswordForm()
					else:
						llamarMensaje="NoRegistro"
						mensaje="Contraseña nueva NO coinciden"
				else:
					llamarMensaje="NoRegistro"
					mensaje="Contrasena Actual NO coincide"
			else:
				llamarMensaje="NoRegistro"
				mensaje="Error de datos"
			
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'editar_password.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		