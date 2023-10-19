from django.contrib import admin
from .models import Student,Item,Booking

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemcode','itemname','image_tag','itemstatus')
    readonly_fields= ['image_tag']
admin.site.register(Item,ItemAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('uid','itemcode','startdate','enddate','quantity','bookingstatus')
    list_editable = ('bookingstatus',)
admin.site.register(Booking,BookingAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('uid','name','email')
admin.site.register(Student,StudentAdmin)