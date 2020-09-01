from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api.serializers import HelloSerializer


class HelloApiView(APIView):

    serializer_class=HelloSerializer

    def get(self,request,format=None):

        an_api_view= [
            'uses http methods as funtion(get,post,delete,patch,put)',
            'similar to a traditional django view',
            'gives you the most control over your logic',
            'is mapped manually to urls'
        ]

        return Response({'message': 'hello', 'an_api_view':an_api_view})

    def post(self,request):
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message='hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):

        return Response({'method':'put'})

    def patch(self,request,pk=None):
        return Response({'method':'patch'})

    def delete(self,request,pk=None):

        return Response({'method':'delete'})
