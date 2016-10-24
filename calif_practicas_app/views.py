"Modulo de vistas"

from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

# Import the models that we want to use
from calif_practicas_app.models import Empresa
from calif_practicas_app.models import Calificacion

# Create your views below.

def index(request):
    """
    Indice de la aplicacion web

    Muestra el titulo y una imagen de presentacion, seguidos de
    una fila de botones con las distintas funcionalidades de la aplicacion.
    """
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    lista_empresas = Empresa.objects.order_by('-nombre')[:5]

    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    context_dict = {'empresas': lista_empresas}

    # Render the response and send it back!
    return render(request, 'calif_practicas_app/index.html', context_dict)
