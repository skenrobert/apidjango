from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    # fields = '__all__' TODO: below other form
    fields = ('id','title','description','technology','created_at')
    read_only_fields = ('created_at',)# end with comma 