from django.contrib import admin
from .models import Query
# Register your models here.
class user_query_model(admin.ModelAdmin):
    items_list = ('username','topic','description')

admin.site.register(Query,user_query_model)
