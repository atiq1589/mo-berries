from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
  """
  Base serializer
  """
  def create(self, validated_data):
    request = self.context['request']
    if request.user.is_authenticated:
        validated_data['created_by'] = request.user
    return super().create(validated_data)
