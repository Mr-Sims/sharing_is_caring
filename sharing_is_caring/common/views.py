from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = 'common/index.html'


class AboutUsView(TemplateView):
    template_name = 'common/about-us.html'
