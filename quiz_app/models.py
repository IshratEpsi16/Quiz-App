from django.db import models

# here 'table' is the table of our quiz db


class table(models.Model):
    question = models.CharField(max_length=300)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_ans = models.CharField(max_length=300)
