from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=264)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("to_do:list")
