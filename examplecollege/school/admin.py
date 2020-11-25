from django.contrib import admin
from .models import Learner, Person

#Register your models here.

admin.site.register(Learner)
admin.site.register(Person)