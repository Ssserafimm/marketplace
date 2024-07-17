from django.db import models
from item.models import Item

# Create your models here sd.

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversation')