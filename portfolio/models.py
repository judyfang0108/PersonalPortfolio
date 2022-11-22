from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib import admin

# Create your models here.


class Project(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    body = models.TextField()
    link = models.CharField(max_length=200, default="NA")

    def __str__(self):
        return self.title


class Counting(models.Model, HitCountMixin):
    # 這個是要教學用的
    description = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=250, unique=True)
    show = models.BooleanField(default=True)
    # 用來記錄觀看次數
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    