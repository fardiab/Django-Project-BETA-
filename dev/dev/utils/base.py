from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def serialize(self):
        return {
            'id': self.id,
        }

    def save(self, **kwargs):
        super().save(**kwargs)