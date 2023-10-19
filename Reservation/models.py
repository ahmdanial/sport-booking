from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Student(models.Model):
    uid= models.CharField('ID',max_length=12, primary_key=True)
    name= models.TextField('Name', max_length=50, blank=True)
    email= models.EmailField('Email',max_length=50, blank=True)
    password= models.TextField('Password', max_length=25, default='NULL', blank=True)

    def __str__(self):
        return self.uid

class Item(models.Model):
    itemcode= models.CharField('Item Code', max_length=5, primary_key = True)
    itemname= models.TextField('Item Name', max_length=100)
    slug=models.SlugField(null=True)
    image=models.ImageField(upload_to='item_img/', null='NOT NULL')
    image2=models.ImageField(upload_to='item2_img/', null=True, blank=True)
    image3=models.ImageField(upload_to='item3_img/', null=True, blank=True)
    image4=models.ImageField(upload_to='item4_img/', null=True, blank=True)
    itemstatus= models.CharField(max_length=11, default='AVAILABLE')
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="60" height="60"/>')
    
    def __str__(self):
        return self.itemcode

class Booking(models.Model):
    uid=models.ForeignKey(Student, on_delete=models.CASCADE)
    itemcode=models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    startdate=models.DateField('Start Date', blank=True, null=True)
    enddate=models.DateField('End Date', blank=True, null=True)
    bookingstatus=models.BooleanField(default=True)
    quantity= models.IntegerField('Quantity', default=1)

    def get_item_info(self):
        if self.itemcode:
            return mark_safe(f'{self.itemcode.image_tag()}')
        else:
            return ''
