from django.db import models

# Create your models here.
class Lead(models.Model):
    SOURCE_CHOICE=(
        ("Walk-in","Walk-in"),
        ("Call","Call"),
        ("Referral","Referral"),
        ("Website","Website")
    )
    STATUS_CHOICE=(
        ("New","New"),
        ("Contacted","Contacted"),
        ("Converted","Converted"),
        ("Lost","Lost")
    )
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    source=models.CharField(max_length=100,choices=SOURCE_CHOICE)
    status=models.CharField(max_length=100,choices=STATUS_CHOICE)
    added_date=models.DateTimeField(auto_now=True)
    notes=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f'{self.name}-{self.phone}'