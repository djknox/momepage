from django.shortcuts import render
from core.models import Cohort, Day
import datetime

def today(request):
    """
    View function for home page of site.
    The homepage currently displays Cohort 5's current day information.
    """
    previous_day_name = 'yesterday'
    next_day_name = 'tomorrow'
    day_name = 'today'

    day = Day.objects.filter(date=datetime.date.today()).first()

    if is_Monday():
        previous_day_name = 'Friday'

    if is_Friday():
        next_day_name = 'Monday'

    return render(request, 'index.html', {
        'day': day,
        'dayName': day_name,
        'previousDayName' : previous_day_name,
        'nextDayName' : next_day_name,
    })

def is_Monday():
    """
    Returns true if it's Monday today
    """
    if datetime.date.today().weekday() == 0:
        return True
    else :
        return False

def is_Friday():
    """
    Returns true if it's Friday today
    """
    if datetime.date.today().weekday() == 4:
        return True
    else :
        return False

def previous_day(request):
    """
    View function for 'previous day' (usually yesterday) page of site, displaying the previous day's info.
    """
    previous_day_name = ''
    if is_Monday():
        day_name = 'Friday'
        next_day_name = 'Monday'
    else:
        day_name = 'yesterday'
        next_day_name = 'today'
    day = Day.objects.filter(date=datetime.date.today() - datetime.timedelta(days = 1)).first()
    return render(request, 'index.html', {
        'dayName': day_name,
        'previousDayName': previous_day_name,
        'nextDayName': next_day_name
    })


def next_day(request):
    """
    View function for 'next day' page of site (usually tomorrow), displaying the next day's info.
    """
    next_day_name = ''
    if is_Friday():
        day_name = 'Monday'
        previous_day_name = 'Friday'
    else:
        day_name = 'tomorrow'
        previous_day_name = 'today'
    day = Day.objects.filter(date=datetime.date.today() - datetime.timedelta(days = 1)).first()
    return render(request, 'index.html', {
        'dayName': day_name,
        'previousDayName': previous_day_name,
        'nextDayName': next_day_name
    })