from django.db import models


class Card(models.Model):
    uuid: str = models.CharField(
        max_length=100, unique=True, primary_key=True, db_index=True
    )
    name: str = models.CharField(max_length=100)
    text: str = models.TextField(null=True)
    rulings: str = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name
