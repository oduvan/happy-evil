from django.db import models

class Post(models.Model):
    TYPE_TEXT = 1
    TYPE_PHOTO = 2

    TYPE_CHOICES = (
        (TYPE_TEXT, 'text'),
        (TYPE_PHOTO, 'photo')
        )

    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=TYPE_TEXT)
    photo = models.ImageField(blank=True, upload_to='photo')
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    dt_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)