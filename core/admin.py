from django.contrib import admin
from core.models import State
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(UserAdmin)


@admin.register(State)
class StateModelAdmin(admin.ModelAdmin):
    list_display = ['id', "title", 'desc', 'pic']
