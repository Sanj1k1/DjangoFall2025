#Python modules
from typing import Any
from random import choice,choices,sample
from datetime import datetime,timedelta
#Django modules
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import QuerySet
#Python modules
from apps.tasks.models import Task,Project,UserTask

class Command(BaseCommand):
    help = "Generate tasks data for testing purposes"   
    
    EMAIL_DOMAINS = (
        "example.com",
        "test.com",
        "sample.org",
        "demo.net",
        "mail.com",
    )
    
    SOME_WORDS = (
        "lorem",
        "ipsum",
        "dolor",
        "sit",
        "amet",
        "elit",
        "do",
        "eiusmod",
        "ut",
        "tempor"
    )
    
    TASKS = {
        "update model": "Update the existing Django model to include new fields and relationships.",
        "delete model": "Remove outdated models that are no longer used in the project.",
        "create model": "Create a new model for managing project-related data.",
        "fix bug": "Fix a critical bug in the task assignment module.",
        "add new feature": "Develop a new feature for user activity tracking.",
        "optimize query": "Optimize database queries to reduce response time.",
        "improve UI design": "Enhance the front-end interface for better user experience.",
        "refactor code": "Refactor legacy code to improve readability and maintainability.",
        "write unit tests": "Write unit tests for the task management API.",
        "update documentation": "Update project documentation to reflect recent changes.",
        "setup CI/CD pipeline": "Set up continuous integration and deployment pipeline.",
        "migrate database": "Perform database migrations for the new schema updates.",
        "add API endpoint": "Add a REST API endpoint for fetching project details.",
        "implement authentication": "Implement authentication using Django Rest Framework JWT.",
        "integrate third-party service": "Integrate an external email service for notifications.",
        "resolve merge conflicts": "Resolve merge conflicts during the last code integration.",
        "review pull request": "Review code from team members before merging into main.",
        "improve performance": "Improve system performance by caching frequent queries.",
        "update dependencies": "Upgrade dependencies to the latest stable versions.",
        "fix styling issues": "Fix visual inconsistencies in the task management UI.",
        "deploy to production": "Deploy the latest version of the app to the production server.",
        "analyze logs": "Analyze server logs to identify potential issues.",
        "update README file": "Update the README with setup instructions and usage examples.",
        "add pagination": "Add pagination support to the project list API.",
        "implement search feature": "Implement search functionality for tasks and projects.",
        "create admin dashboard": "Build a custom admin dashboard for managers.",
        "design database schema": "Design and document the initial database schema.",
        "add notifications system": "Add user notification system via email and dashboard alerts.",
        "handle edge cases": "Handle edge cases for invalid user input or missing data."
    }

    
    def __generate_usertasks(self, min_assignees: int = 1, max_assignees: int = 3) -> None:
        """
        Generates UserTasks.
        """
        existed_tasks = list(Task.objects.select_related("project"))
        created_relations = []
        
        for task in existed_tasks:
            project_users = list(task.project.users.all())
        
        assignees = sample(
            project_users,
            k=min(max_assignees, len(project_users))
        )
        
        for user in assignees:
            created_relations.append(UserTask(task=task, user=user))
        
        UserTask.objects.bulk_create(created_relations, ignore_conflicts=True)
        
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(created_relations)} user-task relations."
            )
        )
        
    
    def __generate_tasks(self,tasks_count:int =100) -> None:
        """
        Generates Tasks for testing purposes.
        """
        create_tasks:list[Task] = []
        tasks_before:int = Task.objects.count()
        existed_projects:QuerySet[Project] = Project.objects.all()
        
        i: int
        
        for i in range(tasks_count):
            name: str = f"{choice(list(self.TASKS.keys()))} #{i+1}"
            status:int = choice([1,2,3])
            description: str = self.TASKS[name.split(" #")[0]] if status == 3 else ""
            
            project:Project = choice(existed_projects)
            create_tasks.append(
                Task(
                    name=name,
                    status=status,
                    description=description,
                    project = project,
                )
            )
        
        Task.objects.bulk_create(create_tasks,ignore_conflicts=True)
        tasks_after:int = Task.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {tasks_after - tasks_before} tasks."
            )
        )
        
    
    def __generate_users(self,user_count:int = 100)->None:
        """
        Generates users for testing purposes.
        """
        
        USER_PASSWORD = make_password(password="12345")
        created_users = []
        users_before:int = User.objects.count()
        i:int
        for i in range(user_count):
            username:str = f"user {i+1}"
            email:str = f"user{i+1}@{choice(self.EMAIL_DOMAINS)}"
            created_users.append(
                User(
                    username = username,
                    email = email,
                    password = USER_PASSWORD,
                )
            )
        
        User.objects.bulk_create(created_users,ignore_conflicts=True)
        users_after:int = User.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {users_after - users_before} users."
            )
        )
                    
    def __generate_projects(self, project_count: int = 100) -> None:
        """
        Generates projects for testing purposes.
        """

        create_projects: list[Project] = []
        projects_before: int = Project.objects.count()
        existed_users: QuerySet[User] = User.objects.all()

        i: int
        for i in range(project_count):
            name: str = " ".join(choices(self.SOME_WORDS, k=4)).capitalize()
            author: User = choice(existed_users)
            create_projects.append(
                Project(
                    name=name,
                    author=author
                )
            )
        Project.objects.bulk_create(create_projects, ignore_conflicts=True)

        project: Project
        for project in Project.objects.all():
            project.users.add(*choices(existed_users, k=10))

        projects_after: int = Project.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {projects_after - projects_before} projects."
            )
        )
        

    def handle(self,*args,**kwargs)->None:
        """Command entry point."""
        start_time:datetime = datetime.now()
        self.__generate_users(user_count=20)
        self.__generate_projects(project_count=20)
        self.__generate_tasks(tasks_count=60)
        self.__generate_usertasks(min_assignees=1, max_assignees=3)
        
        print(
            "Synthetic local data generation took: {} seconds".format(
                (datetime.now() - start_time).total_seconds()
            )
        )
        