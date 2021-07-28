from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Verse(models.Model):
    book = models.CharField(max_length=50)
    chapter = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    verse = models.PositiveIntegerField(validators=[MinValueValidator(1)]) # for simplicity's sake, one verse for now
    version = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.book + str(self.chapter) + ":" + str(self.verse) + "(" + self.version + ")"