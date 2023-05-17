from django.db import models

class Pet(models.Model):
    id=1
    name = "Nokdu"
    age = "2 years old"
    breed = "unknown"
    description = "Cute"


    def __str__(self):
        return self.name
