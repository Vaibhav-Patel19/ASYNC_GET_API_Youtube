from django.db import models


class video(models.Model):
    index = models.IntegerField()
    channel_title = models.CharField(max_length = 200, null=True, blank=True)
    video_title = models.CharField(max_length = 200)
    video_description = models.TextField()
    date_time = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.video_title
