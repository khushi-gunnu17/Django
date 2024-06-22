from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class fruitVariety(models.Model) :

    FRUIT_VARIETY_CHOICE = [
        ('A', 'APPLE'),
        ('B', 'BANANA'),
        ('M', 'MANGO'),
        ('K', 'KIWI'),
        ('P', 'PAPAYA'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_app/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=1, choices=FRUIT_VARIETY_CHOICE)
    description = models.TextField(default='')       # compulsory field

    def __str__(self) :
        return self.name
    


# One to Many
class fruitReviews(models.Model) :
    fruit = models.ForeignKey(fruitVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return f'{self.user.username} review for {self.fruit.name}'
    


# Many to Many
class Store(models.Model) :
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    fruit_varities = models.ManyToManyField(fruitVariety, related_name='stores')

    def __str__(self) :
        return self.name
    


# One to one
class Certificate(models.Model) :
    fruit = models.OneToOneField(fruitVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self) :
        return f'Certificate for {self.fruit.name}'