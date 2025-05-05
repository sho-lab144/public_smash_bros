from django.contrib import admin
from .models import Match

#admin.site.register(Match)

@admin.register(Match)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ["match_id"]
