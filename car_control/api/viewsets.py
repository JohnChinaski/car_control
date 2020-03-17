from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import OwnerRegister, VehicleBrand, VehicleModel, Vehicle, VehicleType
from django.contrib.auth.models import User

from .serializers import OwnerRegisterSerializer, \
    VehicleBrandSerializer, \
    VehicleModelSerializer, \
    VehicleSerializer


# PROPRIETÁRIO
class OwnerViewSet(ModelViewSet):
    queryset = OwnerRegister.objects.all()
    serializer_class = OwnerRegisterSerializer


class OwnerDocViewSet(ModelViewSet):
    serializer_class = OwnerRegisterSerializer
    lookup_field = 'doc'

    def get_queryset(self):
        return OwnerRegister.objects.filter(doc_number=self.kwargs['doc'])


class OwnerMatViewSet(ModelViewSet):
    serializer_class = OwnerRegisterSerializer
    lookup_field = 'mat'

    def get_queryset(self):
        return OwnerRegister.objects.filter(registration=self.kwargs['mat'])


class OwnerCreateViewSet(ModelViewSet):
    queryset = OwnerRegister.objects.all()
    serializer_class = OwnerRegisterSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        super(OwnerCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


# VEÍCULOS
class VehicleBrandViewSet(ModelViewSet):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer


class VehicleModelViewSet(ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer


class VehicleTypeViewSet(ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleModelSerializer


class VehicleListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        user = self.request.user
        vehicle = Vehicle.objects.filter(user=user.id)
        if vehicle:
            return vehicle
        else:
            return Response({'erro: Nenhum veículo encontrado para este usuário'})


class VehiclePlateListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    lookup_field = 'placa'

    def get_queryset(self):
        user = self.request.user
        person = OwnerRegister.objects.filter(user=user).first()
        if person:
            vehicle = Vehicle.objects.filter(vehicle_plate=self.kwargs['placa'], user=user)
            if vehicle:
                return vehicle


class VehicleChassisListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    lookup_field = 'chass'

    def get_queryset(self):
        user = self.request.user
        person = OwnerRegister.objects.filter(user=user).first()
        if person:
            vehicle = Vehicle.objects.filter(vehicle_chassis=self.kwargs['chass'], user=user)
            if vehicle:
                return vehicle


class VehicleDocListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    lookup_field = 'doc'

    def get_queryset(self):
        user = self.request.user
        person = OwnerRegister.objects.filter(user=user).first()
        if person:
            vehicle = Vehicle.objects.filter(owner__doc_number=self.kwargs['doc'], user=user)
            if vehicle:
                return vehicle


class VehicleCreateViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        car_type = VehicleType.objects.filter(slug=request.data.get('type')).first()
        brand = VehicleBrand.objects.filter(slug=request.data.get('brand')).first()
        model = VehicleModel.objects.filter(slug=request.data.get('model')).first()
        owner = OwnerRegister.objects.filter(name=request.data.get('owner')).first()
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        request.data.update({'type': car_type.id})
        request.data.update({'brand': brand.id})
        request.data.update({'model': model.id})
        request.data.update({'owner': owner.id})

        super(VehicleCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
