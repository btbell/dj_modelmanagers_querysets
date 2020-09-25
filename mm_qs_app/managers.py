from django.db import models

class PostQuerySet(models.QuerySet):
    def smaller_than(self, size):
        return self.filter(comments__lt=size)

    def greater_than(self, size):
        return self.filter(comments__gt=size)

    def get_users_posts(self, username):
        return self.filter(author__username=username)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def smaller_than(self, size):
        return self.filter(comments__lt=size)

    def brians_posts(self):
        return self.get_queryset().get_brians_posts()

