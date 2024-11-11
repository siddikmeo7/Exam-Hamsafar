from django.db import models
from django.contrib.auth.models import User

# Table user is imported!

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    name = models.CharField(max_length=100,null=True)
    start_location = models.CharField(max_length=50)
    end_location = models.CharField(max_length=50)
    date_run = models.DateTimeField()  
    seats_available = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.start_location} to {self.end_location} by {self.user.username}"
    
class BookTrip(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__ (self):
        return f"{self.trip} {self.phone_number}"
    


