from django.shortcuts import render
from rest_framework.views import *
from .serializers import *
# Create your views here.
class DepastmentView(APIView):
    serializer_class = DepastmentSerilaizer
   
    def get(self, request, format=None):
        
        follower_info = Depastment.objects.all()
        serializer = DepastmentSerilaizer(follower_info, many=True)
        return Response({"success": True, "message": " User following Detail", "data": serializer.data, "status": 200,
                         'data_count': len(serializer.data)}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):

        serializer = DepastmentSerilaizer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()

            return Response({"success": True, "message": "Friend Request Sent!","status":201 ,"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": True, "message": "Friend Request  Was Alraedy Sent!","status": 400, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

