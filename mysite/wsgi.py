from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(mysite.wsgi.application)
