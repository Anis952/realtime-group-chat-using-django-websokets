from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def roomview(request):
    room_no= request.POST['room_no']
    room= request.POST['room']
    return render(request, 'room.html',{'room_no':room_no,'room':room})