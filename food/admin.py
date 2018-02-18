
from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget
from modeltranslation.admin import TranslationAdmin

from food.models import Food, FoodCategory, FoodClassification


class FoodResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(FoodCategory, 'name'))

    class Meta:
        model = Food
        exclude = ('name', 'notes')
        export_order = ('id', 'name_fi', 'name_en', 'notes_fi', 'notes_en')


class FoodAdmin(TranslationAdmin, ImportExportActionModelAdmin):
    list_display = ('name', 'category', 'classification', )

    list_filter = ('category', 'classification', )
    resource_class = FoodResource


class FoodCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'name_fi', 'name_en', )
    list_editable = ('name_fi', 'name_en', )


class FoodClassificationAdmin(TranslationAdmin):
    list_display = ('level', 'name', )


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodClassification, FoodClassificationAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
