# from django.contrib.auth.models import User

# from rest_framework import serializers


# class LeaderborardSerializer(serializers.ModelSerializer):
#     display_name = serializers.SerializerMethodField()
#     reports_count = serializers.SerializerMethodField()
    
#     class Meta:
#         model = User
#         fields = ('id', 'display_name', 'reports_count')
        
        
#     def get_display_name(self, obj):
#         return obj.oneid_profile.full_name if hasattr(obj, 'oneid_profile') and obj.oneid_profile.full_name else obj.username

            
#     def get_reports_count(self, obj):
#         return obj.reports.count()
