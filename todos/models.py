from django.db import models

# Create your models here.
from django.utils.timezone import now


class Todo(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    content = models.TextField(blank=False, null=False, max_length=5600)
    created_at = models.DateTimeField(verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
