from django.contrib import admin
from emps.models import Department, Position, Employees

# Register your models here.

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
