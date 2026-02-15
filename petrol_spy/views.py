from django.contrib.auth.models import User
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from petrol_spy.models import Report


class LeaderboardView(APIView):
    def get(self, request):
        top_reports = Report.objects.values('user_id').annotate(
            cnt = Count('id')
        ).order_by('-cnt')[:10]
        
        top_user_ids = [item['user_id'] for item in top_reports]
        counts_dict = {item['user_id']: item['cnt'] for item in top_reports}
        
        users = User.objects.filter(
            id__in=top_user_ids
        ).select_related('oneid_profile')
        
        results = []
        
        for user in users:
            profile = getattr(user, 'oneid_profile', None)
            results.append(
                {
                    'user': user.id,
                    'display_name': profile.full_name if profile and profile.full_name else user.username,
                    'reports_count': counts_dict[user.id]
                }
            )
        results.sort(key=lambda x: x['reports_count'], reverse=True)
        return Response({'users': results})
