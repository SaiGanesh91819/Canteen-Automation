from django.contrib import admin
from items.models import items
# Register your models here.

class item_model (admin.ModelAdmin):
    items_list = ('item_id','item_name','item_type','item_price','item_availability','item_img')

admin.site.register(items,item_model)