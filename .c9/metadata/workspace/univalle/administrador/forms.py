{"changed":true,"filter":false,"title":"forms.py","tooltip":"/univalle/administrador/forms.py","value":"# -*- coding: utf-8 -*- \nfrom django import forms\nfrom django.contrib.auth.models import User\nfrom univalle.administrador.models import *\nfrom univalle.home.models import *\n\nclass RegistroUsuarioForm(forms.Form):\n\tusername = forms.CharField(label=\"Nombre de Usuario\",widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':\"Ingrese Usuario\"}))\n\temail = forms.EmailField(label=\"Correo Electrónico\",widget=forms.TextInput(attrs={'type':\"text\",'class':\"form-control\",'placeholder':\"Ingrese Correo Electrónico\"}))\n\tpassword_one = forms.CharField(label=\"Contraseña\",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':\"form-control\",'placeholder':\"Ingrese Contraseña\"}))\n\tpassword_two = forms.CharField(label=\"Confirmar Contraseña\",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':\"form-control\",'placeholder':\"Confirme Contraseña\"}))\n\t\t\n\t#validar si ya existe el correo \n\tdef clean_email(self):\n\t\temail = self.cleaned_data['email']\n\t\ttry:\n\t\t\tu = User.objects.get(email=email)\n\t\texcept User.DoesNotExist:\n\t\t\treturn email #para que valide el formulario como si fuera correcto\n\t\traise forms.ValidationError('Correo ya registrado')\n\t\t\nclass EditarUsuarioForm(forms.Form):\n\tusername = forms.CharField(label=\"Nombre de Usuario\",widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':\"Ingrese Usuario\"}))\n\temail = forms.EmailField(label=\"Correo Electrónico\",widget=forms.TextInput(attrs={'type':\"text\",'class':\"form-control\",'placeholder':\"Ingrese Correo Electrónico\"}))\n\t\nclass CarreraForm(forms.Form):\n    codigo = forms.IntegerField(label=\"Código\",widget=forms.TextInput(attrs={'required': True,'type':\"number\",'class':\"form-control\",'placeholder':'Ingrese Código'}))\n    nombre = forms.CharField(label=\"Nombre\",widget=forms.TextInput(attrs={'required': True,'type':\"text\",'class':\"form-control\",'placeholder':'Ingrese Nombre'}))\n\nclass EditarCarreraForm(forms.Form):\n    codigo = forms.IntegerField(label=\"Código\",widget=forms.TextInput(attrs={'required': True,'type':\"number\",'class':\"form-control\",'placeholder':'Ingrese Código','readonly':\"readonly\"}))\n    nombre = forms.CharField(label=\"Nombre\",widget=forms.TextInput(attrs={'required': True,'type':\"text\",'class':\"form-control\",'placeholder':'Ingrese Nombre'}))\n\nclass RegistroInscripcionesForm(forms.Form):\n\tcedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':\"number\",'class':\"form-control\",'placeholder':'Ingrese Número de Cédula'}))\n\tnombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':'Ingrese Nombres'}))\n\tapellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':'Ingrese Apellidos'}))\n\tsnp = forms.CharField(label='Código SNP',widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':'Ingrese su SNP'}))\n\tprogramas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':\"form-control\"}), queryset=programasAcademico.objects.all())\n\nclass EditarInscripcionesForm(forms.Form):\n\tcedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':\"number\",'class':\"form-control\",'placeholder':'Ingrese Número de Cédula','readonly':\"readonly\"}))\n\tnombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':'Ingrese Nombres'}))\n\tapellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':'Ingrese Apellidos'}))\n\tsnp = forms.CharField(label='Código SNP',widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':'Ingrese su SNP'}))\n\tprogramas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':\"form-control\"}), queryset=programasAcademico.objects.all())\n","undoManager":{"mark":-2,"position":50,"stack":[[{"start":{"row":19,"column":53},"end":{"row":20,"column":1},"action":"insert","lines":["","\t"],"id":407,"ignore":true}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["\t"],"id":408,"ignore":true}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":409,"ignore":true}],[{"start":{"row":21,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["class RegistroUsuarioForm(forms.Form):","\tusername = forms.CharField(label=\"Nombre de Usuario\",widget=forms.TextInput(attrs={'required': True,'type':\"text\", 'class':\"form-control\",'placeholder':\"Ingrese Usuario\"}))","\temail = forms.EmailField(label=\"Correo Electrónico\",widget=forms.TextInput(attrs={'type':\"text\",'class':\"form-control\",'placeholder':\"Ingrese Correo Electrónico\"}))","\tpassword_one = forms.CharField(label=\"Contraseña\",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':\"form-control\",'placeholder':\"Ingrese Contraseña\"}))","\tpassword_two = forms.CharField(label=\"Confirmar Contraseña\",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':\"form-control\",'placeholder':\"Confirme Contraseña\"}))",""],"id":410,"ignore":true}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":14},"action":"remove","lines":["Registro"],"id":411,"ignore":true},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["E"]}],[{"start":{"row":21,"column":7},"end":{"row":21,"column":11},"action":"insert","lines":["dita"],"id":412,"ignore":true}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["r"],"id":413,"ignore":true}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":414,"ignore":true}],[{"start":{"row":22,"column":170},"end":{"row":22,"column":191},"action":"insert","lines":["'readonly':\"readonly\""],"id":415,"ignore":true}],[{"start":{"row":22,"column":170},"end":{"row":22,"column":171},"action":"insert","lines":[","],"id":416,"ignore":true}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["\t"],"id":417,"ignore":true}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["i"],"id":418,"ignore":true}],[{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["s"],"id":419,"ignore":true}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["_"],"id":420,"ignore":true}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["s"],"id":421,"ignore":true}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["t"],"id":422,"ignore":true}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":8},"action":"insert","lines":["af"],"id":423,"ignore":true}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["f"],"id":424,"ignore":true}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":[" "],"id":425,"ignore":true}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["="],"id":426,"ignore":true}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":[" "],"id":427,"ignore":true}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":177},"action":"insert","lines":["forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':\"form-control\"}), queryset=programasAcademico.objects.all())"],"id":428,"ignore":true}],[{"start":{"row":11,"column":144},"end":{"row":11,"column":162},"action":"remove","lines":["programasAcademico"],"id":429,"ignore":true}],[{"start":{"row":11,"column":133},"end":{"row":11,"column":158},"action":"remove","lines":[", queryset=.objects.all()"],"id":430,"ignore":true}],[{"start":{"row":11,"column":133},"end":{"row":11,"column":158},"action":"insert","lines":[", queryset=.objects.all()"],"id":431,"ignore":true}],[{"start":{"row":11,"column":144},"end":{"row":11,"column":162},"action":"insert","lines":["programasAcademico"],"id":432,"ignore":true}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":177},"action":"remove","lines":[" forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':\"form-control\"}), queryset=programasAcademico.objects.all())"],"id":433,"ignore":true}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["="],"id":434,"ignore":true}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":10},"action":"remove","lines":["f "],"id":435,"ignore":true}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":8},"action":"remove","lines":["af"],"id":436,"ignore":true}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":6},"action":"remove","lines":["_st"],"id":437,"ignore":true}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":3},"action":"remove","lines":["is"],"id":438,"ignore":true}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["\t"],"id":439,"ignore":true}],[{"start":{"row":22,"column":170},"end":{"row":22,"column":171},"action":"remove","lines":[","],"id":440,"ignore":true}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["",""],"id":441,"ignore":true}],[{"start":{"row":19,"column":53},"end":{"row":20,"column":2},"action":"insert","lines":["","\t\t"],"id":442,"ignore":true}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["\t"],"id":443,"ignore":true}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["\t"],"id":444,"ignore":true}],[{"start":{"row":22,"column":170},"end":{"row":22,"column":171},"action":"insert","lines":[","],"id":445,"ignore":true}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["\t"],"id":446,"ignore":true}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["\t"],"id":447,"ignore":true}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["\t\t"],"id":448,"ignore":true}],[{"start":{"row":11,"column":2},"end":{"row":11,"column":4},"action":"insert","lines":["\t\t"],"id":449,"ignore":true}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["\t"],"id":450,"ignore":true}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":7},"action":"insert","lines":["\t\t"],"id":451,"ignore":true}],[{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["\t"],"id":452,"ignore":true}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["\t"],"id":453,"ignore":true}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":9},"action":"remove","lines":["\t\t\t"],"id":454,"ignore":true}],[{"start":{"row":11,"column":2},"end":{"row":11,"column":6},"action":"remove","lines":["\t\t\t\t"],"id":455,"ignore":true}],[{"start":{"row":24,"column":1},"end":{"row":26,"column":0},"action":"remove","lines":["password_one = forms.CharField(label=\"Contraseña\",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':\"form-control\",'placeholder':\"Ingrese Contraseña\"}))","\tpassword_two = forms.CharField(label=\"Confirmar Contraseña\",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':\"form-control\",'placeholder':\"Confirme Contraseña\"}))",""],"id":456,"ignore":true}],[{"start":{"row":22,"column":170},"end":{"row":22,"column":192},"action":"remove","lines":[",'readonly':\"readonly\""],"id":457,"ignore":true}]]},"ace":{"folds":[{"start":{"row":13,"column":23},"end":{"row":19,"column":53},"placeholder":"..."},{"start":{"row":26,"column":30},"end":{"row":32,"column":0},"placeholder":"..."}],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":34},"end":{"row":4,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1477778235656}