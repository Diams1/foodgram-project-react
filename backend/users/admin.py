from django.contrib import admin

from .models import Subscription


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username',
        'first_name', 'last_name', 'email', 'password'
    )
    list_filter = ('email', 'username',)
    empty_value_display = '--пусто--'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '--пусто--'
