from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


class Tag(models.Model):
    caption = models.CharField(max_length=100)
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="", max_length=100, null=False)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)