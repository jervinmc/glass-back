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


class Product(models.Model):
    request_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    quantity = models.IntegerField(_('quantity'),default=0.0)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    product_name=models.CharField(_('product_name'),max_length=255,blank=True,null=True)
    description=models.CharField(_('description'),max_length=255,blank=True,null=True)
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    image1 = models.ImageField(
        _('image1'), upload_to=nameFile, default="uploads/users_placeholder.png")
    image2 = models.ImageField(
        _('image2'), upload_to=nameFile, default="uploads/users_placeholder.png")
    image3 = models.ImageField(
        _('image3'), upload_to=nameFile, default="uploads/users_placeholder.png")
    image4 = models.ImageField(
        _('image4'), upload_to=nameFile, default="uploads/users_placeholder.png")
    class Meta:
        ordering = ["-id"]
