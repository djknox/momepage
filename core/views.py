from django.shortcuts import render
from core.models import Cohort, Day
import datetime

def index(request):
    """
    View function for home page of site.
    The homepage currently displays Cohort 5's current day information.
    """
    today = Day.objects.filter(date=datetime.date.today()).first()
    return render(request, 'index.html', {'today': today})