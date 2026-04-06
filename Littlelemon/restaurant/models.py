from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_slot = models.IntegerField(default=10)
    reservation_date = models.DateField()
    
    class Meta:
        unique_together = ('reservation_slot', 'reservation_date')
        
    def __str__(self):
        return f"{self.first_name} -  {self.reservation_date}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title