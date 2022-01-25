from django.db import models


# Create your models here.
from django.core.validators import MinLengthValidator


"""class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    Tenantorwner  = models.CharField(max_length=50)
    block = models.CharField(max_length=1)
    unit = models.CharField(max_length=5)

    #def register(self):
        #self.save()

    #to return the customer object based on the email provided
   # @staticmethod
   # def get_customer_by_email(email):
        #try:
           # return Customer.objects.get(email=email)
        #except:
           # return False

    #to check if the entered email is already registered into our database,if yes then show the required error message
   # def isExists(self):
       # if Registration.objects.filter(email = self.email):
            #return True
#  return  False"""



