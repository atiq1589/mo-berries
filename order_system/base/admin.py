from django.contrib import admin


class ModelMixin(object):
  exclude = ['created_by', 'modified_by', 'created_at', 'modified_at']

  def save_model(self, request, obj, form, change):
    if change:
      obj.modified_by = request.user
    else:
      obj.created_by = request.user
        
    super().save_model(request, obj, form, change)

class BaseModelAdmin(ModelMixin, admin.ModelAdmin):
  pass


class BaseModelTabularInlineAdmin(ModelMixin, admin.TabularInline):
  pass