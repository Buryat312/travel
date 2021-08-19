from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Travel
from .serializers import TravelSerializer
from rest_framework import views, generics
# Create your views here.

class TravelListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class TravelCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def perform_create(self, serializer):
        '''
        Функция для сохранения нынешнего пользователя владельцем созданной им задачи
        '''
        return serializer.save(owner=self.request.user)

class TravelDetailGenericView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    lookup_field = 'id'

class TravelUpdateGenericView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    lookup_field = 'id'

class TravelDestroyGenericView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Travel.objects.all()
    lookup_field = 'id'

# from rest_framework import serializers
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Travel
# from .serializers import TravelSerializer

# class TravelAPIView(APIView):
    

 

#     def get(self, request):
#         travels = Travel.objects.all()
#         serializer = TravelSerializer(travels, many=True)

#         return Response(serializer.data)

