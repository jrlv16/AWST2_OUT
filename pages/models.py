from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/uploads')

# revoir foncion sur crash course


class Page(models.Model):

        title = models.CharField(max_length = 60)
        permalink = models.CharField(max_length = 12, unique = True)
        bodytext = models.TextField('Page Content', blank = True)
        
        def page(self):
            return self.Page()
      