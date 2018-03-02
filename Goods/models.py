from django.db import models

# Create your models here.
class Shopping(models.Model):
    user_id = models.IntegerField()
    commodity_id = models.IntegerField()
    size = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField()
    
    class Meta: 
        ordering = ['-id']

class Order(models.Model):
    user_id = models.IntegerField()
    batch = models.IntegerField(null=True)
    total_price = models.FloatField()
    receiver_name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    date = models.DateField()
    state = models.CharField(max_length=10)

    class Meta: 
        ordering = ['-id']

class OrderDetail(models.Model):
    order_id = models.IntegerField()
    commodity_id = models.IntegerField()
    commodity_name = models.CharField(max_length=500)
    pic_url = models.CharField(max_length=500)
    receiver_name = models.CharField(max_length=20)
    color = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    buying_price = models.FloatField()
    quantity = models.IntegerField()
