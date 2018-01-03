from django.db import models


def category_directory_path(instance, filename):
    """Upload path for a given photo's category."""
    return f"{instance.category.name}/{filename}"

class Photo(models.Model):
    """The model for individual photos."""

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')
    description
    date_uploaded
    date_published
    date_modified
    featured
    order
