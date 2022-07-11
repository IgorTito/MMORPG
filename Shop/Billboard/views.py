from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from .filters import AdFilter
from .forms import AdForm, EchoForm
from .models import Ad, Echo


class AdList(ListView):
    model = Ad
    ordering = '-date_of_create'
    template_name = 'private.html'
    context_object_name = 'private'


class AdView(ListView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    queryset = Ad.objects.all()
    paginate_by = 5

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = AdFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context


class OneAd(DetailView):
    model = Ad
    template_name = 'one_ad.html'
    context_object_name = 'one'
    queryset = Ad.objects.all()


class CreateAd(PermissionRequiredMixin, CreateView):

    form_class = AdForm
    model = Ad
    template_name = 'ad_create.html'
    permission_required = ('Billboard.add_ad')

    def form_valid(self, form):
        author = form.save(commit=False)
        author.author = self.request.user
        return super().form_valid(form)


class DeleteAd(PermissionRequiredMixin, DeleteView):
    model = Ad
    template_name = "ad_delete.html"
    success_url = reverse_lazy('private')
    permission_required = ("Billboard.delete_ad")


class UpdateAd(PermissionRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = "ad_update.html"
    permission_required = ("Billboard.change_ad")


class EchoList(ListView):
    model = Echo
    template_name = 'echo.html'
    context_object_name = 'echo'
    queryset = Echo.objects.all()

    def get_queryset(self):
        return Echo.objects.filter(echo_ad_id=self.kwargs.get('pk'))


class CreateEcho(PermissionRequiredMixin, CreateView):

    form_class = EchoForm
    model = Echo
    template_name = 'echo_create.html'
    permission_required = ('Billboard.add_echo')

    def form_valid(self, form):
        author = form.save(commit=False)
        author.echo_author = self.request.user
        author.echo_ad = Ad.objects.get(author=self.request.user.id)
        return super().form_valid(form)


class AllComments(DetailView):
    model = Echo
    template_name = 'echo.html'
    context_object_name = 'echo'
    queryset = Echo.objects.all()


def imagePage(request):

    data = Ad.objects.all()
    return render(request, 'image.html', {'data': data})


def create(request):

    context = {
        'priv': Ad.objects.filter(author=request.user)
    }
    return render(request, 'private.html', context)
