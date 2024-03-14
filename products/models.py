from django.db import models

# Model for Produccts

class Products(models.Model):
    del_choices = (
            ('0','delete'),
            ('1','live')
    )
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField()
    del_status = models.IntegerField(choices=del_choices,default=1)
    creat_at = models.DateTimeField(auto_now_add=True)
    updat_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    



