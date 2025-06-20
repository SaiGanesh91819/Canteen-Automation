from django.db import models # type: ignore

# Create your models here.
class items(models.Model):

    item_id = models.IntegerField()
    item_name = models.CharField(max_length=30)
    item_type = models.CharField(max_length=30)
    item_price = models.DecimalField(decimal_places=2,max_digits=5)
    item_availability = models.IntegerField()
    item_img = models.ImageField(upload_to='item_imgs/',null=True)
