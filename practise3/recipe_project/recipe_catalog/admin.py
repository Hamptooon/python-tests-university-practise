from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'raw_weight', 'cooked_weight', 'cost', 'cooking_time')
    search_fields = ('name',)
    list_filter = ('cooking_time',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'calc_cost', 'calc_weight', 'calc_cooking_time')
    search_fields = ('name',)
    inlines = [RecipeIngredientInline]


    def calc_cost(self, obj):
        return obj.calc_cost()
    calc_cost.short_description = 'Cost (RUB)'

    def calc_weight(self, obj):
        return obj.calc_weight()
    calc_weight.short_description = 'Weight (grams)'

    def calc_cooking_time(self, obj):
        return obj.calc_cooking_time()
    calc_cooking_time.short_description = 'Cooking Time (minutes)'


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')
    search_fields = ('recipe__name', 'ingredient__name')



admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
