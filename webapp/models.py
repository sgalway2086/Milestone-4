from django.db import models

# Create your models here.
class Posts(models.Model):
    poster_username = models.CharField(max_length=20, null=False, blank=False)
    post_name = models.CharField(max_length=60, null=False, blank=False)
    post_content = models.TextField(null=False, blank=False)
    post_comments = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
