from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

# Validations

def validate_student_number(value):
    if value[0] != "L" or value[1] != "E":
        raise ValidationError(
        f"{value} is not a valid Student number, must be in the format LE<6 digit code>"
    )
    if not re.sub('LE','',value).isnumeric():
        raise ValidationError(
        f"{value} is not a valid Student number, end 6 characters must be digits"
    )

def validate_email_address(value):
    validate_email = EmailValidator
    if not validate_email(value):
        raise ValidationError(
        f"{value} is not a valid email address"
    )

def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
        f"{value} cannot contain numbers"
    )

def validate_phone(value):
    if not value.isnumeric():
        raise ValidationError(
            f"{value} must be a number."
        )
    if value[0] != "0":
        raise ValidationError(
        f"{value} must have a valid dialling code."
        )      
    if value[1] not in [str(x) for x in range(1,9)]:
        raise ValidationError(
        f"{value} must have a valid dialling code."
        )
    if value[2] not in [str(x) for x in range(0,9)]:
        raise ValidationError(
        f"{value} must have a valid dialling code."
        )

# Models

class Person(models.Model):
    first_name = models.CharField(max_length=30, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[validate_name])
    phone_number = models.CharField(max_length=10, validators=[validate_phone])
    email_address = models.CharField(max_length=50, validators=[validate_email_address])

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Learner(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    student_number = models.CharField(max_length=8, unique=True, validators=[validate_student_number])
    # qualification = 

    def __str__(self):
        return f"{self.student_number}, {self.person}"
