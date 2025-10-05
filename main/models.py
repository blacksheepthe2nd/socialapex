from django.db import models 
 
class DummyModel(models.Model): 
    name = models.CharField(max_length=100, default="dummy") 
    created_at = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return self.name 
