from django.contrib import admin
from JKNGO.models import cloth, food, plant, rupees
from JKNGO.models import person
# Register your models here.
admin.site.register(person);
admin.site.register(plant);
admin.site.register(cloth);
admin.site.register(rupees);
admin.site.register(food);
