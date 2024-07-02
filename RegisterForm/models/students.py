from django.db import models

class Students(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=256)
    college_name = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=10)
    whatsapp_number = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    department = models.CharField(max_length=256)
    year = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.is_paid} - {self.email}"
