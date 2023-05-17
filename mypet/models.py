from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey는 다른 모델과 연결하기 위해 사용
    content = models.TextField()
    create_date = models.DateTimeField()