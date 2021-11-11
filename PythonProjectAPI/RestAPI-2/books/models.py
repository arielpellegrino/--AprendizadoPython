from django.db import models

# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=true, default=uuid4, editable=false)
    title = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    release_year = models.integerField()
    state = model.CharField(max_lenght=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=true)
