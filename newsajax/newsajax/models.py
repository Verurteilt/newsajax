from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class userProfile(models.Model):
    """ userProfile modelos que actua como perfil """

    def url(self, filename):
        ruta = "MultimediaData/Users/%s/%s" % (self.user.username, filename)
        return ruta

    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to=url)
    edad = models.CharField(max_length=30)
    dedicacion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user.username


class Noticias(models.Model):
    """ Modelos de Noticias para aparecer en el index"""

    def url(self, filename):
        ruta = "MultimediaData/Users/%s/Noticias/%s" % (self.user.username, filename)
        return ruta

    user = models.ForeignKey(User)
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    photo = models.ImageField(upload_to=url)

    def __unicode__(self):
        return self.titulo

admin.site.register(userProfile)
admin.site.register(Noticias)
