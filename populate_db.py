"Script para rellenar la base de datos con datos de prueba"

# If you don't import the project's settings, you'll get an exception when attempting to
# import your models. This is because the necessary Django infrastructure has not yet
# been initialised. This is why we import the models AFTER the settings have been loaded.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calificador_practicas.settings')

import django
django.setup()

# -------------------------------------------------------------

from calif_practicas_app.models import Empresa, Calificacion

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    unit4_califs = [
        {"usuario":"isma94",
        "opinion":"He aprendido mucho en esta empresa.",
        "nota":8},
        {"usuario":"pepe",
        "opinion":"No me ha gustado nada.",
        "nota":3}
    ]

    google_califs = [
        {"usuario":"isma94",
        "opinion":"He aprendido muchisimo durante este tiempo.",
        "nota":9},
        {"usuario":"paco",
        "opinion":"No es para tanto.",
        "nota":6},
        {"usuario":"rafa",
        "opinion":"Ha sido un trabajo muy interesante.",
        "nota":8}
        ]

    empresas = {"Unit4": {"califs": unit4_califs},
                "Google": {"califs": google_califs} }

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for emp, emp_data in empresas.items():
        empresa = add_empresa(emp)

        for calif in emp_data["califs"]:
            add_calif(empresa, calif["usuario"], calif["opinion"], calif["nota"])

    # Print out the categories we have added.
    for emp in Empresa.objects.all():
        for cal in Calificacion.objects.filter(empresa=emp):
                print("- {0} - {1}".format(str(emp), str(cal)))

def add_calif(emp, user, opinion, nota=5):
    calif = Calificacion.objects.get_or_create(empresa=emp, usuario=user)[0]

    calif.opinion = opinion
    calif.nota = nota

    calif.save()
    return calif

def add_empresa(nombre):
    empresa = Empresa.objects.get_or_create(nombre=nombre)[0]

    empresa.save()
    return empresa

# Start execution here!
if __name__ == '__main__':
    print("Starting calif_practicas_app population script...")
    populate()
