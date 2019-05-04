from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic import FormView,TemplateView
from .forms import ContatoForm

from .models import Noticia,MensagemDeContato

class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'

def detalhes(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    return render(request, 'app_noticias/detalhes.html', {'detalhes': post})

def noticia_detalhes(request, noticia_id):
    try:
        noticia = Noticia.objects.get(pk=noticia_id)
    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada.')
    return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})

def slug_view(request, pk): #como arrumar saporra
    try:
        '''noticia = Noticia.objects.all()'''
        '''tag = pk'''
        noticia = Noticia.objects.filter(tags__slug=pk).order_by('data_publicacao').reverse()
        
    except Noticia.DoesNotExist:
        raise Http404('Notícias não encontradas.')
    return render(request, 'app_noticias/slug.html', {'noticias': noticia,'tag':pk})

def noticias_resumo(request):
    total = Noticia.objects.count()
    html = """
    <html>
    <body>
    <h1>Resumo</h1>
    <p>A quantidade total de noticias é {}.</p>
    </body>
    </html>
    """.format(total)
    return HttpResponse(html)

def noticias_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total':total})


class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')
    
class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/contato_sucesso.html'