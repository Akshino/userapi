from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import generics



class profile_list(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        return queryset
    
class profile_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()