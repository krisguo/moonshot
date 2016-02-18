from rest_framework import serializers
from questions.models import Question



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'description')





# class QuestionSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     description = serializers.CharField(style={'base_template': 'textarea.html'})
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Question` instance, given the validated data.
#         """
#         return Question.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Question` instance, given the validated data.
#         :type instance: object
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('code', instance.code)
#         instance.save()
#         return instance
