from django.shortcuts import render
from .models import Rooms, Sensors, Alert, TopViolators
from django.http import JsonResponse

def base(request):
    return render(request, 'base.html')

def rooms(request):
    rooms = Rooms.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def api_room(request, id):
    room_sensors = Sensors.objects.get(room__number = id)
    data = {'Temperature': room_sensors.temperature,
            'Oxygen': room_sensors.oxygen,
            'Noise': room_sensors.noise,
            'Peoples': room_sensors.people}
    return JsonResponse(data)

def room(request, id):
    return render(request, 'room.html', {'id': id})

def top_violators(request):
    records = TopViolators.objects.order_by('-quantity')[:5]
    data = {i: {record.room.number: record.quantity} for i, record in enumerate(records)}
    return render(request, 'top_violators.html', {'records': data})

def api_violations(request):
    records = Alert.objects.order_by('-time')
    data = {record.room.number: record.message for record in records[:3]}
    if len(records)>=6:
        for record in records[3:6]:
            num = record.room.number
            if num not in data:
                data[num] = f'Комната {num}: к вам поднимается комендант. Вы не устарнили нарушние по датчику {record.sensor} со значением {record.value}'
                break
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


