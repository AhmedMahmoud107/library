from django import forms
from .models import Book , Category

class CategoryForm(forms.ModelForm):
  class Meta:
      model = Category
      fields = ['name']
      widgets = {
          'name':forms.TextInput(attrs={'class':'form-control'}),
      }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_photo',
            'author_photo',
            'pages',
            'price',
            'rental_price',
            'rental_period',
            'total_rental',
            'status',
            'Category',
        ]
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'author': forms.TextInput(attrs={'class':'form-control'}),
        'book_photo': forms.FileInput(attrs={'class':'form-control'}),
        'author_photo': forms.FileInput(attrs={'class':'form-control'}),
        'pages': forms.NumberInput(attrs={'class':'form-control'}),
        'price': forms.NumberInput(attrs={'class':'form-control'}),
        'rental_price': forms.NumberInput(attrs={'class':'form-control', 'id':'rental_price'}),
        'rental_period': forms.NumberInput(attrs={'class':'form-control', 'id':'rental_period'}),
        'total_rental': forms.NumberInput(attrs={'class':'form-control', 'id':'total_rental'}),
        'status': forms.Select(attrs={'class':'form-control'}),
        'Category': forms.Select(attrs={'class':'form-control'}),
        }