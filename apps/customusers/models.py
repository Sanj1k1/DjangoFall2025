#Python Modules

#Django Modules
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models import EmailField,CharField,BooleanField,DateTimeField,DateField,DecimalField
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
        extra_fields.setdefault('is_active',True)        
        return self.create_user(email, password, **extra_fields)
        

class CustomUser(AbstractBaseUser,PermissionsMixin):
    """
    Custom user model extending AbstractBaseUser.
    """
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]
    
    EMAIL_MAX_LENGTH = 150
    NAME_MAX_LENGTH = 50
    
    first_name = CharField(max_length=NAME_MAX_LENGTH,blank=True)
    last_name = CharField(max_length=NAME_MAX_LENGTH,blank=True)
    email = EmailField(max_length=EMAIL_MAX_LENGTH,unique=True)
    username = CharField(max_length=NAME_MAX_LENGTH,blank=True)
    phone = CharField(max_length=20,blank=True,null=True)
    city = CharField(max_length=100, blank=True, null=True)
    country = CharField(max_length=100, blank=True, null=True)
    department =CharField(max_length=50, blank=True, null=True)
    role =CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    birth_date = DateField(blank=True, null=True)
    salary = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
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
    last_login = DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
       return self.email