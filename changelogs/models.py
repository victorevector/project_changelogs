from django.db import models
from django.template.defaultfilters import slugify

class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Changelog(models.Model):
    project = models.ForeignKey(Project)
    date = models.DateField(help_text='Date: ')
    log = models.TextField(max_length = 2000, help_text='Log:   ')

    def __unicode__(self):
        return self.log
