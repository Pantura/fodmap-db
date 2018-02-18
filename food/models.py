from django.db import models


class FoodCategory(models.Model):
    """
    A category that a food belongs to
    """

    name = models.CharField(max_length=120, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class FoodClassification(models.Model):
    """
    Classification for a food that be for example: OK or Severe effects.
    """
    name = models.CharField(max_length=120, null=True, blank=True, default="")
    level = models.IntegerField(unique=True)

    def __str__(self):
        return "{}-{}".format(self.level, self.name)


class Food(models.Model):
    """
    A food substance that might cause or is known not to cause symptoms.
    """
    name = models.CharField(max_length=120, null=True, blank=True, default="")
    notes = models.TextField(null=True, blank=True, default="")
    category = models.ForeignKey(FoodCategory, null=True, on_delete=models.SET_NULL)
    classification = models.ForeignKey(FoodClassification, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} - {}".format(self.name, self.classification)
