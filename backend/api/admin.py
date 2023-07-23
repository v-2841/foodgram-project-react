from django.contrib import admin

from .models import (
    Tag, Ingredient, IngredientSpecification, Recipe, TagRecipe,
    UserFavoritedRecipe, UserShoppingCart,
)

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(TagRecipe)
admin.site.register(Ingredient)
admin.site.register(IngredientSpecification)
admin.site.register(UserFavoritedRecipe)
admin.site.register(UserShoppingCart)