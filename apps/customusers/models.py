#Python Modules

#Django Modules
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models import EmailField,CharField,BooleanField,DateTimeField
from django.utils import timezone
#Project Modules

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email=email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields): 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        

class CustomUser(AbstractBaseUser,PermissionsMixin):
    """
    Custom user model extending AbstractBaseUser.
    """
    EMAIL_MAX_LENGTH = 150
    NAME_MAX_LENGTH = 50
    first_name = CharField(max_length=NAME_MAX_LENGTH,blank=True)
    last_name = CharField(max_length=NAME_MAX_LENGTH,blank=True)
    email = EmailField(max_length=EMAIL_MAX_LENGTH,unique=True)
    is_active = BooleanField(
        default=True,
        help_text=
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts.",
        )
    is_staff = BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
        )
    
    date_joined = DateTimeField(default=timezone.now)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
       return self.email