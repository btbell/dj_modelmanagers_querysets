from django.db import models

class PostQuerySet(models.QuerySet):
    def get_users_posts(self, username):
        return self.filter(author__user__username=username)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_users_posts(self, username):
        return self.get_queryset().get_users_posts(username)

