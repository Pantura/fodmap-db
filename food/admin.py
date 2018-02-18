

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from food.models import Food, FoodCategory, FoodClassification


class FoodAdmin(TranslationAdmin):
    list_display = ('name', 'category', 'classification', )


class FoodCategoryAdmin(TranslationAdmin):
    list_display = ('name', )


class FoodClassificationAdmin(TranslationAdmin):
    list_display = ('level', 'name', )


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodClassification, FoodClassificationAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
