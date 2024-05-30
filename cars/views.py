from django.db.migrations import serializer
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import CarMark, Car
from .seriallizers import CarMarkSerializer, CarSerializer, CarSerializer2, CarMarkSerializer2

from rest_framework import permissions

class CarMarkListCreateView(APIView):
    """
    View for creating and listing CarMark objects
    - Method [GET, POST]
    """

    def get(self, request):
        car_marks = CarMark.objects.all()

        serializer = CarMarkSerializer(car_marks, many=True)

        response = {
            "Cars-Marks": serializer.data
        }
        return Response(response)

    def post(self, request):
        serializer = CarMarkSerializer(data=request.data)

        serializer.is_valid()
        serializer.save()

        response = {
            "Create": "Your mark added successfully!"
        }

        return Response(response)


class CarMarkUpdateDeleteView(APIView):
    """
    View for delete and update CarMark object with pk
    """

    def delete(self, request, pk):
        car_mark = CarMark.objects.get(ol=pk)

        car_mark.delete()

        response = {
            "Delete": f"{car_mark.name} deleted!"
        }

        return Response(response)

    def put(self, request, pk):
        try:
            car_mark = CarMark.objects.get(pk=pk)
        except Exception as e:
            return Response({"Error": str(e)})

        serializer = CarMarkSerializer(instanse=car_mark, data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"Update": serializer.data})


# -------------------------------------------------

class CarMarkListCreateView2(generics.ListCreateAPIView):
    """
    View for listing CarMark objects and for create them.
    - Methods [GET, POST]
    """
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializer


class CarMarkUpdateDelete2(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView,):
    queryset = CarMark.objects.all()
    serializer_class = CarMarkSerializer

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            car_mark = self.queryset.get(pk=pk)
        except Exception as e:
            return Response({"Error": str(e)})
        serializer = self.serializer_class(instance=car_mark, data=self.request.data)
        serializer.is_valid(raise_exception = True)


    def delete(self, request, *args,** kwargs):
        pk = kwargs.get('pk')
        try:
            CarMark.Obiects.get(pk=pk).delete()
        except Exception as e:
            return Response({"Error": str(e)})

        return Response({"DELETE": f"CarMark with id {pk} deleted!"})


class CarListView2(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer2


class CarCreateView2(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer2


class CarDetailView2(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer2


class CarDestroyView2(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer2



class CarUpdateView2(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer2


#---------------------------------------------
class CarMarkViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    Viewset for listing, creating, updating, deleting CarMark objects.
    -Methods [GET, POST, PUT, DELETE]
    """
    queryset = CarMark. objects. all()
    serializer_class = CarMarkSerializer2
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]



    def delete(self, request, *args,**kwargs):
        pk = kwargs.get('pk')
        try:
            CarMark.objects.get(pk=pk).delete()
        except Exception as e:
            return Response({"Error": str(e)})

        return Response({"DELETE":f"CarMark with id {pk} deleted!"})


class CarViewset(viewsets.ModelViewSet):

    """
    ViewSet for Car model (pk)
    - Methods [GET, POST, PUT, DELETE]
    """


    queryset = Car.objects.all()
    serializer_class = CarSerializer2






"""
BaseAuth -> Base username:password
Session
Token


JWTToken
"""
