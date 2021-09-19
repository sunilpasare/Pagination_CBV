from django.contrib import admin
from .models import Laptop

class LaptopAdmin(admin.ModelAdmin):
    list_display=['id','Modelname','Company','Ram','Rom','Weight','Processor','document']

admin.site.register(Laptop,LaptopAdmin)





