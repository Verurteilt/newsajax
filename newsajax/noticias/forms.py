from django import forms 
from newsajax.newsajax.models import Noticias

class Noticiasform(forms.ModelForm):
		class Meta:
			model = Noticias
			fields = ('titulo', 'contenido', 'photo')