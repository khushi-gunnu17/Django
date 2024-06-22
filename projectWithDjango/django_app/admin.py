from django.contrib import admin
from .models import fruitVariety, fruitReviews, Store, Certificate

# Register your models here.
class FruitReviewInline(admin.TabularInline) : 
    model = fruitReviews
    extra = 2


class fruitVarietyAdmin(admin.ModelAdmin) :
    list_display = ('name', 'type', 'date_added')
    inlines = [FruitReviewInline] 


class StoreAdmin(admin.ModelAdmin) :
    list_display = ('name', 'location')
    filter_horizontal = ('fruit_varities', )


class fruitCertificate(admin.ModelAdmin) :
    list_display = ('fruit', 'certificate_number')



admin.site.register(fruitVariety, fruitVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Certificate, fruitCertificate)