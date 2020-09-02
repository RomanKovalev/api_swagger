from django.db import models

class Student(models.Model):

    MARKS_CHOICES =( 
        (2, "Неудовлетворительно"), 
        (3, "Удовлетворительно"), 
        (4, "Хорошо"), 
        (5, "Отлично"), 
    ) 

    full_name = models.CharField(max_length=100, blank=False, null=True)
    birth_date = models.DateField(blank=False, null=True)
    mark = models.IntegerField(choices=MARKS_CHOICES, blank=True)

    def __str__(self):
        return "{} ({})".format(self.full_name, self.birth_date)
