from django.contrib import admin
from quotes_app.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ("author", "quote", "years", "area", "image")
    list_filter = ("author", "area")
    search_fields = ("author", "years", "area")

admin.site.register(Quote, QuoteAdmin)
