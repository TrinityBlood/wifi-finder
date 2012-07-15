from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'posts'
