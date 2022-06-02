from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from chat.models import Mensaje, Usuario, Canal




def index(request):
    return HttpResponse('Hello, world. You are at the chat index.')
    #return msg_details( 1 )


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
def login_page(request):
    return render(request, 'listings/base.html')
'''