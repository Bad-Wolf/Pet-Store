from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.user}'


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    cover_image_url = models.URLField(blank=True,
                      default='https://islandpress.org/sites/default/files/400px%20x%20600px-r01BookNotPictured.jpg')
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author}'