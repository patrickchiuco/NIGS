from django.db import models
import datetime
# Create your models here.

class customers (models.Model):
    cpno = models.IntegerField(null=False,primary_key=true)
    room = models.CharField(max_length=80,null=False)
    bldg = models.CharField(max_length=80,null=False)
    first_name = models.CharField(max_length=40,null=False)
    surname = models.CharField(max_length=40,null=False)
    m_initial = models.CharField(maxlength=40,null = False)
    count = models.IntegerField(default=0)
    
    def __unicode__(self):
        return unicode((self.cpno,self.surname,self.first_name))
    
class orders (models.Model):
    order_number = models.AutoField(primary_key=True)
    cpno = models.ForeignKey(customers,null=False)
    time = models.DateTimeField(default=datetime.datetime.now())
    isDone = models.BooleanField()
    

