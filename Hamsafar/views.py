from django.views import generic
from django.urls import reverse_lazy 
from django.shortcuts import redirect ,render
from .models import *

class TripsListView(generic.ListView):
    model = Trip
    fields = ["user","name","start_location","end_location","date_run","seats_available","description","price","is_active"]
    template_name = "base.html"

class AddTrip(generic.CreateView):
    model = Trip
    fields = "__all__"
    template_name = "trip_form.html"
    success_url = reverse_lazy('Base-Page')

class DetailTrip(generic.DetailView):
    model = Trip
    template_name = "detail-trip.html"  

class EditTrip(generic.UpdateView):
    model = Trip
    fields = "__all__"
    template_name = "trip_form.html"
    success_url = reverse_lazy('Base-Page')

class DeleteTrip(generic.DeleteView):
    model = Trip
    template_name = "confdeltrip.html"
    success_url = reverse_lazy('Base-Page')

class BookTrip(generic.CreateView):
    model = BookTrip
    fields = "__all__"
    template_name = "book_trip_form.html"
    success_url = reverse_lazy('Base-Page')

class BookedTripsListView(generic.ListView):
    model = BookTrip
    fields = ["__all__"]
    template_name = "bookedtrips_list.html"


def user_logout(request):
    return render(request,'registration/logout.html')