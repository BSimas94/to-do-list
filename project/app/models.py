from django.db import models

# Create your models here.
class Task(models.Model):
    task_description = models.CharField(max_length=264)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.time_stamp)