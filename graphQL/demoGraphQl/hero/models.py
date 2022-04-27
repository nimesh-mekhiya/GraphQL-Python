from django.db import models

class FileUploadV2(models.Model):
    document = models.TextField()