from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Actuantes,
    Empresa,
    GastoEmpresa,
    GastoPersonal,
    Instrumental,
    Instrumento,
    Movilidad,
    Profesional,
    TipoGasto,
    Trabajo,
    Vehiculo,
)

admin.site.register(TipoGasto)


class ProfesionalInline(admin.StackedInline):
    model = Profesional
    extra = 0


class VehiculoInline(admin.StackedInline):
    model = Vehiculo
    extra = 0


class InstrumentoInline(admin.TabularInline):
    model = Instrumento
    extra = 0


class GastoEmpresaInline(admin.TabularInline):
    model = GastoEmpresa
    extra = 0


class GastoPersonalInline(admin.TabularInline):
    model = GastoPersonal
    extra = 0


class ActuantesInline(admin.TabularInline):
    model = Actuantes
    extra = 0
    verbose_name_plural = "actuantes"


class MovilidadInline(admin.TabularInline):
    model = Movilidad
    extra = 0
    verbose_name_plural = "movilidad"


class InstrumentalInline(admin.TabularInline):
    model = Instrumental
    extra = 0
    verbose_name_plural = "instrumental"


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "cantidad_de_profesionales",
        "cantidad_de_vehiculos",
        "cantidad_de_instrumentos",
        "gastos_por_hora",
    ]
    list_filter = ["nombre"]
    search_fields = ["nombre"]
    fieldsets = [
        (
            "",
            {
                "fields": [
                    ("nombre"),
                    ("horas_semanales", "gastos_por_hora"),
                    ("cantidad_de_profesionales",),
                    ("cantidad_de_vehiculos",),
                    ("cantidad_de_instrumentos",),
                ],
                "classes": ["extrapretty"],
            },
        )
    ]
    readonly_fields = [
        "gastos_por_hora",
        "cantidad_de_profesionales",
        "cantidad_de_vehiculos",
        "cantidad_de_instrumentos",
    ]
    inlines = [ProfesionalInline, VehiculoInline, InstrumentoInline, GastoEmpresaInline]


@admin.register(Profesional)
class ProfesionalAdmin(UserAdmin):
    list_display = ("username", "__str__", "costo_por_hora", "empresa", "last_login")
    list_filter = UserAdmin.list_filter + ("empresa",)
    search_fields = UserAdmin.search_fields + ("matricula", "cuit")
    custom_fields = (("CoPA", {"fields": ("empresa", "matricula", "cuit", "costo_por_hora")}),)
    fieldsets = UserAdmin.fieldsets + custom_fields
    add_fieldsets = UserAdmin.add_fieldsets + custom_fields
    readonly_fields = ["costo_por_hora"]
    inlines = [GastoPersonalInline]


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "valor", "kilometraje_anual", "tipo_combustible", "rendimiento", "costo_km", "empresa"]
    list_filter = ["tipo_combustible", "empresa"]
    search_fields = ["nombre"]
    readonly_fields = [
        "combustible",
        "valor_residual",
        "amortizacion_valor",
        "kilometraje_mensual",
        "amortizacion_seguro",
        "amortizacion_patente",
        "amortizacion_cochera",
        "amortizacion_lavado",
        "amortizacion_neumaticos",
        "reparaciones",
        "repuestos",
        "service",
        "lubricacion",
        "costo_km",
    ]


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "valor_USD", "valor_ARS", "vida_util", "costo_jornada", "empresa"]
    list_filter = ["empresa"]
    search_fields = ["nombre"]
    readonly_fields = [
        "valor_ARS",
        "costo_jornada",
    ]


@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = [
        "expediente",
        "empresa",
        "fecha",
        "comitente",
        "cantidad_de_profesionales",
        "cantidad_de_vehiculos",
        "cantidad_de_instrumentos",
        "costo_total",
    ]
    list_filter = ["profesionales__empresa__nombre"]
    search_fields = [
        "expediente",
        "comitente",
        "profesionales__matricula",
        "profesionales__first_name",
        "profesionales__last_name",
        "profesionales__empresa__nombre",
    ]
    date_hierarchy = "fecha"
    inlines = [ActuantesInline, MovilidadInline, InstrumentalInline]
    readonly_fields = [
        "sellado_fiscal",
        "informe_catastral",
        "empresa",
        "cantidad_de_profesionales",
        "cantidad_de_vehiculos",
        "cantidad_de_instrumentos",
        "horas_total",
        "gastos_de_empresa",
        "costo_actuantes",
        "costo_movilidad",
        "costo_instrumental",
        "aportes",
        "gastos_especificos",
        "costo_total",
    ]
