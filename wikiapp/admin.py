from django.contrib import admin
from wikiapp import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','sex','birth','phone','enabled')

admin.site.register(models.User, UserAdmin)