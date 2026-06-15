from django.db import models

class feedback(models.Model):

    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Library', 'Library'),
        ('Hostel', 'Hostel'),
        ('Cafeteria', 'Cafeteria'),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    feedback_type = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    message = models.TextField()

    def _str_(self):
        return self.name


