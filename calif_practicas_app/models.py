from __future__ import unicode_literals

from django.db import models

# To make readable URLs, we need to include a slug field in the Category model. First we need to
# import the function slugify from Django that will replace whitespace with hyphens (for example,
# "how do i create a slug in django" turns into "how-do-i-create-a-slug-in-django").
from django.template.defaultfilters import slugify

# You should be aware that Django creates an ID field for you automatically in each table relating to a model.
# You therefore DO NOT need to explicitly define a primary key for each model.

def validar_rango_nota(value):
    if value < 0 or value > 10:
        raise ValidationError(
            _('%(value)s no es una nota valida (debe estar entre 0 y 10)'),
            params={'value': value},
        )

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Empresa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    empresa = models.ForeignKey(Empresa, related_name='calificaciones')
    usuario = models.CharField(max_length=50)
    opinion = models.TextField()
    nota = models.PositiveIntegerField(default=5)
    #nota = models.PositiveIntegerField(default=5, validators[validar_rango_nota])

    def __str__(self):
        return self.usuario + ' -> ' + str(self.empresa) + ' -> ' + str(self.nota)

    class Meta:
        verbose_name_plural = 'calificaciones'

# class Category(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)
#
#     class Meta:
#         verbose_name_plural = 'categories'
#
#     # This method is used to provide a unicode representation of a model instance.
#     # This will be incredibly handy to you when you begin to use the Django admin interface.
#     def __str__(self):
#         return self.name
#
#
# class Page(models.Model):
#     category = models.ForeignKey(Category)
#     title = models.CharField(max_length=128)
#     url = models.URLField()
#     views = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
