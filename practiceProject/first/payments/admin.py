from django.contrib import admin
from payments.models import pay_method

# Register your models here.
class pay_methodAdmin(admin.ModelAdmin):# inherit apply to admin.model
    list_display = ('id','pay_id','pay_option','min_pay') # we resister model class
    
admin.site.register(pay_method,pay_methodAdmin)# we resigter pay_methoAdmin class