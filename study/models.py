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


class Participant(models.Model):
    name = models.CharField(max_length=200)
    experience = models.PositiveIntegerField(
        help_text="Years of teaching experience in this field of study"
    )
    department = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Response(models.Model):
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="responses"
    )
    text = models.ForeignKey(TextItem, on_delete=models.CASCADE)
    classification = models.CharField(
        max_length=5, choices=TextItem.TEXT_ORIGIN_CHOICES
    )
    confidence = models.PositiveSmallIntegerField()
    response_time = models.PositiveIntegerField(help_text="Time in milliseconds")
    index = models.PositiveSmallIntegerField(help_text="Order of the text shown")

    def __str__(self):
        return f"{self.participant.name} - {self.text} ({self.classification})"
