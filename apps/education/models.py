#Python modules

#Django modules
from django.db.models import Model,DateTimeField,CharField,TextField,BooleanField,ForeignKey,CASCADE,DecimalField,PositiveSmallIntegerField
from django.conf import settings
#Project modules

# Create your models here.
class SoftDeleteModel(Model):
    deleted_at = DateTimeField(null=True,blank=True)
    
    class Meta:
        abstract = True


class Course(SoftDeleteModel):
    MAX_TITLE = 100
    title = CharField(max_length=MAX_TITLE)
    description = TextField(blank=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    owner = ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE,related_name="owned_courses")
    
class Lesson(SoftDeleteModel):
    course = ForeignKey(Course,on_delete=CASCADE,related_name="lessons")
    title = CharField(max_length=200)
    content = TextField()
    order = DecimalField(max_digits=10,decimal_places=2,default=0.0)
    indentation = PositiveSmallIntegerField(default=0)
    is_published = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    