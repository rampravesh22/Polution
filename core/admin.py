from django.contrib import admin
from core.models import State,Pollution
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(UserAdmin)


# @admin.register(State)
# class StateModelAdmin(admin.ModelAdmin):
#     list_display = ['id', "title", 'desc', 'pic']

@admin.register(Pollution)
class PollutionModelAdmin(admin.ModelAdmin):
    list_display = ['id', "City", 'Date', 'Pm2','Pm10','No','No2','Nox','Nh3','Co','So2','O3','Benzene','Toluene','Xylene','Aqi','Air_quality']
