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


class Transaction(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0.0)
    product_id = models.IntegerField(_('product_id'),default=0.0)
    quantity = models.IntegerField(_('quantity'),default=0.0)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    variant = models.CharField(_('variant'),max_length=255,blank=True,null=True)
    payment_mode = models.CharField(_('payment_mode'),max_length=255,blank=True,null=True)
    address = models.CharField(_('address'),max_length=255,blank=True,null=True)
    contact_number = models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    tracking_id = models.CharField(_('tracking_id'),max_length=255,blank=True,null=True)
    color = models.CharField(_('color'),max_length=255,blank=True,null=True)
    status = models.CharField(_('status'),max_length=255,blank=True,null=True)
    date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
