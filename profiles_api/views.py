from rest_framework.views import APIView
from rest_framework.response import Response



class HelloAPIView(APIView):
    """Test the APIView"""

    def get(self, request, format=None):
        """Testing the get function of an api view"""

        an_apiview = ['gg!', 'an apiview uses https methods as functions', 
                      'nd is mapped manually to URLs..'
                      ]
        
        return Response({'message': 'Hello Amiine!', 'an_apiView':an_apiview})