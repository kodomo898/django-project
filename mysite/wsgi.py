from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(wsgi.application)
