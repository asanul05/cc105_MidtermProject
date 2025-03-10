from datetime import datetime,date
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=False)
    status = models.CharField(max_length=20, default='Pending')  

    def save(self, *args, **kwargs):
        """Override save to set status based on due date."""
     
        self.due_date = datetime.strptime(self.due_date, '%Y-%m-%d').date() 

        if self.due_date > date.today():
            self.status = 'Upcoming'
        elif self.due_date == date.today():
            self.status = 'Due Today'
        else:
            self.status = 'Overdue'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    