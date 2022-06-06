from django.shortcuts import render, redirect
from chat.models import Usuario,Canal,Mensaje
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'chat/home.html')



def canal(request, canal):
    username = request.GET.get('username')
    canal_detalles = Canal.objects.get(name=canal)
    return render(request, 'chat/canal.html', {
        'username': username,
        'room': canal,
        'room_details': canal_detalles
    })

def check_canal(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Canal.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Canal.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_msg = Mensaje.objects.create(value=message, user=username, canal=room_id)
    new_msg.save()
    return HttpResponse('Mensaje enviado.')

def getMessages(request, canal):
    room_details = Canal.objects.get(name=canal)

    messages = Mensaje.objects.filter(canal=room_details.id)
    return JsonResponse({"messages":list(messages.values())})