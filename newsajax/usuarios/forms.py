from django import forms


class EditForm1(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=False)
    edad = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Edad'}), required=False)
    dedicacion = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Escribe a que te dedicas'}), required=False)
    photo = forms.ImageField(label='Imagen de Perfil', required=False)
