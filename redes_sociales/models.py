from django.db import models


class Redsocial(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre',
        help_text='Escríbelo tal cual el ícono de Font Awesome 4 (twitter, facebook, instagram, linkedin, youtube...). '
                  'El pie de página usa este nombre en minúsculas para mostrar el ícono.',
    )
    link = models.URLField(verbose_name='Enlace')

    class Meta:
        verbose_name = 'red social'
        verbose_name_plural = 'redes sociales'
        ordering = ['name']

    def __str__(self):
        return self.name
