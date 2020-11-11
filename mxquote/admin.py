from django.contrib import admin

# Register your models here.
from .models import SCB, RE, MPC, Licencias, MIC

admin.site.register(SCB)
admin.site.register(RE)
admin.site.register(MPC)
admin.site.register(Licencias)
admin.site.register(MIC)
