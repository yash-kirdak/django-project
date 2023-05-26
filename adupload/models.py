from django.db import models
from autoslug import AutoSlugField
class Document(models.Model):
    pdf_title=models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='documents/',max_length=250,null=True,default=None)
    pdf_slug=AutoSlugField(populate_from='pdf_title',unique=True,null=True,default=None)