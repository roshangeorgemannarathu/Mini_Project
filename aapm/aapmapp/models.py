from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class dealer(AbstractUser):
    email = models.EmailField(unique=True)
    fullname = models.TextField(max_length=100, default="")
    role = models.TextField(max_length=100, default="")
    
    def __str___(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.ForeignKey("Dealer", on_delete=models.CASCADE)  # Assuming you have a ForeignKey relationship with the Dealer model
    fullname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    phone = models.CharField(max_length=10)
    housename = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    district = models.CharField(max_length=50, choices=[  # Add choices for the available districts
        ("Thiruvananthapuram", "Thiruvananthapuram"),
        ("Kollam", "Kollam"),
        ("Pathanamthitta", "Pathanamthitta"),
        ("Alappuzha", "Alappuzha"),
        ("Kottayam", "Kottayam"),
        ("Idukki", "Idukki"),
        ("Ernakulam", "Ernakulam"),
        ("Thrissur", "Thrissur"),
        ("Palakkad", "Palakkad"),
        ("Malappuram", "Malappuram"),
        ("Kozhikode", "Kozhikode"),
        ("Wayanad", "Wayanad"),
        ("Kannur", "Kannur"),
        ("Kasaragod", "Kasaragod"),
        
        # Add other districts here
         
    ])
    photoid = models.FileField(upload_to='photoids/')  # Make sure to configure your media settings for file uploads
    photo = models.ImageField(upload_to='photos/')  # Make sure to configure your media settings for image uploads

    def __str__(self):
        return self.fullname

class Aquarium(models.Model):
    dealer = models.ForeignKey(dealer, on_delete=models.CASCADE)  # Add this line to create the foreign key relationship
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='aquarium_images/')

    def __str__(self):
        return self.name

class Pet(models.Model):
    dealer = models.ForeignKey(dealer, on_delete=models.CASCADE)  # Add this line to create the foreign key relationship
    CATEGORY_CHOICES = [
        ('dog', 'Dogs'),
        ('cat', 'Cats'),
        ('fish', 'Fish'),
        ('bird', 'Birds'),
    ]




    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_images/')

    def __str__(self):
        return f"{self.get_category_display()} - {self.id}"

