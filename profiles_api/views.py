from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloAPIView(APIView):
    """Test the APIView"""
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