from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

# Import the models that we want to use
from calif_practicas_app.models import Empresa
from calif_practicas_app.models import Calificacion

# Create your views below.

def index(request):
    # --------------- EXAMPLE 1 -----------------

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    #context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    #return render_to_response('calif_practicas_app/index.html', context_dict, context)

    # --------------- EXAMPLE 2 -----------------

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    lista_empresas = Empresa.objects.order_by('-nombre')[:5]

    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    context_dict = {'empresas': lista_empresas}

    # Render the response and send it back!
    return render(request, 'calif_practicas_app/index.html', context_dict)
