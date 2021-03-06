from django.contrib import admin
from Core.models import Wallet

# Wallet admin
class WalletsAdmin(admin.ModelAdmin):
    list_display = ('id','user','name')
    search_fields = ('id','user','name')

admin.site.register(Wallet,WalletsAdmin)
