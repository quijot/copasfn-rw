from django.contrib.auth import mixins  # LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic  # ListView

from . import forms, models


class CounterMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_queryset().count()
        return context


class EmpresaFilterMixin:
    def get_queryset(self):
        """
        Returns only objects related to the User's Empresa.
        """
        if self.request.user.empresa:
            if self.model == models.Empresa:
                qs = self.model.objects.filter(id=self.request.user.empresa.pk)
            else:
                qs = self.model.objects.filter(empresa=self.request.user.empresa)
        else:
            qs = self.model.objects.none()
        return qs


class EmpresaInitialMixin:
    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        initial["empresa"] = self.request.user.empresa
        return initial


class ChildrenContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context[self.children] = self.fs(self.request.POST, instance=self.object)
        else:
            context[self.children] = self.fs(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context[self.children]
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return render(self.request, context["view"].get_template_names(), context)
        return super().form_valid(form)


class EmpresaDetailView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Empresa
    form_class = forms.EmpresaForm


class EmpresaCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Empresa
    form_class = forms.EmpresaForm

    def form_valid(self, form):
        """Assign Empresa to the User who has created it."""
        instance = form.save()
        self.request.user.empresa = instance
        self.request.user.save()
        return super().form_valid(form)


class EmpresaUpdateView(EmpresaFilterMixin, ChildrenContextMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Empresa
    form_class = forms.EmpresaForm
    # ChildrenContextMixin params
    children = "gastos"
    fs = forms.GastosEmpresaInlineFormSet


class ProfesionalListView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.ListView):
    model = models.Profesional


class ProfesionalDetailView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Profesional
    form_class = forms.ProfesionalForm


class ProfesionalCreateView(EmpresaInitialMixin, mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Profesional
    form_class = forms.ProfesionalForm


class ProfesionalUpdateView(EmpresaFilterMixin, ChildrenContextMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Profesional
    form_class = forms.ProfesionalForm
    # ChildrenContextMixin params
    children = "gastos"
    fs = forms.GastosPersonalesInlineFormSet


class InstrumentoListView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.ListView):
    model = models.Instrumento


class InstrumentoDetailView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Instrumento
    form_class = forms.InstrumentoForm


class InstrumentoCreateView(EmpresaInitialMixin, mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Instrumento
    form_class = forms.InstrumentoForm


class InstrumentoUpdateView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Instrumento
    form_class = forms.InstrumentoForm


class InstrumentoDeleteView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Instrumento
    success_url = reverse_lazy("instrumento_list")


class VehiculoListView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.ListView):
    model = models.Vehiculo


class VehiculoDetailView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = models.Vehiculo
    form_class = forms.VehiculoForm


class VehiculoCreateView(EmpresaInitialMixin, mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Vehiculo
    form_class = forms.VehiculoForm


class VehiculoUpdateView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Vehiculo
    form_class = forms.VehiculoForm


class VehiculoDeleteView(EmpresaFilterMixin, mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Vehiculo
    success_url = reverse_lazy("vehiculo_list")
