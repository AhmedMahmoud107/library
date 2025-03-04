from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    status_book = [
        ('avilable','avilable'),
        ('rented','rented'),
        ('sold','sold'),
    ]
    
    
    title = models.CharField(max_length = 250)
    author = models.CharField(max_length = 150)
    book_photo = models.ImageField(upload_to ='photos' , null = True , blank = True)
    author_photo = models.ImageField(upload_to ='photos' , null = True , blank = True)
    pages = models.IntegerField(null = True , blank = True)
    price = models.DecimalField(max_digits = 6 ,decimal_places = 2 , null = True , blank = True)
    rental_price = models.DecimalField(max_digits = 6 ,decimal_places = 2 , null = True , blank = True)
    rental_period = models.IntegerField(null = True , blank = True)
    total_rental = models.DecimalField(max_digits = 6 ,decimal_places = 2 , null = True , blank = True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50 , choices = status_book, null = True , blank = True)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, null = True , blank = True )
    
    
    def __str__(self):
        return self.title

    