from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, usename, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            usename=usename,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, usename, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            usename=usename,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Custom User Model 
class User(AbstractBaseUser):
    usename = models.CharField(max_length=100)
    
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["usename"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin