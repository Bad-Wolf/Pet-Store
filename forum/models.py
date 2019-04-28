from django.db import models


class Question(models.Model):
    author = models.CharField(max_length=20, default='Anonymous')
    question_field = models.TextField()

    def __str__(self):
        return f'{self.author} {self.question_field}'


class Answer(models.Model):
    author = models.CharField(max_length=20, default='Anonymous')
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f'{self.author} {self.content[:10]}...'


