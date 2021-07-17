from django.db import models
from django.contrib.auth.models import User

# Create your models here.  # create your database model
# title
# status
# date - current
# user
# priority



class TODO(models.Model):
    # created status_choices
    status_choices = [                 
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]       

    #created priority_choices   - 10 choices --> putting emoji              
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)    # we will make choices here
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choices)    # we will make choices here
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # on_delete=models.CASCADE If we delete any user the Todo regarding that user will be deleted
                                                                # User has been imported



    # Once model of database is created we have to just run the command to create database >python manage.py makemigrations
    ''' Database is created
    Migrations for 'app':
    app\migrations\0001_initial.py
    - Create model TODO
    '''
    # Now to make table in database we have to do >python manage.py migrate
    # Now the table is created in database.
    

