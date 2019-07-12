from django.db import models

class Cohort(models.Model):
    """Model representing a Momentum cohort."""
    name = models.CharField(max_length=300, help_text= "Enter the name of the cohort here.")
    start_date = models.DateField(null=True, blank=True, help_text="Enter the start date for the cohort here.")
    end_date = models.DateField(null=True, blank=True, help_text="Enter the end date for the cohort here.")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Cohort object."""
        return self.name


class Day(models.Model):
    """Model representing a day of class for a Momentum cohort."""
    number = models.IntegerField(help_text= "Enter the number of the day here.")
    date = models.DateField(unique=True, help_text="Enter the date of the day here.")
    description = models.TextField(null=True, blank=True, help_text="Enter the description of the day here.")
    created_date = models.DateTimeField(auto_now_add=True)

    # a Day belongs to one Cohort, and a Cohort will have many Days
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Day object."""
        return f"Day {self.number}"

    class Meta:
        ordering = ['-number']


class AgendaItem(models.Model):
    """Model representing an item on the agenda for a Day."""
    description = models.TextField(help_text="Enter the description of the agenda item here.")
    created_date = models.DateTimeField(auto_now_add=True)

    # an AgendaItem belongs to one Day, and a Day will have many AgendaItems
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the AgendaItem object."""
        return self.description


class GuestLecture(models.Model):
    """Model representing a guest lecture for a Day."""
    start_time = models.TimeField(help_text="Enter the time when the guest lecture will start.")
    end_time = models.TimeField(help_text="Enter the time when the guest lecture will end.")
    speaker = models.CharField(max_length=300, help_text= "Enter the name of the guest speaker here.")
    description = models.TextField(help_text="Enter the description of guest lecture here.")
    created_date = models.DateTimeField(auto_now_add=True)

    # an AgendaItem belongs to one Day, and a Day will have many AgendaItems
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the GuestLecture object."""
        return f"{self.speaker} - {self.description}"


class FieldTrip(models.Model):
    """Model representing a field trip for a Day."""
    start_time = models.TimeField(help_text="Enter the time when the field trip will start.")
    end_time = models.TimeField(help_text="Enter the time when the field trip will end.")
    company = models.CharField(max_length=300, help_text= "Enter the name of the company here.")
    description = models.TextField(help_text="Enter the description of the field trip here.")
    created_date = models.DateTimeField(auto_now_add=True)

    # a FieldTrip belongs to one Day, and a Day will have many FieldTrips
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the GuestLecture object."""
        return self.company