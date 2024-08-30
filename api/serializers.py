from rest_framework import serializers
from .models import Student,Course,Instructor,Singer,Song

# class StudentSerializer(serializers.Serializer):
#     name    = serializers.CharField(max_length=100)
#     roll    = serializers.IntegerField()
#     city    = serializers.CharField(max_length=100)


# class StudentSerializer(serializers.Serializer):
#     name    = serializers.CharField(max_length=100)
#     roll    = serializers.IntegerField()
#     city    = serializers.CharField(max_length=100)

#     def create(self,validated_data):
#         return Student.objects.create(**validated_data)

#Field Level validation
#     def validate_roll(self, value):
#         if value>=200:
#             return serializers.ValidationError('Seats Full')
#         return value

#object Level validation
    # def validate(self, attrs):
    #     if attrs.get('account_type') == 'business' and not attrs.get('business_profile'):
    #         raise serializers.ValidationError("Business profile is required for business account type")
    #     return attrs

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        
class InstructorSerializer(serializers.ModelSerializer):
    crs=CourseSerializer(many=True, read_only=True)
    class Meta:
        model=Instructor
        # fields='__all__'
        fields=['name','email','crs']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:asf
        model=Song
        fields='__all__'

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True, read_only= True)
    class Meta:
        model=Singer
        fields=['name','sungby']