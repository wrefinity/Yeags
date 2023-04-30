import json
from typing import Any, Dict
from .models import World
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, View, ListView, RedirectView, UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



class WorldDetailView(LoginRequiredMixin, DetailView):
    model = World


world_detail_view = WorldDetailView.as_view()


class WorldListView(ListView):
    model = World
    template_name = "pages/Worlds/lists.html"
    context_object_name = 'worlds'
    paginate_by = 10
    
    def get_context_data(self, **kwargs: Any):
        context = super(WorldListView, self).get_context_data(**kwargs)
        worlds = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(worlds, self.paginate_by)
        try:
            worlds = paginator.page(page)
        except EmptyPage:
            worlds = paginator.page(paginator.num_pages)
        context['worlds'] = worlds
        return  context
    
    

world_list_view = WorldListView.as_view()

''' get some list of worlds to feature'''
class WorldFeatured(ListView):
    model = World
    context_object_name = 'worlds'
    template_name = "pages/Worlds/featured.html"
    queryset = World.objects.all()[0:5]

world_featured = WorldFeatured.as_view()


class WorldCloneView(View):

    def get(self, request,  *args, **kwargs):
        pass
    def post(self, request,  *args, **kwargs):
        pass

world_clone_view = WorldCloneView.as_view()