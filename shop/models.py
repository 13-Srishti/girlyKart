from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id= models.AutoField
    prod_name= models.CharField(max_length= 50)
    category= models.CharField(max_length= 60, default='')
    sub_category= models.CharField(max_length= 60, default= '')
    price= models.IntegerField(default=0)
    desc= models.CharField(max_length= 350)
    pub_date= models.DateField()
    image= models.ImageField(upload_to='shop/images', default= '')

    def __str__(self):
        return self.prod_name

class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length= 50)
    email= models.CharField(max_length= 30, default='')
    subject= models.CharField(max_length= 90, default= '')
    message= models.CharField(max_length= 260,default=0)
    
    def __str__(self):
        return self.name

