from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    # pin=models.IntegerField()
    # type=models.BooleanField()

    def __str__(self):
        return self.name

class product(models.Model):
    productid = models.CharField(max_length=50, unique=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    img=models.ImageField()

    def __str__(self):
        return self.productid

class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    number = models.IntegerField()
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.Product_ID} - {self.customer.name} - {self.date}"


class cart(models.Model):
    customerid=models.IntegerField()
    number=models.IntegerField()
    def __str__(self):
        return self.customerid
    

class SellerInfo(models.Model):
    sellername = models.CharField(max_length=20)
    selleremail = models.EmailField(max_length=20)
    selleraddress = models.TextField(max_length=75)
    sellerphone = models.CharField(max_length=15) 
    
    
    