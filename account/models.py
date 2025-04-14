from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField



class UserAccountManager(BaseUserManager):
    
    def create_user(self, email, fullname, phone,password=None):
        if not email:
            raise ValueError("User must have an email")
        else:
            email = self.normalize_email(email)
            user = self.model(email=email, fullname=fullname, phone=phone)
            user.set_password(password)
            user.save()
            return user
        

    def create_superuser(self, email, fullname, password):
        user = self.create_user(email=email, fullname=fullname, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    


class UserAccount(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True)
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=13,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)




    class Meta:
        indexes = [
            models.Index(fields=["fullname"])
        ] 
        
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
    objects = UserAccountManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    

    def __str__(self):
        return self.fullname





