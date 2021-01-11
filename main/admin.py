from django.contrib import admin

from .models import Team
from .models import Member

admin.site.register(Team)
admin.site.register(Member)
