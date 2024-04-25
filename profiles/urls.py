from django.urls import path


from django.urls import path
from .views import profile_detail,profile_list

urlpatterns = [
    path('list/profile/', profile_list.as_view()),
    path('list/profile/<int:pk>/', profile_detail.as_view()),
]


