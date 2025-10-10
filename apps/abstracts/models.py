#Python modules
from datetime import datetime,timezone
#Django modules 
from django.db.models import Model,DateTimeField
from django.utils import timezone as djnago_timezone

class AbstractBaseModel(Model):
    """
    Abstract base model with common fields.
    """
    
    created_at = DateTimeField(
        auto_now_add=True
    )
    updated_at = DateTimeField(
        auto_now=True
    )
    deleted_at = DateTimeField(
        null=True,
        blank=True,
    )
    
    class Meta:
        """ Meta class for AbstractBaseModel."""
        abstract = True #Почему он видит его при миграции
        
    def delete(self,*args,**kwargs)->None:
        #self.deleted_at = datetime.now(timezone.utc) #Purely python way
        self.deleted_at = djnago_timezone.now()
        self.save(update_fields=["deleted_at"])
        
