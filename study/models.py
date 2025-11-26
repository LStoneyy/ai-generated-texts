from django.db import models


class TextItem(models.Model):
    TEXT_ORIGIN_CHOICES = [
        ("human", "Human-written"),
        ("ai", "AI-generated"),
    ]

    title = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    origin = models.CharField(max_length=5, choices=TEXT_ORIGIN_CHOICES)

    def __str__(self):
        return f"{self.title or 'Text'} ({self.origin})"
