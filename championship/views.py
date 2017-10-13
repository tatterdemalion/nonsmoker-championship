from django.views.generic.list import ListView
from championship.models import NonSmoker


class ScoreBoard(ListView):
    model = NonSmoker
