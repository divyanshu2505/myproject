from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiOrder, ChaiCertification

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1
class ChaiVareityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added', 'date_updated')
    search_fields = ('name',)
    list_filter = ('date_added', 'date_updated')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    inlines = [ChaiReviewInline]

class ChaiCertificationAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certification_body', 'certification_date', 'expiration_date')
    search_fields = ('chai__name', 'certification_body')
    list_filter = ('certification_date', 'expiration_date')
admin.site.register(ChaiVarity)

