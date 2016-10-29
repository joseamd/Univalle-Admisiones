{"changed":true,"filter":false,"title":"settings.py","tooltip":"/univalle/settings.py","value":"\"\"\"\nDjango settings for univalle project.\n\nGenerated by 'django-admin startproject' using Django 1.9.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.9/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.9/ref/settings/\n\"\"\"\n# -*- coding: utf-8 -*-\n\nimport os\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = '-1*qe%x7fekbsz=x*3eht8o$+o$-*!yu8gi5g9xzy#dhyuyi(x'\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = []\nSECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'univalle.home',\n    'univalle.administrador',\n]\n\nMIDDLEWARE_CLASSES = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'univalle.urls'\nAUTH_PROFILE_MODULE= 'home.userProfile'#identificar o definir el perfil de los usuarios\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [os.path.join(BASE_DIR, 'home/templates'),\n                 os.path.join(BASE_DIR, 'admin/templates'),],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'univalle.wsgi.application'\n\n# Database\n# https://docs.djangoproject.com/en/1.9/ref/settings/#databases\n\nDATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.postgresql_psycopg2',\n        'NAME': 'univalledb',\n        'USER': 'univalledbuser',\n        'PASSWORD': '94536998',\n        'HOST': '127.0.0.1',\n        'PORT': '5432',\n    }\n}\n\n# Password validation\n# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.9/topics/i18n/\n\nLANGUAGE_CODE = 'es-co'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.9/howto/static-files/\n\nSTATIC_URL = '/static/'\n\n#aqui va la configuracion del servidor de correo (gmail)\nEMAIL_HOST = 'smtp.gmail.com'\nEMAIL_PORT = 587\nEMAIL_HOST_USER = 'alexpoison100@gmail.com'\nEMAIL_HOST_PASSWORD = 'cedula94536998cali'\nEMAIL_USE_TLS = True\n\nMEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))\nMEDIA_URL = '/media/'\n\n#alex prueba    ","undoManager":{"mark":66,"position":66,"stack":[[{"start":{"row":41,"column":20},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["''"],"id":3}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["u"],"id":4}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["n"],"id":5}],[{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["i"],"id":6}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["v"],"id":7}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["a"],"id":8}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["l"],"id":9}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["l"],"id":10}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["e"],"id":11}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["."],"id":12}],[{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["a"],"id":13}],[{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["d"],"id":14}],[{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["m"],"id":15}],[{"start":{"row":42,"column":17},"end":{"row":42,"column":18},"action":"insert","lines":["i"],"id":16}],[{"start":{"row":42,"column":18},"end":{"row":42,"column":19},"action":"insert","lines":["n"],"id":17}],[{"start":{"row":62,"column":58},"end":{"row":63,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":63,"column":0},"end":{"row":63,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":63,"column":8},"end":{"row":63,"column":49},"action":"insert","lines":["os.path.join(BASE_DIR, 'home/templates'),"],"id":19}],[{"start":{"row":63,"column":8},"end":{"row":63,"column":12},"action":"insert","lines":["    "],"id":20}],[{"start":{"row":63,"column":12},"end":{"row":63,"column":16},"action":"insert","lines":["    "],"id":21}],[{"start":{"row":63,"column":16},"end":{"row":63,"column":20},"action":"insert","lines":["    "],"id":22}],[{"start":{"row":63,"column":16},"end":{"row":63,"column":20},"action":"remove","lines":["    "],"id":23}],[{"start":{"row":63,"column":16},"end":{"row":63,"column":17},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":63,"column":44},"end":{"row":63,"column":45},"action":"remove","lines":["e"],"id":25}],[{"start":{"row":63,"column":43},"end":{"row":63,"column":44},"action":"remove","lines":["m"],"id":26}],[{"start":{"row":63,"column":42},"end":{"row":63,"column":43},"action":"remove","lines":["o"],"id":27}],[{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"remove","lines":["h"],"id":28}],[{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"insert","lines":["a"],"id":29}],[{"start":{"row":63,"column":42},"end":{"row":63,"column":43},"action":"insert","lines":["d"],"id":30}],[{"start":{"row":63,"column":43},"end":{"row":63,"column":44},"action":"insert","lines":["m"],"id":31}],[{"start":{"row":63,"column":44},"end":{"row":63,"column":45},"action":"insert","lines":["i"],"id":32}],[{"start":{"row":63,"column":45},"end":{"row":63,"column":46},"action":"insert","lines":["n"],"id":33}],[{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":[","],"id":34}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["# "],"id":35}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"remove","lines":[" "],"id":36}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"remove","lines":["#"],"id":37}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"remove","lines":["'"],"id":38}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["'"],"id":39}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["."],"id":40}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"remove","lines":["e"],"id":41}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"remove","lines":["l"],"id":42}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"remove","lines":["l"],"id":43}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"remove","lines":["a"],"id":44}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"remove","lines":["v"],"id":45}],[{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"remove","lines":["i"],"id":46}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"remove","lines":["n"],"id":47}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"remove","lines":["u"],"id":48}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["u"],"id":49}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["n"],"id":50}],[{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["i"],"id":51}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["v"],"id":52}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["a"],"id":53}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["l"],"id":54}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["l"],"id":55}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["e"],"id":56}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["."],"id":57}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["# "],"id":58}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"remove","lines":[" "],"id":59}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"remove","lines":["#"],"id":60}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["i"],"id":61}],[{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["s"],"id":62}],[{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["t"],"id":63}],[{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["r"],"id":64}],[{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"insert","lines":["a"],"id":65}],[{"start":{"row":42,"column":24},"end":{"row":42,"column":25},"action":"insert","lines":["d"],"id":66}],[{"start":{"row":42,"column":25},"end":{"row":42,"column":26},"action":"insert","lines":["o"],"id":67}],[{"start":{"row":42,"column":26},"end":{"row":42,"column":27},"action":"insert","lines":["r"],"id":68}]]},"ace":{"folds":[],"scrolltop":366,"scrollleft":0,"selection":{"start":{"row":42,"column":27},"end":{"row":42,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":27,"state":"start","mode":"ace/mode/python"}},"timestamp":1477541605259}