from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Favorite, Ingredient, IngredientAmount, Recipe, Shopping,
                     Tag, TagRecipe)


class TagsInline(admin.TabularInline):
    model = TagRecipe
    extra = 1


class IngredientInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '--пусто--'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    save_on_top = True
    empty_value_display = '--пусто--'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'is_favorited', )
    search_fields = ('author', 'name', 'tags')
    inlines = (IngredientInline, TagsInline)
    empty_value_display = '--пусто--'

    def is_favorited(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    is_favorited.short_description = 'В избранном'

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '--пусто--'


@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '--пусто--'
