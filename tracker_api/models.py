from django.db import models
from django.utils.timezone import now
from datetime import date

# Create your models here.
class Answer(models.Model):
    question = models.CharField(max_length=60)
    date = models.DateField(default=now)
    value = models.IntegerField()
    period = models.BooleanField(default=False)
    def __str__(self):
        return self.question
