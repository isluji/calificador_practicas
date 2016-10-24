"Definicion de los modelos para la base de datos"

from __future__ import unicode_literals

from django.db import models

# To make readable URLs, we need to include a slug field in the Enterprise model. First we need to
# import the function slugify from Django that will replace whitespace with hyphens (for example,
# "how do i create a slug in django" turns into "how-do-i-create-a-slug-in-django").
from django.template.defaultfilters import slugify

# You should be aware that Django creates an ID field for you automatically in each table relating to a model.
# You therefore DO NOT need to explicitly define a primary key for each model.


########################## MODELS ##########################

class Empresa(models.Model):
    """
    Empresa que tiene convenio con la facultad o universidad
    en cuestion y algun estudiante de los que han realizado
    sus practicas en ella la ha valorado.
    """

    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Empresa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    """
    Calificacion dada por un estudiante universitario a la
    empresa en la que ha realizado las practicas. Consta de una opinion
    y de una nota entre 0 y 10.
    """

    empresa = models.ForeignKey(Empresa, related_name='calificaciones')
    usuario = models.CharField(max_length=50)
    opinion = models.TextField()
    nota = models.PositiveSmallIntegerField(default=5)

    def save(self, *args, **kwargs):
        if self.nota < 0:
            self.nota = 0
        elif self.nota > 10:
            self.nota = 10

        super(Calificacion, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario + ' -> ' + str(self.empresa) + ' -> ' + str(self.nota)

    class Meta:
        verbose_name_plural = 'calificaciones'
