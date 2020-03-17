"""vehicles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .api.viewsets import OwnerViewSet, \
    OwnerCreateViewSet, \
    OwnerDocViewSet, \
    OwnerMatViewSet, \
    VehicleBrandViewSet, \
    VehicleModelViewSet, \
    VehicleTypeViewSet, \
    VehicleListViewSet, \
    VehiclePlateListViewSet, \
    VehicleChassisListViewSet, \
    VehicleDocListViewSet, \
    VehicleCreateViewSet

urlpatterns = [
    # Autenticação
    url(r'^auth/', obtain_jwt_token),

    # Gestão de proprietarios
    url(r'^proprietario/', OwnerViewSet.as_view({'get': 'list'})),
    url(r'^criar/proprietario/', OwnerCreateViewSet.as_view({'post': 'create'})),
    url(r'^doc/proprietario/(?P<doc>\w+)$', OwnerDocViewSet.as_view({'get': 'list'})),
    url(r'^mat/proprietario/(?P<mat>\w+)$', OwnerMatViewSet.as_view({'get': 'list'})),

    # Lista modelos cadastrados
    url(r'^modelos/', VehicleModelViewSet.as_view({'get': 'list'})),
    # Lista marcas cadastradas
    url(r'^marcas/', VehicleBrandViewSet.as_view({'get': 'list'})),
    # Lista tipos de veículos cadastrados
    url(r'^tipos/', VehicleTypeViewSet.as_view({'get': 'list'})),

    # Gestão de veículos
    url(r'^veiculos/', VehicleListViewSet.as_view({'get': 'list'})),
    url(r'^placa/veiculos/(?P<placa>\w+)$', VehiclePlateListViewSet.as_view({'get': 'list'})),
    url(r'^chass/veiculos/(?P<chass>\w+)$', VehicleChassisListViewSet.as_view({'get': 'list'})),
    url(r'^doc/veiculos/(?P<doc>\w+)$', VehicleDocListViewSet.as_view({'get': 'list'})),
    url(r'^criar/veiculos/', VehicleCreateViewSet.as_view({'post': 'create'}))
]
