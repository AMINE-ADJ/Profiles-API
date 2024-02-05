from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

from rest_framework import viewsets

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API APIView"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """A function handler (get function) of an api view"""

        an_apiview = ['gg!', 'an apiview uses https methods as functions', 
                      'nd is mapped manually to URLs..'
                      ]
        
        return Response({'message': 'Hello Amiine!', 'an_apiView':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            nickname = serializer.validated_data.get('nickname')
            message = f'Hello {name}, {nickname}'

            return Response({'message' : message, 'status':status.HTTP_200_OK})
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})
    

    def patch(self, request, pk=None):
        """Handle a partial update of an object """

        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """Delete object from the DB"""

        return Response({'method': 'DELETE'})
    




class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message : but in reality it returns a list of objects that our ViewSet represents..So it's like the HTTP GET request"""
        a_viewset =[
            'Uses actions ( list, create, retrieve, update, partial_update )',
            'Automatically maps to URLs using Routers..', 
            'Provides more functionality with less code',
        ] 
        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message : POST a new item"""
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            # nickname = serializer.validated_data.get('nickname')
            message = f"Hello {name}, nice to meet you from ViewSet endpoint"
            return Response({'message':message, 'status':status.HTTP_200_OK})
        else : 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""

        return Response({'http_method': 'GET'})
    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )

