from django.core.validators import MaxLengthValidator
from django.db import models


class Chapter(models.Model):
    text = models.TextField(validators=[MaxLengthValidator(2000)])

    def __str__(self):
        return self.text


class Ticket(models.Model):
    chapter = models.OneToOneField(to=Chapter, on_delete=models.CASCADE)
    question = models.TextField(validators=[MaxLengthValidator(100)])
    picture = models.ImageField()
    answer = models.TextField(validators=[MaxLengthValidator(100)])
    explanation = models.TextField(validators=[MaxLengthValidator(2000)])

    def __str__(self):
        return f"{self.chapter} {self.question} {self.answer}"
