from django.db import models

# Create your models here.
class catagory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class product(models.Model):
    web_id = models.URLField()
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    catagory = models.ManyToManyField(catagory)

    def __str__(self):
        return self.name


class productinventory(models.Model):
    sku = models.PositiveIntegerField(default=0)
    upc = models.PositiveIntegerField(default=0)
    is_active  = models.BooleanField(default=False)
    retail_price = models.DecimalField( max_digits=5, decimal_places=2)
    store_price = models.DecimalField(decimal_places=2,max_digits=5)
    is_digital = models.BooleanField(default=False)
    weight = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(product,on_delete=models.CASCADE)




class media(models.Model):
    img_url = models.ImageField(upload_to="images/")
    alt_text = models.TextField()
    is_feature = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    productinventory = models.ForeignKey(productinventory,on_delete=models.CASCADE)

    


class stock(models.Model):
    last_checked = models.DateTimeField(auto_now_add=True)
    units = models.CharField(max_length=100)
    units_sold = models.BigIntegerField()
    productinventory = models.OneToOneField(productinventory,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.units



    

