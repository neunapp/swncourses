from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


#
class IsAutemticateMixin(object):
    """ mixin para direccionar a home a usuarios registardos """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(
                reverse(
                    'matriculas_app:matricula-dashboard'
                )
            )
        #
        return super(IsAutemticateMixin, self).dispatch(request, *args, **kwargs)
