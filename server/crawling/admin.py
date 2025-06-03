from django.contrib import admin
from crawling.models import Match


class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'match_time', 'team_a','team_b')


admin.site.register(Match, MatchAdmin)