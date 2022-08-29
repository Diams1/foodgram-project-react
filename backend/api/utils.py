import csv

from django.db.models import Sum

from recipes.models import IngredientAmount


def create_shopping_list(user, response):
    ingredients = IngredientAmount.objects.filter(
        recipe__shopping__user=user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(ingredient_amount=Sum('amount')).values_list(
        'ingredient__name', 'ingredient__measurement_unit',
        'ingredient_amount')

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    for item in list(ingredients):
        writer.writerow(item)

    return response
