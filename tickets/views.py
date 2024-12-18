from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,filters 
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
from rest_framework .authentication import BasicAuthentication,TokenAuthentication
from rest_framework .permissions import IsAuthenticated
from django.http import Http404
from .permissions import IsAuthorOrReadOnly
# fbv no model 1
    
def no_rest_no_model(request):
    guests=[{
        'id':1,
        "name":"mero",
        "mobile":101515,
    },
    {
        'id':2,
        "name":"ali",
        "mobile":202020,
    }
    ]
    return JsonResponse(guests,safe=False)

# fbv model 2

def no_rset_from_model(request):
    data=Guest.objects.all()
    response={'guest':list(data.values('name','mobile'))}
    return JsonResponse(response)

#  fbv list 3 

# post get
@api_view(['GET','POST'])
def fbv_list(request):
    if request.method == 'GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

# get put delete
@api_view(['GET','PUT','DELETE'])
def fbv_pk(request,pk):
    guest=Guest.objects.get(pk=pk)
    if request.method == 'GET':
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
            guest.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
#  4 cbv
class cbv_list(APIView):
    # def get_object(self,pk):
    def get(self,request):
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
class cbv_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoseNotExist:
            raise Http404
    def get(self,request,pk):
        guests=self.get_object(pk)
        serializer=GuestSerializer(guests)
        return Response(serializer.data)
    def put(self,request,pk):
        guests=self.get_object(pk)
        serializer=GuestSerializer(guests,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        guests=self.get_object(pk)
        guests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#  5 mixins

class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

#  6 generics 

class generics_list(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    

#  6 viewsets
 

class viewsets_guest(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class viewsets_reservation(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer



@api_view(['GET'])
def find_movie(request):
    movies=Movie.objects.filter(
        hall=request.data['hall'],
        movie=request.data['movie']

    )
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def new_reservation(request):
    movie=Movie.objects.get(
        hall=request.data['hall'],
        movie=request.data['movie']

    )
    guest=Guest()
    guest.name=request.data['name']
    guest.mobile=request.data['mobile']
    guest.save()
    reservation=Reservation()
    reservation.guest=guest
    reservation.movie=movie
    reservation.save()
    return Response(reservation.data,status=status.HTTP_201_CREATED)



class post_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    # authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthorOrReadOnly]
    authentication_classes=[TokenAuthentication]