from django.db import models
import datetime
# Create your models here.

class customers (models.Model):
    cpno = models.IntegerField(null=False,primary_key=True)
    room = models.CharField(max_length=80,null=False)
    bldg = models.CharField(max_length=80,null=False)
    first_name = models.CharField(max_length=40,null=False)
    surname = models.CharField(max_length=40,null=False)
    m_initial = models.CharField(max_length=40,null = False)
    count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return unicode((self.cpno,self.surname,self.first_name))
    
class cuisine (models.Model):
    c_name = models.CharField(max_length=50,null=False)
    
    def __unicode__(self):
        return unicode((self.cat_name))
    
class category (models.Model):
    cat_name = models.CharField(max_length=50,null=False)
    
    def __unicode__(self):
        return unicode((self.cat_name))

class items (models.Model):
    sizeChoices = (
        ('R','regular'),
        ('L','large'),
    )
    
    item_no = models.AutoField(primary_key=True)
    iname = models.CharField(max_length=50)
    desc = models.TextField()
    size = models.CharField(max_length=1,choices=sizeChoices)
    price = models.IntegerField()
    isAvailable = models.BooleanField(default=True)
    cat_no = models.ForeignKey(category,null=False)
    c_no = models.ForeignKey(cuisine,null=False)
    
    def __unicode__ (self):
        return unicode((self.iname,self.price))
    
class orders (models.Model):
    order = models.ManyToManyField(items,through='includes')
    cpno = models.ForeignKey(customers,null=False)
    time = models.DateTimeField(default=datetime.datetime.now())
    isDone = models.BooleanField()
    
    def __unicode__(self):
        return unicode((self.cpno,self.time,self.isDone))

class includes (models.Model):
    order_no = models.ForeignKey(orders,null=False)
    item_no = models.ForeignKey(items,null=False)
    qty = models.IntegerField()
    
    def __unicode__(self):
        return unicode((self.order_no,self.item_no,self.qty))
