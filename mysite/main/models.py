from django.db import models

class Memories(models.Model):
    name_memorie = models.CharField('Name', max_length=150)
    date_memorie = models.DateField('Date of memorie')
    description_memorie = models.TextField()

    def __str__(self):
        return self.name_memorie
