from rest_framework import serializers

from .models import Course,Lesson

class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    lessons_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = "__all__"
    
    def get_lessons_count(self,obj):
        return obj.lessons.filter(deleted_at__isnull=True).count()
    
    def get_owner_email(self,obj):
        return obj.owner.email
        
    
    
    
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"