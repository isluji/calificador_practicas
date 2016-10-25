"Modulo para pruebas unitarias"

# Configuracion necesaria antes de importar los modelos
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calificador_practicas.settings")

import django
django.setup()

# -----------------------------------------------------

from django.test import TestCase
from calif_practicas_app.models import Empresa, Calificacion

# Create your tests here.
class EmpresaTestCase(TestCase):
    def setUp(self):
        """Crea un par de objetos para realizar el test con ellos"""
        Empresa.objects.create(nombre="Sun Microsystems", slug="sun-microsystems")
        Empresa.objects.create(nombre="Google", slug="google")

    def test_empresa_genera_slug(self):
        """Las empresas que pasan este test se crean y generan su nombre 'slug' correctamente"""
        sun = Empresa.objects.get(nombre="Sun Microsystems")
        google = Empresa.objects.get(nombre="Google")

        # Con esto, se genera la forma slug del nombre (todo en minuscula y separado por guiones,
        # de forma que sea apto para utilizarse en URLs) y se actualiza la base de datos.
        sun.save()
        google.save()

        self.assertEqual(sun.slug, "sun-microsystems")
        self.assertEqual(google.slug, "google")

class CalificacionTestCase(TestCase):
    sun = Empresa.objects.get_or_create(nombre="Sun Microsystems", slug="sun-microsystems")[0]
    google = Empresa.objects.get_or_create(nombre="Google", slug="google")[0]

    def setUp(self):
        """Crea algunas calificaciones para realizar el test con ellas
        (hemos creado las empresas previamente como variables de clase, pues actuan de clave externa)"""
        Calificacion.objects.create(empresa=self.sun, usuario="paco",
                                    opinion="He desarrollado aplicaciones web con Node.js", nota=7)
        Calificacion.objects.create(empresa=self.google, usuario="jose",
                                    opinion="No me ha gustado nada la forma de trabajar en esta empresa", nota=-2)
        Calificacion.objects.create(empresa=self.sun, usuario="jose",
                                    opinion="Increible, ojala todas las empresas fueran asi", nota=14)

    def test_calificacion_valida_nota(self):
        "Comprobamos que las notas sean truncadas al rango [0-10]"
        califCorrecta = Calificacion.objects.get(empresa=self.sun, usuario="paco")
        califMenor = Calificacion.objects.get(empresa=self.google, usuario="jose")
        califMayor = Calificacion.objects.get(empresa=self.sun, usuario="jose")

        self.assertEqual(califMenor.nota, 0)
        self.assertEqual(califCorrecta.nota, 7)
        self.assertEqual(califMayor.nota, 10)
