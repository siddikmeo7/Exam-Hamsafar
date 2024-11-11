from django.urls import path
from .views import *

urlpatterns = [
    path('',TripsListView.as_view(),name='Base-Page'),
    path('addtrip',AddTrip.as_view(),name='Add-Trip'),
    path('detailtrip/<int:pk>',DetailTrip.as_view(),name='Detail-Trip'),
    path('edittrip/<int:pk>',EditTrip.as_view(),name='Edit-Trip'),
    path('deletetrip/<int:pk>',DeleteTrip.as_view(),name='Delete-Trip'),
    path('booktrip/<int:pk>/', BookTrip.as_view(), name='Book-Trip'),
    path('bookedtrips/', BookedTripsListView.as_view(), name='Booked-Trips'),
    path('logout',user_logout,name='logout'),
    
]

