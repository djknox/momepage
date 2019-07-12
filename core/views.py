from django.shortcuts import render
from core.models import Cohort, Day
import datetime

def today(request):
    """
    View function for home page of site.
    The homepage currently displays Cohort 5's current day information.
    """
    yesterday = True
    tomorrow = True

    day = Day.objects.filter(date=datetime.date.today()).first()

    if datetime.date.today().weekday() == 0:
        yesterday = False

    if datetime.date.today().weekday() == 4:
        tomorrow = False

    return render(request, 'index.html', {
        'day': day,
        'yesterday' : yesterday,
        'tomorrow' : tomorrow,
    })


def previous_day(request):
    """
    View function for 'previous day' (usually yesterday) page of site, displaying the previous day's info.
    """
    yesterday = True
    day = Day.objects.filter(date=datetime.date.today() - datetime.timedelta(days = 1)).first()
    return render(request, 'index.html', {'day': day})


def next_day(request):
    """
    View function for 'next day' page of site (usually tomorrow), displaying the next day's info.
    """
    tomorrow = True
    day = Day.objects.filter(date=datetime.date.today() + datetime.timedelta(days = 1)).first()
    return render(request, 'index.html', {'day': day})