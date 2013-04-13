from django.shortcuts import render_to_response
from django.template import RequestContext
from newsajax.newsajax.models import Noticias
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect
import simplejson as json
from newsajax.noticias.forms import Noticiasform
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def ver_noticias(request, id_usuario, pagina):
    usuario = User.objects.get(id=id_usuario)
    lista_noticias = Noticias.objects.filter(user=id_usuario)
    paginator = Paginator(lista_noticias, 3)
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        noticias = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticias = paginator.page(paginator.num_pages)
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('noticias/noticias.html', {'noticias': noticias, 'usuario': usuario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def ver_noticias_alone(request, id_noticia):
    noticia = Noticias.objects.filter(id=id_noticia)
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('noticias/noticias_alone.html', {'noticia': noticia, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def add_notice(request):
    formulario = Noticiasform()
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response('noticias/add_notice.html', {'formulario': formulario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def add_notice_ajax(request):
    if request.is_ajax() and request.method == "POST":
        info_enviado = False
        errores = ''
        formulario = Noticiasform(request.POST, request.FILES)
        usuario = User.objects.get(pk=request.user.id)
        usuario_id = request.user.id
        if formulario.is_valid():
            author = formulario.save(commit=False)
            author.user = usuario
            author.save()
            formulario.save(commit=True)
            info_enviado = True
        else:
            errores = formulario.errors
        response = {'info_enviado': info_enviado, 'errores': errores, 'usuario_id': usuario_id}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404


def eliminar(request, id_noticia):
    noticia = Noticias.objects.get(pk=id_noticia)
    id = request.user.id
    noticia.delete()
    return HttpResponseRedirect(reverse('newsajax.noticias.views.ver_noticias', args=(id, 1, )))


def editar(request, id_noticia):
    noticia = Noticias.objects.get(id=id_noticia)
    formulario = Noticiasform(instance=noticia)
    menu_noticias = Noticias.objects.filter()[0:10]
    return render_to_response("noticias/editar_noticia.html", {'formulario': formulario, 'menu_noticias': menu_noticias}, context_instance=RequestContext(request))


def editar_noticia_ajax(request):
    if request.is_ajax() and request.method == 'POST':
        noticia = Noticias.objects.get(pk=request.POST['id_noticia'])
        formulario = Noticiasform(request.POST, request.FILES, instance=noticia)
        usuario = User.objects.get(pk=request.user.id)
        errores = ''
        exito = False
        if formulario.is_valid():
            n = formulario.save(commit=False)
            n.user = usuario
            n.save()
            formulario.save(commit=True)
            exito = True
        else:
            errores = formulario.errors
        response = {'exito': exito, 'errores': errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404
