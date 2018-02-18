

from modeltranslation.translator import translator, TranslationOptions
from food.models import FoodCategory, Food, FoodClassification


class FoodCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'notes', )


class FoodClassificationTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(FoodCategory, FoodCategoryTranslationOptions)
translator.register(FoodClassification, FoodClassificationTranslationOptions)
translator.register(Food, FoodTranslationOptions)


