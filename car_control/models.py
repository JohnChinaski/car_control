from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class OwnerRegister(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('nome completo'))
    doc_number = models.CharField(unique=True, max_length=150, verbose_name=_('numero do documento'))
    registration = models.CharField(max_length=50, verbose_name=_('matrícula'), null=True, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, db_column="user")
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['name']
        verbose_name = _('registro de proprietário')
        verbose_name_plural = _('registros de proprietários')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Cria a matrícula utilizando o id
        if not self.pk:
            person = super(OwnerRegister, self).save(*args, **kwargs)
            code = 'PROP{id}05d'.format(id=self.id)
            self.registration = code
            self.save()
        else:
            person = super(OwnerRegister, self).save(*args, **kwargs)
        return person


class VehicleBrand(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('marca / fabricante'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['name']
        verbose_name = _('marca / fabricante')
        verbose_name_plural = _('marcas / fabricantes')

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('tipo de vículo'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['name']
        verbose_name = _('tipo de veículo')
        verbose_name_plural = _('tipos de veículos')

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('modelo'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')

    class Meta:
        ordering = ['name']
        verbose_name = _('modelo do veículo')
        verbose_name_plural = _('modelos do veículos')

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    owner = models.ForeignKey(OwnerRegister, verbose_name=_('proprietário'), on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, db_column="user")
    slug = models.SlugField(max_length=150, verbose_name=_('slug'), default='')
    brand = models.ForeignKey(VehicleBrand, verbose_name=_('marca'), on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(VehicleModel, verbose_name=_('modelo'), on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(VehicleType, verbose_name=_('tipo'), on_delete=models.SET_NULL, null=True)
    model_year = models.CharField(max_length=4, verbose_name=_('ano do modelo'))
    fabric_year = models.CharField(max_length=4, verbose_name=_('ano de fabricação'))
    vehicle_plate = models.CharField(unique=True, max_length=7, verbose_name=_('placa do veículo'))
    vehicle_chassis = models.CharField(unique=True, max_length=17, verbose_name=_('chassis do veículo'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('data da criação do registro'))

    class Meta:
        ordering = ['user']
        verbose_name = _('cadastro de veículo')
        verbose_name_plural = _('cadastros de veículos')

    def __str__(self):
        return '{owner} - {model} - {plate}'.format(owner=self.owner.name, model=self.model, plate=self.vehicle_plate)
