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


class Size(models.Model):
    product_id = models.IntegerField(_('product_id'),default=0.0)
    size=models.CharField(_('size'),max_length=255,blank=True,null=True)
    color=models.CharField(_('color'),max_length=255,blank=True,null=True)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
