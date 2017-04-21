from django.db import models
from django.contrib.auth.models import Permission

# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)

# def guardar(app_label, model):
#     p = AuthPermission()
#     p.content_type.app_label = app_label
#     p.content_type.model = model
#     p.save()

# class Roles (models.Model):
#     Meta:
#         models = Gr
