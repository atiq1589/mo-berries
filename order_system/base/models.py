from django.db import models
from django.conf import settings


class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              related_name='%(class)s_created_by', on_delete=models.SET_NULL, null=True, blank=True)
  modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='%(class)s_modified_by', on_delete=models.SET_NULL, null=True, blank=True)

  def save(self, *args, **kwargs):
    self.full_clean()
    super().save(*args, **kwargs)
  class Meta:
    abstract = True
    