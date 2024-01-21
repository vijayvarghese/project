from django.db import models

class MyFormData(models.Model):
    input1 = models.CharField(max_length=255)
    input2 = models.CharField(max_length=255)
    rich_text_field = models.TextField(default='')
    #rich_input = models.TextField()

    def __str__(self):
        return f"{self.input1} - {self.input2}"
