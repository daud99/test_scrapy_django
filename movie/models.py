from djongo import models as models

# Create your models here.

class Movie(models.Model):
    id = models.ObjectIdField(db_column="_id")
    source = models.CharField(max_length=255)
    title = models.TextField()
    description = models.TextField()
    reviews = models.TextField()
    quotes = models.TextField()

    def __str__(self):
        return self.source