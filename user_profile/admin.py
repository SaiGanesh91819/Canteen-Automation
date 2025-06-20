from django.contrib import admin # type: ignore
from user_profile.models import user_profile_data


class user_profile_model(admin.ModelAdmin):
    items_list = ('first_name','last_name','phone_number','email','branch','reg_no')

admin.site.register(user_profile_data,user_profile_model)
