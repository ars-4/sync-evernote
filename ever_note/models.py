from django.db import models

# Create your models here.

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(BaseModel):
    username = models.CharField(max_length=244, null=True, default='Guest')
    title = models.TextField(null=True)

    def __str__(self):
        return self.username
