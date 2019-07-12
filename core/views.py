from django.shortcuts import render
from core.models import Cohort, Day
import datetime

def today(request):
    """
    View function for home page of site.
    The homepage currently displays Cohort 5's current day information.
    """
    day = Day.objects.filter(date=datetime.date.today()).first()
    return render(request, 'index.html', {'day': day})


def yesterday(request):
    """
    View function for 'yesterday' page of site, displaying the previous day's info.
    """
    day = Day.objects.filter(date=datetime.date.today() - datetime.timedelta(days = 1)).first()
    return render(request, 'index.html', {'day': day})


def tomorrow(request):
    """
    View function for 'tomorrow' page of site, displaying the next day's info.
    """
    day = Day.objects.filter(date=datetime.date.today() + datetime.timedelta(days = 1)).first()
    return render(request, 'index.html', {'day': day})