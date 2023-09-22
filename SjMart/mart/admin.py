from django.contrib import admin
from .models import Acquisition,name,staff,job_categories,shifts,suppliers,staff_in_shift

admin.site.register(Acquisition)
admin.site.register(name)
admin.site.register(staff)
admin.site.register(job_categories)
admin.site.register(shifts)
admin.site.register(suppliers)
admin.site.register(staff_in_shift)

# Register your models here.
