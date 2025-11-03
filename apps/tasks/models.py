# Python modules + Third party modules

# Django modules
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    TextField,
    IntegerField,
    ForeignKey,
    ManyToManyField,
    UniqueConstraint,
    PROTECT,
    CASCADE,
)
# Project modules
from apps.abstracts.models import AbstractSoftDeletableModel
from settings.base import AUTH_USER_MODEL

class Project(AbstractSoftDeletableModel):
    """
    Project database (table) model.
    """

    NAME_MAX_LEN = 100

    name = CharField(
        max_length=NAME_MAX_LEN,
    )
    author = ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=PROTECT,
        related_name="owned_projects",
    )
    users = ManyToManyField(
        to=AUTH_USER_MODEL,
        blank=True,
        related_name="joined_projects",
    )

    def __str__(self) -> str:
        return self.name
    

class Task(AbstractSoftDeletableModel):
    """
    Task database (table) model.
    """

    NAME_MAX_LEN = 200
    STATUS_TODO = 1
    STATUS_TODO_LABEL = "To Do"
    STATUS_IN_PROGRESS = 2
    STATUS_IN_PROGRESS_LABEL = "In Progress"
    STATUS_DONE = 3
    STATUS_DONE_LABEL = "Done"
    STATUS_CHOICES = (
        (STATUS_TODO, STATUS_TODO_LABEL),
        (STATUS_IN_PROGRESS, STATUS_IN_PROGRESS_LABEL),
        (STATUS_DONE, STATUS_DONE_LABEL),
    )
    
    name = CharField(
        max_length=NAME_MAX_LEN,
        db_index=True,
    )
    description = TextField(
        blank=True,
        default="",
    )
    status = IntegerField(
        default=STATUS_TODO,
        choices=STATUS_CHOICES,
    )
    parent = ForeignKey(
        to="self",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    project = ForeignKey(
        to=Project,
        on_delete=CASCADE,
    )
    assignees = ManyToManyField(
        to=AUTH_USER_MODEL,
        through="UserTask",
        through_fields=("task", "user"),
        blank=True,
    )



class UserTask(AbstractSoftDeletableModel):
    """
    UserTask database (table) model.
    """

    task = ForeignKey(
        to=Task,
        on_delete=CASCADE,
    )
    user = ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=CASCADE,
    )


    class Meta:
        """Customization of the model's meta data."""

        # unique_together = ("task", "user")
        constraints = [
            UniqueConstraint(
                fields=["task", "user"],
                name="unique_task_user",
            ),
        ]
