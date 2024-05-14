from django.db import models

class Units(models.Model):
  """Model for measurement units (e.g., cups, grams)."""
  name = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.name

class Stores(models.Model):
  """Model for stores where ingredients can be purchased."""
  store_name = models.CharField(max_length=255)
  address = models.TextField()

  def __str__(self):
    return self.store_name

class Categories(models.Model):
  """Model for recipe categories (e.g., breakfast, dessert)."""
  category = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.category
  
class Departments(models.Model):
  """Model for recipe departments (e.g., diary, meat)."""
  department = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.department

class Frequencies(models.Model):
  """Model for recipe frequencies (e.g., daily, weekly)."""
  frequency = models.CharField(max_length=255)
  duration = models.IntegerField(blank=True)

class Locations(models.Model):
  """Model for ingredient locations (e.g., fridge, pantry)."""
  location = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.department

class Ingredients(models.Model):
  """Model for ingredients used in recipes."""
  ingredient = models.CharField(max_length=255)
  location = models.ForeignKey(Locations, on_delete=models.CASCADE)
  qty = models.FloatField(blank=True, null=True)  # Can be null if not tracked
  unit = models.ForeignKey(Units, on_delete=models.CASCADE)
  is_favorite = models.BooleanField(default=False)

  def __str__(self):
    return self.ingredient

class Recipes(models.Model):
  """Model for recipes."""
  recipe_name = models.CharField(max_length=255)
  instructions = models.TextField()
  servings = models.IntegerField()
  last_made = models.DateField(blank=True, null=True)  # Can be null if not tracked
  on_schedule = models.BooleanField(default=False)
  category = models.ForeignKey('Categories', on_delete=models.CASCADE)
  frequency = models.ForeignKey('Frequencies', on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.recipe_name

class RecipeIngredients(models.Model):
  """Model for associating ingredients with recipes."""
  recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
  qty = models.FloatField()
  unit = models.ForeignKey(Units, on_delete=models.CASCADE)
  is_optional = models.BooleanField(default=False)

  class Meta:
    unique_together = (('recipe', 'ingredient'),)  # Ensure unique combination of recipe and ingredient

  def __str__(self):
    return f"{self.recipe.recipe_name} - {self.ingredient.ingredient}"

class Products(models.Model):
  """Model for specific product instances of an ingredient."""
  ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
  brand = models.CharField(max_length=255)
  size = models.CharField(max_length=255)
  store = models.ForeignKey(Stores, on_delete=models.CASCADE)
  department = models.ForeignKey(Departments, on_delete=models.CASCADE)
  isle = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return f"{self.ingredient.ingredient} ({self.brand} - {self.size})"

class Prices(models.Model):
  """Model for tracking product prices over time."""
  product = models.ForeignKey(Products, on_delete=models.CASCADE)
  date = models.DateField()
  cost = models.DecimalField(max_digits=10, decimal_places=2)

  class Meta:
    unique_together = (('product', 'date'),)  # Ensure unique combination of product and date

  def __str__(self):
    return f"{self.product.ingredient.ingredient} - {self.product.brand} - {self.date} (${self.cost})"