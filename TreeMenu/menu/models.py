from django.db import models


class MenuItem(models.Model):
    name_item = models.CharField(max_length=200)
    higher_level = models.ForeignKey('self', null=True, blank=True, related_name='lower_level',
                                     on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_item
