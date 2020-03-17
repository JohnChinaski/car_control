from django.contrib import admin

from .models import VehicleType, Vehicle, VehicleModel, VehicleBrand, OwnerRegister


class UserRegisterBrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'doc_number']


class VehicleBrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class VehicleModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class VehicleTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class VehicleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('vehicle_plate',)}
    list_display = ['user', 'vehicle_plate', 'date_created']


admin.site.register(OwnerRegister, UserRegisterBrandAdmin)
admin.site.register(VehicleBrand, VehicleBrandAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(Vehicle, VehicleAdmin)
