from django.db import models


# Creating a Student table in django database to see in Django Administration
class Student(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    name = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=20, null=True)
    roll_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:   # To Display the name in Admin Panel
        # Model name correction; it appears Students(extra s) in Admin Panel
        verbose_name_plural = "Students"
