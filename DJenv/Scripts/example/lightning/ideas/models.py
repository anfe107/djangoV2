from django.db import models

# TODO  generated file for defining model (-classes)

class Question(models.Model):
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    end = models.DateTimeField()
    lifespan_ideas = models.DurationField()

    def __str__(self):
        return '{} fragt: {}'.format(self.author, self.text)

class Idea(models.Model):
    test = models.CharField(max_length=200),
    end = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Keyword(models.Model):
    text = models.CharField(max_length=20)

# Create your models here.
