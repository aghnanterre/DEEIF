from django.db import models
import datetime

# Create your models here.

class Expression(models.Model):
    ''' une Expression est une liste de mots
    '''
    date_creation= models.DateTimeField('date création')
    date_modification=models.DateTimeField('date modification')
    contenu=
    
    def __init__(self,str):
        self.date_creation=datetime.datetime.now()
        
    
    def __str__(self):
        return(self.date_creation)