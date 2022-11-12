from django.urls import path
from .views import Userview, userdetailsview

urlpatterns = [

    path('users/', Userview.as_view()),
    path('userDetails/<int:pk>', userdetailsview.as_view()),
]