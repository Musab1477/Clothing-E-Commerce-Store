from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    # message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


class signUpDetail(models.Model):
    userId = models.IntegerField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.EmailField(unique=True, max_length=25)
    mobileNumber = models.CharField(validators=[phone_validator], max_length=17, blank=False, default='+1234567890')
    password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.firstName
    
class OTP(models.Model):
    user = models.ForeignKey(signUpDetail, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return timezone.now() < self.expires_at
    
    def __str__(self):
        return self.user.firstName