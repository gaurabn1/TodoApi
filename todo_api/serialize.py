from rest_framework.serializers import ModelSerializer
from .models import *

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'due_date', 'remainder_date']

