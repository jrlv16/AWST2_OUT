from django.shortcuts import render, get_object_or_404
from .models import Page
from django.conf.urls import url
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

# Create your views here.

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink = pagename)
    
    context = {
        'title' : pg.title,
        'content' : pg.bodytext,
        'page_list' : Page.objects.all(),
        }
    
    # assert False # permet de tester l'affichage de la page
    
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
            ['jl062705@sfr.fr'],
            connection=con
            )
        return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html',
{'form': form, 'page_list': Page.objects.all(),
'submitted': submitted})    