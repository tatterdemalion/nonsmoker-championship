from django.db import models


class NonSmoker(models.Model):
    name = models.CharField(max_length=255)
    quit_date = models.DateTimeField(auto_now_add=True)
    quit_date.editable = True

    def __str__(self):
        return f'{self.name} - {self.quit_date.isoformat()}'

    class Meta:
       ordering = ['quit_date']
