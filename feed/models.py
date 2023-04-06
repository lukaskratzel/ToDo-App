from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):

    text_max_length = 200
    priority_choices = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Very high'),
        (5, 'Urgent'),
    ]

    text = models.CharField(max_length=text_max_length)
    priority = models.IntegerField(choices=priority_choices)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )

    def __str__(self) -> str:
        return f"{self.user.username}: " + self.text[:30]
