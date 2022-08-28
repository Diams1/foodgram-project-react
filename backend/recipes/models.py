from django.db import models
from django.db.models.constraints import UniqueConstraint

from users.models import User


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тег',
        max_length=200,
        db_index=True,
        blank=False,
        unique=True
    )
    color = models.CharField(
        verbose_name='Hex-код цвета',
        default='#DCDCDC',
        max_length=7,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=200,
        blank=False,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Ингредиент',
        max_length=200,
        db_index=True,
        blank=False,
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=200,
        blank=False,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        verbose_name='Ингредиенты',
        through='IngredientAmount',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги',
        through='TagRecipe',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        db_index=True,
        blank=False,
    )
    shopping_cart = models.ManyToManyField(
        User,
        related_name='recipes_shopping',
        verbose_name='Список покупок',
        through='Shopping'
    )
    favorite = models.ManyToManyField(
        User,
        related_name='recipes_favorite',
        verbose_name='В избранном',
        through='Favorite',
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        help_text='в минутах',
        blank=False,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    text = models.TextField(verbose_name='Описание', )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='recipes_photo/',
        null=False,
        blank=False
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.name}'


class TagRecipe(models.Model):
    tag = models.ForeignKey(
        Tag,
        verbose_name='Теги',
        on_delete=models.CASCADE,
        related_name='tag_recipes'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipes_tag'
    )

    class Meta:
        verbose_name_plural = 'Теги для рецептов'


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Наименование',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=1,
    )

    class Meta:
        verbose_name_plural = 'Ингредиенты для рецептов'
        constraints = [
            UniqueConstraint(fields=['ingredient', 'recipe'],
                             name='unique ingredients in recipes')
        ]


class Shopping(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping',
        db_index=True,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        constraints = [
            models.UniqueConstraint(fields=('user', 'recipe'),
                                    name='unique cart user')
        ]

    def __str__(self):
        return f'{self.recipe} в списке покупок {self.user}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        db_index=True
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(fields=('user', 'recipe'),
                                    name='favorite recipe for unique user')
        ]

    def __str__(self):
        return f'{self.recipe} в избранном у {self.user}'
