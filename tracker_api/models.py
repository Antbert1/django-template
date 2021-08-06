from django.db import models

# Create your models here.
class Answer(models.Model):
    question = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now=True)
    value = models.IntegerField()
    def __str__(self):
        return self.question
