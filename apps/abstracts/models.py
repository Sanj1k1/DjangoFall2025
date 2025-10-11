#Python modules
from datetime import datetime,timezone
#Django modules 
from django.db.models import Model,DateTimeField,BooleanField
from django.utils import timezone as djnago_timezone

class AbstractSoftDeletableModel(Model):
    """
    Abstract Soft Delete model with commond fields.
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
    
    is_deleted = BooleanField(
        default=False
    )
    
    class Meta:
        """Meta class for AbstractSoftDelete model"""
        abstract = True
    
    def soft_delete(self,*args,**kwargs)->None:
        if not self.is_deleted:
            self.is_deleted = True
            self.deleted_at = djnago_timezone.now()
            self.save(update_fields=["is_deleted","deleted_at"])
            
    def restore(self,*args,**kwargs)->None:
        if self.is_deleted:
            self.is_deleted = True
            self.deleted_at = None
    
    def hard_delete(self,*args,**kwargs)->None:
        self.deleted_at = djnago_timezone.now()
        self.save(update_fields=["deleted_at"])