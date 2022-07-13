from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin

from .filters import AdFilter
from .forms import AdForm, EchoForm
from .models import Ad, Echo

from django.contrib import messages


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
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class OneAd(CustomSuccessMessageMixin, DetailView, FormMixin):
    model = Ad
    template_name = 'one_ad.html'
    context_object_name = 'one'
    queryset = Ad.objects.all()
    form_class = EchoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("one", kwargs={"pk": self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.echo_ad = self.get_object()
        self.object.echo_author = self.request.user
        self.object.save()
        return super().form_valid(form)


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

def imagePage(request):
    data = Ad.objects.all()
    return render(request, 'image.html', {'data': data})


@login_required
def create(request):

    context = {
        'priv': Ad.objects.filter(author=request.user)
    }
    return render(request, 'private.html', context)