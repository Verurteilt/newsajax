from django import forms


class ContactForm(forms.Form):
	email	= forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=True )
	titulo	= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Titulo'}),  required=True)
	texto	= forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Escribe aqui Tu mensaje'}), required=True)


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario'}), required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'}), required=True)


class RegisterForm(forms.Form):
	username=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Usuario'}), required=True)
	email= forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email'}) , required=True)
	password=forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={'placeholder':'Password'}) , required=True)
	password2=forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={'placeholder':'Password Confirmation'}),  required=True)
