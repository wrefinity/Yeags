import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import BooleanField, CharField, \
    TextField, UUIDField, CharField, ForeignKey, URLField,\
    JSONField, ImageField, DateTimeField, FilePathField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
User = get_user_model()


class World(models.Model):
    CATEGORY_CHOICES = [
        ("CAT-1", "CAT-1")
    ]
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, blank=True, null=True)
    creator = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uuid = UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    description = TextField(null=False, blank=True)
    thumbnail: ImageField(upload_to='thumbnails/', blank=True, null=True)
    category = CharField(choices=CATEGORY_CHOICES, max_length=50)
    # tags: ManyToManyField(Tag, blank=True)
    visibility = BooleanField(_('visibility'), default=False)
    source_path = FilePathField(path=settings.WORLD_PATH)
    source_url: URLField(max_length=200, blank=True, null=True)
    world_definition: JSONField()
    # agents: ManyToManyField (Agent, blank=True)
    # plan: ForeignKey (WorldPlan, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("worlds:details", kwargs={"uuid": self.uuid})
    
