from django.db import models


class Favorite(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"