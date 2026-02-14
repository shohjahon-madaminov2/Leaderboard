from django.contrib.auth.models import User
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from petrol_spy.serializers import LeaderborardSerializer


class LeaderboardView(APIView):
    def get(self, request):
        users = User.objects.annotate(
            reports_count=Count('reports')
        ).order_by('-reports_count')[:10]
        
        serializer = LeaderborardSerializer(users, many=True)
        
        return Response(
            {'users': serializer.data}
        )
