"""models.py"""
from django.db import models

class Unit(models.Model):
    """Model for measurement units (e.g., cups, grams)."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)

class Store(models.Model):
    """Model for stores where ingredients can be purchased."""
    store_name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return str(self.store_name)

class Category(models.Model):
    """Model for recipe categories (e.g., breakfast, dessert)."""
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.category)

class Department(models.Model):
    """Model for recipe departments (e.g., diary, meat)."""
    department = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.department)

class Frequency(models.Model):
    """Model for recipe frequencies (e.g., daily, weekly)."""
    frequency = models.CharField(max_length=255)
    duration = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.frequency)

class Location(models.Model):
    """Model for ingredient locations (e.g., fridge, pantry)."""
    location = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.location)

class Ingredient(models.Model):
    """Model for ingredients used in recipes."""
    ingredient = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    qty = models.FloatField(blank=True, null=True)    # Can be null if not tracked
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ingredient)

class Recipe(models.Model):
    """Model for recipes."""
    recipe_name = models.CharField(max_length=255)
    instructions = models.TextField()
    servings = models.IntegerField()
    last_made = models.DateField(blank=True, null=True)    # Can be null if not tracked
    on_schedule = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    frequency = models.ForeignKey('Frequency', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.recipe_name)

class RecipeIngredient(models.Model):
    """Model for associating ingredients with recipes."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_optional = models.BooleanField(default=False)

    class Meta:
        """Foreign Keys unique combo"""
        unique_together = (('recipe', 'ingredient'),)

    def __str__(self):
        return f"{self.recipe.recipe_name} - {self.ingredient.ingredient}"

class Product(models.Model):
    """Model for specific product instances of an ingredient."""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    isle = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.ingredient.ingredient} ({self.brand} - {self.size})"

class Price(models.Model):
    """Model for tracking product prices over time."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Foreign Keys unique combo"""
        unique_together = (('product', 'date'),)

    def __str__(self):
        return f"{self.product.ingredient.ingredient} - {self.product.brand} - {self.date} (${self.cost})"
    