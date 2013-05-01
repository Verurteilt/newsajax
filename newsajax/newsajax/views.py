from django.shortcuts import render_to_response
from django.template import RequestContext
from newsajax.newsajax.forms import ContactForm
from newsajax.newsajax.forms import RegisterForm
from newsajax.newsajax.forms import LoginForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
import simplejson as json
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth.models import User
from newsajax.newsajax.models import Noticias


def index(request):
    menu_noticias = Noticias.objects.filter()[0:10]
    noticia_muro = Noticias.objects.order_by('-pk')[0:1]
    return render_to_response('index.html', {'menu_noticias': menu_noticias, 'noticia_muro': noticia_muro}, context_instance=RequestContext(request))


def about(request):
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('about.html', {'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def about_author(request):
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('about_author.html', {'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def contacto(request):
    formulario = ContactForm()
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('formularios/contacto.html', {'formulario': formulario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def contacto_ajax(request):
    if request.is_ajax() and request.method == "POST":
        info_enviado = False
        email = ""
        texto = ""
        errores = ""
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['email']
            texto = formulario.cleaned_data['texto']
            # Configuracion enviando mensaje via GMAIL
            to_admin = 'mini.guero@hotmail.com'
            html_content = "Informacion recibida de [%s] <br><br><br>***Mensaje****<br><br>%s" % (email, texto)
            msg = EmailMultiAlternatives('Correo de Contacto', html_content, 'from@server.com', [to_admin])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
        else:
            errores = formulario.errors
        response = {'info_enviado': info_enviado, 'errores': errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404


def login(request):
    formulario = LoginForm()
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('formularios/login.html', {'formulario': formulario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def login_ajax(request):
    if request.is_ajax() and request.method == "POST":
        exito = False
        formulario = LoginForm(request.POST)
        errores = ''
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuario = auth_authenticate(username=username, password=password)
            if usuario is not None and usuario.is_active:
                exito = True
                auth_login(request, usuario)
                return HttpResponseRedirect('/')
        else:
            errores = formulario.errors
        response = {'errores': errores, 'exito': exito}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def registro(request):
    formulario = RegisterForm()
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('formularios/registro.html', {'formulario': formulario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def registro_ajax(request):
    if request.is_ajax() and request.method == "POST":
        formulario = RegisterForm(request.POST)
        exito = True
        errores = ''
        password = ''
        password2 = ''
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            email = formulario.cleaned_data['email']
            password = formulario.cleaned_data['password']
            password2 = formulario.cleaned_data['password2']
            if password2 == password and password2 != "" and password != "":
                usuario = User.objects.create_user(username, email, password2)
                usuario.is_active = True
                exito = True
                usuario.save()
            else:
                exito = False
        else:
            errores = formulario.errors
            exito = False
        response = {'exito': exito, 'errores': errores, 'password': password, 'password2': password2}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404
