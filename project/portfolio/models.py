from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from decimal import *
  

# Create your models here.
class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length = 255)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.portfolio_name

    def to_json(self):
        return dict(
            id = self.id,
            portfolio_name = self.portfolio_name
        )



class Asset(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    quantity = models.IntegerField(default = 0)
    cost_basis = models.DecimalField(max_digits = 6, decimal_places = 2,default = 0.00)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id') 

    


    def to_json(self,value,portfolio_value):
        return dict(
            id = self.id,
            quantity = self.quantity ,
            cost_basis = self.cost_basis ,
            content_object = self.content_object.to_json(),
            content_type = str(self.content_type),
            object_id = str(self.object_id), 
            value = value,
            weight =  value * 100 / portfolio_value

        )

    # def to_json(self):
    #     return dict(
    #         id = self.id,
    #         quantity = self.quantity ,
    #         cost_basis = self.cost_basis ,
    #         content_object = self.content_object.to_json(),
    #         content_type = str(self.content_type),
    #         object_id = str(self.object_id)

    #     )
