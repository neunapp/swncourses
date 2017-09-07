# -*- coding: utf-8 -*-

# django
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    View,
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#local
from .models import Blog, BlogCategory, Tag
#forms


#views
class BlogListView(ListView):
    """ modelo para lista de blogs """

    context_object_name = 'blogs'
    model = Blog
    template_name = 'blog/list.html'

    def get_queryset(self):
        #return queryset
        return Blog.objects.filter(
            published=True,
        )


class BlogDetailView(DetailView):
    """ modelo para ver un ariculo """
    
    model = Blog
    template_name = 'blog/detail.html'
