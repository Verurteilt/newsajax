from django.shortcuts import render_to_response
from django.template import RequestContext
from newsajax.newsajax.models import userProfile
from django.contrib.auth.models import User
from newsajax.usuarios.forms import EditForm1
from django.http import Http404
from django.http import HttpResponse
import simplejson as json
from newsajax.newsajax.models import Noticias


def perfil_ver(request, id_usuario):
    usuario = User.objects.get(pk=id_usuario)
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('usuarios/perfil.html', {'usuario': usuario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def editar(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    formulario = EditForm1()
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response("usuarios/editar_perfil.html", {'formulario': formulario, 'usuario': usuario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def editar_ajax(request):
    if request.is_ajax() and request.method == 'POST':
        usuario = User.objects.get(pk=request.POST['id_usuario'])
        formulario = EditForm1(request.POST, request.FILES)
        try:
            userProfile.objects.create(user=usuario)
        except:
            pass
        errores = ''
        exito = False
        if formulario.is_valid():
            usuario.email = formulario.cleaned_data['email']
            usuario.get_profile().edad = formulario.cleaned_data['edad']
            usuario.get_profile().dedicacion = formulario.cleaned_data['dedicacion']
            usuario.get_profile().photo = formulario.cleaned_data['photo']
            usuario.save()
            usuario.get_profile().save()
            exito = True
        else:
            errores = formulario.errors
        response = {'exito': exito, 'errores': errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404
