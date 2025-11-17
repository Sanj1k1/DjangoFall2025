#Python modules
from typing import Any
from faker import Faker
from random import randint,choice
from datetime import datetime

#Django modules
from django.core.management.base import BaseCommand
from django.db.models import QuerySet
from django.utils import timezone
from django.db import connection
#Project modules
from apps.customusers.models import CustomUser

class Command(BaseCommand):
    help = "Generate CustomUser data for testing purposes."
    
    def reset_user_id_sequence(self):
        """Сброс автоинкремента ID (SQLite)."""
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='users_user';")

    
    def __generate_users(self,user_count:int=100)->None:
        fake = Faker("en_US")
        
        CustomUser.objects.all().delete()
        self.reset_user_id_sequence()
        
        created_users = []
        departments = ["IT", "HR", "Sales", "Finance"]
        roles = ["admin", "manager", "employee"]
        batch_size = 1000
        users_before = CustomUser.objects.count()
        
        for i in range(1,user_count+1):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = f"{first_name.lower()[0]}.{last_name.lower()}{i}@example.com"
            phone = f"+7{randint(7000000000, 7999999999)}"
            city = fake.city()
            country = fake.country()
            department = choice(departments)
            role = choice(roles)
            birth_date = fake.date_of_birth(minimum_age=18,maximum_age=50)
            user = CustomUser(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=email.split('@')[0],
                    phone=phone,
                    city=city,
                    country=country,
                    department=department,
                    role=role,
                    birth_date=birth_date,
                    is_active=True,
                    is_staff=(role=="admin"),
            )
            user.set_password("12345")
            created_users.append(user)
            
            if len(created_users) >= batch_size:
                CustomUser.objects.bulk_create(created_users)
                created_users = []
                self.stdout.write(f"{i} users created...")
        
        if created_users:
            CustomUser.objects.bulk_create(created_users)
            
        self.stdout.write(self.style.SUCCESS(f"Successfully created {user_count} users."))
         

    def handle(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        start_time = datetime.now()
        self.__generate_users()
        self.stdout.write(
            self.style.SUCCESS(f"Process finished in {(datetime.now() - start_time).total_seconds()} seconds")
        )
