from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Measure

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




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
    list_display = ('recipe', 'ingredient', 'quantity', 'measure')
    search_fields = ('recipe__name', 'ingredient__name')
    def raw_weight(self, obj):
        """Отображаем вес ингредиента в граммах, учитывая его единицу измерения."""
        return obj.calc_weight(True)  # 1 - это количество, которое мы хотим конвертировать
    raw_weight.short_description = 'Raw Weight (grams)'

    def cooked_weight(self, obj):
        """Отображаем приготовленный вес ингредиента в граммах."""
        if obj.cooked_weight:
            return obj.calc_weight(False)  # 1 - это количество, которое мы хотим конвертировать
        return None
    cooked_weight.short_description = 'Cooked Weight (grams)'

    # Добавляем эти вычисленные поля в список отображаемых данных
    list_display += ('raw_weight', 'cooked_weight')
    # def unit_display(self, obj):
    #     """Отображаем единицу измерения для ингредиента в рецепте."""
    #     return obj.unit.name if obj.unit else 'N/A'
    # unit_display.short_description = 'Unit'


# Регистрируем модели с учетом новых изменений
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Measure)  # Не забудьте зарегистрировать модель Unit для админки
