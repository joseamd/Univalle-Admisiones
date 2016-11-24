{"changed":true,"filter":false,"title":"models.py","tooltip":"/univalle/home/models.py","value":"# -*- coding: utf-8 -*-\n\nfrom django.db import models\nfrom django.contrib.auth.models import User\n\n# Create your models here.\ndef url(obj, filename):\n\t\truta =\"MultimediaData/Users/%s/%s\"%(obj.user.username,filename)\n\t\treturn ruta\n\t\t\nclass userProfile(models.Model):\n\n\tuser \t\t= models.OneToOneField(User)\n\tphoto\t\t= models.ImageField(upload_to=url)\n\te_mail\t\t= models.EmailField(max_length=254)\n\n\tdef __unicode__(self):\n\t\treturn self.user.username\n\t\nclass programasAcademico(models.Model):\n\tcodigo\t\t=models.BigIntegerField(null=False, unique=True, primary_key=True)\n\tnombre\t\t=models.CharField(max_length=100)\n\tstatus\t\t=models.BooleanField(default=True)\n\n\n\tdef __unicode__(self):\n\t\treturn self.nombre\n\nclass inscripciones(models.Model):\n\tcedula\t\t=models.BigIntegerField(null=False, unique=True, primary_key=True)\n\tnombre\t\t=models.CharField(max_length=100)\n\tapellido\t=models.CharField(max_length=100)\n\tsnp\t\t\t=models.CharField(max_length=50)\n\tref_pago\t=models.IntegerField()\n\tcarrera\t\t=models.CharField(max_length=100)\n\tstatus\t\t=models.BooleanField(default=True)\n\n\tdef __str__(self):\n\t\treturn '%s - %s' % (self.cedula, self.snp)\n\t \n","undoManager":{"mark":-2,"position":-1,"stack":[]},"ace":{"folds":[],"scrolltop":245,"scrollleft":0,"selection":{"start":{"row":37,"column":1},"end":{"row":38,"column":44},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"timestamp":1478980245098}