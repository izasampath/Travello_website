from django.shortcuts import render
from .models import Destination


# Create your views here.


def index(request):
    #
    # dest1 = Destination()
    # dest1.name = 'Vaddirala'
    # dest1.desc = 'No water'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 35
    # dest1.offer = True
    #
    # dest2 = Destination()
    # dest2.name = 'Jammalamadugu'
    # dest2.desc = 'One day Madugu'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 50
    # dest2.offer = False
    #
    # dest3 = Destination()
    # dest3.name = 'Dannawada'
    # dest3.desc = "One day wada"
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 10
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
