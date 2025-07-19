from django.db import models

# Create your models here.

class category(models.Model):
    categoryId=models.IntegerField(primary_key=True, unique=True)
    categoryName=models.CharField(max_length=25)
    
    def __str__(self):
        return self.categoryName

class size(models.Model):
    sizeId=models.IntegerField(primary_key=True, unique=True)
    sizeName=models.CharField(max_length=30)

    def __str__(self):
        return self.sizeName
    
class color(models.Model):
    colorName=models.CharField(max_length=25)
    hexValue=models.CharField(max_length=7)

    def __str__(self):
        return self.colorName
    
class image(models.Model):
    product=models.ForeignKey('product', on_delete=models.CASCADE, related_name='images')
    productImage=models.ImageField(upload_to='shopDetails')
    productColor=models.ForeignKey(color,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product.productName} in {self.productColor.colorName}"

class product(models.Model):
    productCategory=models.ManyToManyField(category, related_name='productCategory')
    productId=models.IntegerField(primary_key=True, unique=True)
    productName=models.CharField(max_length=50)
    discountPrice=models.FloatField()
    productPrice=models.FloatField()
    productSize=models.ManyToManyField(size,related_name='productSize')
    productColor=models.ManyToManyField(color,related_name='productColor')
    productImg=models.ImageField(upload_to='shopDtails')
    productDetail=models.TextField()
    productDesc=models.TextField()
    productInfo=models.TextField()
    productMaterial=models.TextField()
    
    
    def __str__(self):
        return self.productName