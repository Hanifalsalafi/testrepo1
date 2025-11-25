from django.contrib import admin
from .models import laptop
# Register your models here.
admin.site.register(laptop)

class laptopAdmin(admin.ModelAdmin):
    list_display = ('password','retype_password','laptop','email', 'about','message',
                    'Checkbox','files','ram','ssd','youtube_channal')