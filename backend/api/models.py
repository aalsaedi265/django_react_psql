
from django.db import models
from django.contrib.auth.models import User

# orm in django is write model in py and django will convert to right datanase code

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return self.title
    