from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from forms import SignUpForm

#from chat.models import Mensaje, Usuario, Canal

'''
def index(request, pk):
    # return HttpResponse('Hello, world. You are at the chat index.')
    return msg_details( 1 )


def msg_details(request, pk):
    msg = Mensaje.objects.get( pk=pk )
    emsr = Mensaje.objects.filter( emisor=msg.emisor )
    rcpt = Mensaje.objects.filter( receptor=msg.receptor )

    context = {
        'de': emsr,
        'para': rcpt,
    }

    return render( request, 'chat/vistas/msg_details.html', context )
'''


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})