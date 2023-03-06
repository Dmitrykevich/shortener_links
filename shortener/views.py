from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404, redirect

from .forms import VisitorUrlForm
from .models import VisitorUrl


class IndexView(TemplateView):
    template_name = 'shortener/index.html'
    form_class = VisitorUrlForm
    success_url = reverse_lazy('shortener:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            unique_visitor = request.COOKIES['unique_visitor_id']
            visitor_url = form.save(commit=False)
            visitor_url.unique_visitor = unique_visitor
            visitor_url.save()
            return HttpResponseRedirect(self.success_url)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class LinksListView(ListView):
    template_name = 'shortener/links_list.html'
    model = VisitorUrl

    def get_queryset(self):
        unique_visitor = self.request.COOKIES.get('unique_visitor_id')
        queryset = super().get_queryset().filter(unique_visitor=unique_visitor)
        return queryset


def redirect_to_origin_url(request, url_hash):
    url = get_object_or_404(VisitorUrl, url_hash=url_hash)
    return redirect(url.origin_url)
