# Create your views here.
from django.utils import timezone
from .models import Video, Pagina, Service, ImagenesPrincipales
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import FormularioForm
from django.contrib import messages

def form(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            # Configurar la fecha y hora de solicitud con la zona horaria 'America/Bogota'
            form.instance.fecha_solicitud = timezone.now()  # Asignamos la fecha y hora actual en la zona horaria predeterminada de Django

            form.save()
            messages.success(request, 'Solicitud enviada correctamente. En breve nos pondremos en contacto con usted')
            # Puedes agregar una redirección después de guardar los datos exitosamente
            return redirect('servicios')
    else:
        form = FormularioForm()
        pagina_formulario = get_object_or_404(Pagina, pagename='Formulario')
        pageslogan = pagina_formulario.pageslogan
        pagetitle = pagina_formulario.pagetitle
        pagename = pagina_formulario.pagename
        pagebanner = pagina_formulario.pagebanner
        pagebannermov = pagina_formulario.pagebannermov
        pagemetatitle = pagina_formulario.pagemetatitle
        pageogdesc = pagina_formulario.pageogdesc
        pagekeywords = pagina_formulario.pagekeywords
        pagemetadesc = pagina_formulario.pagemetadesc
        pageogurl = pagina_formulario.pageogurl
        pageogimg = pagina_formulario.pageogimg
        pageogurlsec = pagina_formulario.pageogurlsec
        return render(request, 'formulario-solicitud.html', {
            'pagina': pagina_formulario,
            'form': form,
            'pagemetatitle': pagemetatitle,
            'pageogdesc': pageogdesc,
            'pagekeywords': pagekeywords,
            'pagemetadesc': pagemetadesc,
            'pageogurl': pageogurl,
            'pageogimg': pageogimg,
            'pageogurlsec': pageogurlsec,
            'pagebanner': pagebanner,
            'pagename': pagename,
            'pagebannermov': pagebannermov,
            'pagetitle': pagetitle,
            'pageslogan': pageslogan,
        })

def servicios(request):
    pagina_servicios = get_object_or_404(Pagina, pagename='Servicios')
    pageslogan = pagina_servicios.pageslogan
    pagetitle = pagina_servicios.pagetitle
    pagename = pagina_servicios.pagename
    pagebanner = pagina_servicios.pagebanner
    pagebannermov = pagina_servicios.pagebannermov
    pagemetatitle = pagina_servicios.pagemetatitle
    pageogdesc = pagina_servicios.pageogdesc
    pagekeywords = pagina_servicios.pagekeywords
    pagemetadesc = pagina_servicios.pagemetadesc
    pageogurl = pagina_servicios.pageogurl
    pageogimg = pagina_servicios.pageogimg
    pageogurlsec = pagina_servicios.pageogurlsec
    return render(request, 'servicios.html', {
        'pagina': pagina_servicios,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        })

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'servicio-detalle.html'
    context_object_name = 'servicio'

    def get_object(self):
        return get_object_or_404(Service, serviceurl=self.kwargs['serviceurl'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['metatitulo'] = self.object.servicemetatitle
        context['titulo'] = self.object.servicename
        context['keywords'] = self.object.servicekeywords
        context['mdescription'] = self.object.servicemetadesc
        context['ogurl'] = self.object.serviceogurl
        context['ogimg'] = self.object.serviceogimg
        context['ogurlimg'] = self.object.serviceogurlsec
        context['ogdesc'] = self.object.serviceogdesc

        # Agregar la lista de promociones al contexto
        # promos = Promo.objects.all()
        # context['promos'] = promos

        return context
    
def pauta(request):
    pagina_pauta = get_object_or_404(Pagina, pagename='Pauta')
    comments = Comment.objects.all()
    pageslogan = pagina_pauta.pageslogan
    pagetitle = pagina_pauta.pagetitle
    pagename = pagina_pauta.pagename
    pagebanner = pagina_pauta.pagebanner
    pagebannermov = pagina_pauta.pagebannermov
    pagemetatitle = pagina_pauta.pagemetatitle
    pageogdesc = pagina_pauta.pageogdesc
    pagekeywords = pagina_pauta.pagekeywords
    pagemetadesc = pagina_pauta.pagemetadesc
    pageogurl = pagina_pauta.pageogurl
    pageogimg = pagina_pauta.pageogimg
    pageogurlsec = pagina_pauta.pageogurlsec
    return render(request, 'pauta.html', {
        'pagina': pagina_pauta,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        'comments': comments,
        })

def cookies(request):
    pagina_cookies = get_object_or_404(Pagina, pagename='Cookies')
    pageslogan = pagina_cookies.pageslogan
    pagetitle = pagina_cookies.pagetitle
    pagename = pagina_cookies.pagename
    pagebanner = pagina_cookies.pagebanner
    pagebannermov = pagina_cookies.pagebannermov
    pagemetatitle = pagina_cookies.pagemetatitle
    pageogdesc = pagina_cookies.pageogdesc
    pagekeywords = pagina_cookies.pagekeywords
    pagemetadesc = pagina_cookies.pagemetadesc
    pageogurl = pagina_cookies.pageogurl
    pageogimg = pagina_cookies.pageogimg
    pageogurlsec = pagina_cookies.pageogurlsec
    return render(request, 'cookies.html', {
        'pagina': pagina_cookies,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        'comments': comments,
        })

def privacy(request):
    pagina_privacy = get_object_or_404(Pagina, pagename='Privacy')
    pageslogan = pagina_privacy.pageslogan
    pagetitle = pagina_privacy.pagetitle
    pagename = pagina_privacy.pagename
    pagebanner = pagina_privacy.pagebanner
    pagebannermov = pagina_privacy.pagebannermov
    pagemetatitle = pagina_privacy.pagemetatitle
    pageogdesc = pagina_privacy.pageogdesc
    pagekeywords = pagina_privacy.pagekeywords
    pagemetadesc = pagina_privacy.pagemetadesc
    pageogurl = pagina_privacy.pageogurl
    pageogimg = pagina_privacy.pageogimg
    pageogurlsec = pagina_privacy.pageogurlsec
    return render(request, 'privacy.html', {
        'pagina': pagina_privacy,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        'comments': comments,
        })

def index(request):
    carrusel = ImagenesPrincipales.objects.all()
    video = get_object_or_404(Video, videoname='Video intro')
    videourl = video.videourl
    pagina_home = get_object_or_404(Pagina, pagename='Home')
    pageslogan = pagina_home.pageslogan
    pagetitle = pagina_home.pagetitle
    pageogdesc = pagina_home.pageogdesc
    pagename = pagina_home.pagename
    pagebanner = pagina_home.pagebanner
    pagebannermov = pagina_home.pagebannermov
    pagemetatitle = pagina_home.pagemetatitle
    pagekeywords = pagina_home.pagekeywords
    pagemetadesc = pagina_home.pagemetadesc
    pageogurl = pagina_home.pageogurl
    pageogimg = pagina_home.pageogimg
    pageogurlsec = pagina_home.pageogurlsec
    context= {
        'carrusel': carrusel,
        'pageogdesc':pageogdesc,
        'pageslogan': pageslogan,
        'pagetitle': pagetitle,
        'pagename': pagename,
        'pagebanner': pagebanner,
        'pagebannermov': pagebannermov,
        'pagemetatitle': pagemetatitle,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'videourl':videourl,
    }
    return render(request, 'home.html', context)

def contacto(request):
    pagina_contacto = get_object_or_404(Pagina, pagename='Contacto')
    pageslogan = pagina_contacto.pageslogan
    pagetitle = pagina_contacto.pagetitle
    pagename = pagina_contacto.pagename
    pagebanner = pagina_contacto.pagebanner
    pagebannermov = pagina_contacto.pagebannermov
    pagemetatitle = pagina_contacto.pagemetatitle
    pageogdesc = pagina_contacto.pageogdesc
    pagekeywords = pagina_contacto.pagekeywords
    pagemetadesc = pagina_contacto.pagemetadesc
    pageogurl = pagina_contacto.pageogurl
    pageogimg = pagina_contacto.pageogimg
    pageogurlsec = pagina_contacto.pageogurlsec
    return render(request, 'contacto.html', {
        'pagina': pagina_contacto,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        })

def nosotros(request):
    pagina_nosotros = get_object_or_404(Pagina, pagename='Nosotros')
    pageslogan = pagina_nosotros.pageslogan
    pagetitle = pagina_nosotros.pagetitle
    pagename = pagina_nosotros.pagename
    pagebanner = pagina_nosotros.pagebanner
    pagebannermov = pagina_nosotros.pagebannermov
    pagemetatitle = pagina_nosotros.pagemetatitle
    pageogdesc = pagina_nosotros.pageogdesc
    pagekeywords = pagina_nosotros.pagekeywords
    pagemetadesc = pagina_nosotros.pagemetadesc
    pageogurl = pagina_nosotros.pageogurl
    pageogimg = pagina_nosotros.pageogimg
    pageogurlsec = pagina_nosotros.pageogurlsec
    return render(request, 'nosotros.html', {
        'pagina': pagina_nosotros,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan,
        })

def comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'partials/comments.html', context)

def carrusels(request):
    carrusel = ImagenesPrincipales.objects.all()
    context = {
        'carrusel': carrusel,
    }
    return render(request, 'partials/carrusel.html', context)

# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)

def robots(request):
    return render(request, 'robots.txt')
