from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Quote(models.Model):
    fullname=models.CharField(_('fullname'),max_length=255,blank=True,null=True)
    message=models.CharField(_('message'),max_length=255,blank=True,null=True)
    product_name=models.CharField(_('product_name'),max_length=255,blank=True,null=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    date_created=models.DateTimeField(_('date_created'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
