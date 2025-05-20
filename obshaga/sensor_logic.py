import random

def gen_normal(param, normal_ranges):
        r = normal_ranges[param]
        return round(random.uniform(r[0], r[1]), 1)

def generate_intruder_sen(room, normal_ranges):
    intruder = {
        'temperature': [(10, 20), (33, 41)],
        'oxygen': [(14, 17), (25, 30)],
        'noise': [(70, 100)],
        'people_count': [(7, 15)]
    }

    sensor_names = {
        'temperature': 'Температура',
        'oxygen': 'Кислород',
        'noise': 'Шум',
        'people_count': 'Количество людей'
    }

    param = random.choice(list(intruder.keys()))
    violation_range = random.choice(intruder[param])
    value = round(random.uniform(violation_range[0], violation_range[1]), 1)

    from .models import Sensors, Alert, TopViolators
    sen = Sensors()
    sen.room = room
    sen.temperature = gen_normal('temperature', normal_ranges)
    sen.oxygen = gen_normal('oxygen', normal_ranges)
    sen.noise = gen_normal('noise', normal_ranges)
    sen.people = gen_normal('people_count', normal_ranges)

    if param == 'temperature':
        sen.temperature = value
    elif param == 'oxygen':
        sen.oxygen = value
    elif param == 'noise':
        sen.noise = value
    elif param == 'people_count':
        sen.people = int(value)

    sen.save()

    Alert.objects.create(
        room=room,
        sensor=sensor_names[param],
        value=value,
        message=f"Показатель '{sensor_names[param]}' в комнате {room.number} вне нормы: {value}."
    )

    obj = TopViolators.objects.get(room=room)
    obj.quantity+=1
    obj.save()


def generate_all_data():
    from .models import Rooms, Sensors
    Sensors.objects.all().delete()

    rooms = list(Rooms.objects.all())
    normal_ranges = {
        'temperature': (21, 32),
        'oxygen': (18, 24),
        'noise': (0, 69),
        'people_count': (0, 6)
    }
    intruder_rooms = random.sample(rooms, min(3, len(rooms)))

    for room in intruder_rooms:
        generate_intruder_sen(room, normal_ranges)

    for room in rooms:
        if room not in intruder_rooms:
            Sensors.objects.create(
                room=room,
                temperature=round(random.uniform(*normal_ranges['temperature']), 1),
                oxygen=round(random.uniform(*normal_ranges['oxygen']), 1),
                noise=round(random.uniform(*normal_ranges['noise']), 1),
                people=random.randint(*normal_ranges['people_count'])
            )

    
    

    

