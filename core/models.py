from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.FloatField()
  validate = models.DateTimeField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering =  ('-created',)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("core:detail",kwargs={"pk":self.pk})

  def get_absolute_url_update(self):
    return reverse("core:update",kwargs={"pk":self.pk})

  def get_absolute_url_delete(self):
    return reverse("core:delete",kwargs={"pk":self.pk})
  