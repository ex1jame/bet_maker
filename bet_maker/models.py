from django.db import models

# Create your models here.
class Bets(models.Model):
    amount = models.IntegerField()
    STATUS_CHOICES = [
        ('PENDING', 'Ещё не сыграла'),
        ('WON', 'Выиграла'),
        ('LOST', 'Проиграла')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)