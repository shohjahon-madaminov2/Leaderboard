from django.urls import path

from petrol_spy.views import LeaderboardView

urlpatterns = [
    path('leaderboard/', LeaderboardView.as_view())
]
