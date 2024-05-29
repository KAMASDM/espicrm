from rest_framework import serializers
from .models import assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment
        fields = [
            'id', 'assigned_users', 'enquiry', 'student_country', 'university',
            'level_applying_for', 'course_interested', 'intake_interested', 'specialisation',
            'duration', 'application_fee', 'tution_fee', 'fee_currency', 'course_link',
            'AssesmentFollowup', 'ass_status', 'notes'
        ]

    def validate_ass_status(self, value):
        if not value:
            raise serializers.ValidationError("This field is required.")
        return value

    def create(self, validated_data):
        return assessment.objects.create(**validated_data)