from .models import Redsocial


def redes_sociales(request):
    """Deja las redes sociales disponibles en todas las plantillas (pie de página)."""
    return {'redes_sociales': Redsocial.objects.all()}
