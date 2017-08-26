#modelo matriculas

from .models import Registration

def create_matricula_free(curso, usuario):
    """ funcion que registra matriculas gratuitas """

    matricula = Registration(
        course=curso,
        user=usuario,
        amount=curso.price,
        activate=True,
        user_activate=usuario,
    )
    matricula.save()
    #
    print '*** matricula gratis guardada ***'
    return True


def create_update_registration(curso, usuario):
    """ funcion que registra o actualiza una matricula """

    obj, created = Registration.objects.update_or_create(
        course=curso,
        user=usuario,
        defaults={
            'amount': curso.price
        },
    )

    print '*** pre-incripcion registrada ***'
    return created
