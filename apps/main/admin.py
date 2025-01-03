from django.contrib import admin
from apps.main.models import Settings, Settings_All, News
# Register your models here.
admin.site.register(Settings)
admin.site.register(Settings_All)
admin.site.register(News)
