from django.conf.urls import url
from .views import ScoreBoard


urlpatterns = [
    url(r'$', ScoreBoard.as_view(), name='scoreboard')
]
