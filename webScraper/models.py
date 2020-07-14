from django.db import models
from django.utils import timezone

class Offre(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_link = models.CharField(max_length=1000)
    jobboard = models.CharField(max_length=200, default='null for now')
    created_date = models.DateTimeField(default=timezone.now)
    
    class Admin:
        pass
    
    def __str__(self):
        return self.job_title
    
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['job_link'], name='unique job posting')
            ]

# Create your models here.
