from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
size_type = (('S', 'S'),
             ('M', "M"),
             ("L", "L"),
             ('XL', 'XL'),
             ('2XL', '2XL'))


def upload_img(instace,filename):
    imgname,ext=filename.split('.')

    return f"clothes/{instace.slug}.{ext}"

class clothe(models.Model):
    owner=models.ForeignKey(User, related_name='pro_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    price = models.FloatField(max_length=5)
    Brief_summary = models.CharField(max_length=200)
    size = models.CharField(max_length=3, choices=size_type)
    #color
    descripion=models.TextField(max_length=800)
    Weight=models.FloatField(max_length=4)
    Dimensions=models.CharField(max_length=18)
    Materials=models.FloatField(max_length=2)
    puplish_at=models.DateField(auto_now=True)
    category=models.ForeignKey('Category',on_delete= models.CASCADE)
    image=models.ImageField(upload_to=upload_img)
    image2=models.ImageField(upload_to=upload_img)
    image3=models.ImageField(upload_to=upload_img)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title) 
        super(clothe,self).save(*args,**kwargs)
    
    def __str__(self) :
        return self.title
        


class Category(models.Model):
        name=models.CharField(max_length=25)

        def __str__(self):
            return self.name


class review(models.Model):
    
    clothe_r=models.ForeignKey(clothe,related_name='add_review', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Your_review=models.TextField(max_length=700)
    creat_at=models.DateField(auto_now=True)
    def __str__(self) :
        return self.name