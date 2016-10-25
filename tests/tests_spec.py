
# Configuracion necesaria antes de importar los modelos
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calificador_practicas.settings")

import django
django.setup()

# -----------------------------------------------------

from describe_it import describe, it, before_each, after_each, Fixture
from calif_practicas_app.models import Empresa, Calificacion

# This declares a test context.
@describe
def enterprise():
    f = Fixture()                                       # Fixture is a hack to get around
                                                        # Python's implementation of closures.
                                                        # You can use other methods, such as
                                                        # nonlocal if you like.

    @before_each                                        # Will be called before each 'it'
    def setup():
        # Crea un par de objetos para realizar el test con ellos
        Empresa.objects.create(nombre="Sun Microsystems", slug="sun-microsystems")
        Empresa.objects.create(nombre="Google", slug="google")

        # Nos aseguramos de que las empresas se han creado correctamente
        f.sun = Empresa.objects.get(nombre="Sun Microsystems")
        f.google = Empresa.objects.get(nombre="Google")

        # Con esto, se genera la forma slug del nombre (todo en minuscula y separado por guiones,
        # de forma que sea apto para utilizarse en URLs) y se actualiza la base de datos.
        f.sun.save()
        f.google.save()

    @after_each                                         # Will be called after each 'it'
    def teardown():
        f.sun.delete()
        f.google.delete()

    @it                                                 # This marks a test method.
    def enterprise_creates_slug():
        # describe_it doesn't come with an assertion lib. Pick any one you like.
        assert f.sun.slug == "sun-microsystems"
        assert f.google.slug == "google"

    ######### This is a nested context that augments the context above #########
    @describe
    def calification():

        # Before each 'it' method, any before_each in outer contexts will be called first.
        # Then this method will be called.
        @before_each
        def setup():
            # Crea algunas calificaciones para realizar el test con ellas
            # (ya contamos con las empresas puesto que las hemos creado en el contexto padre)
            Calificacion.objects.create(empresa=f.sun, usuario="paco",
                                        opinion="He desarrollado aplicaciones web con Node.js")
            Calificacion.objects.create(empresa=f.google, usuario="jose",
                                        opinion="No me ha gustado nada la forma de trabajar en esta empresa")
            Calificacion.objects.create(empresa=f.sun, usuario="jose",
                                        opinion="Increible, ojala todas las empresas fueran asi")

            # Nos aseguramos de que las calificaciones se han creado correctamente,
            # y le asignamos a cada una uno de los posibles casos, y llamamos a save(),
            # que trunca la nota dentro del rango valido y actualiza la base de datos
            f.califCorrecta = Calificacion.objects.get(empresa=f.sun, usuario="paco")
            f.califCorrecta.nota = 7
            f.califCorrecta.save()

            f.califMenor = Calificacion.objects.get(empresa=f.google, usuario="jose")
            f.califMenor.nota = -2
            f.califMenor.save()

            f.califMayor = Calificacion.objects.get(empresa=f.sun, usuario="jose")
            f.califMayor.nota = 14
            f.califMayor.save()

        @after_each                                         # Will be called after each 'it'
        def teardown():
            f.califCorrecta.delete()
            f.califMenor.delete()
            f.califMayor.delete()

        @it
        def grade_is_inside_valid_range():
            assert f.califCorrecta.nota == 7
            assert f.califMenor.nota == 0
            assert f.califMayor.nota == 10
