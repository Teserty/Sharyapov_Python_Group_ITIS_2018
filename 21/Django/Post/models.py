from django.db import models
from django.utils import timezone
import re

regex = r'#[a-zA-Zа-яА-Я0-9]+[a-zA-Zа-яА-Я0-9]*'


class HashTag(models.Model):
    title = models.TextField()

    def create(self, text):
        self.title = text
        self.save()


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    tags = models.ManyToManyField(HashTag)

    def tagF(self):
        tags = re.findall(regex, self.text)
        savedTags = HashTag.objects.all()
        for tag in tags:
            if tag not in savedTags:
                HashTag.create(tag)
            self.tags.add(HashTag.objects.filter(title=tag))

    def publish(self):
        self.tagF()
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

