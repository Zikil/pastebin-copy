from django.contrib import admin
from .models import Paste

# Register your models here.

#admin.site.register(Paste)
# Define the admin class
class PasteAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug', 'author', 'create_time', 'life_time', 'die_time', 'access')


# Register the admin class with the associated model
admin.site.register(Paste, PasteAdmin)
