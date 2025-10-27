from django.db import models

class UsersDetails(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    class Meta:
        db_table = "users_details"

    def __str__(self):
        return f"{self.name} ({self.user_type})"
