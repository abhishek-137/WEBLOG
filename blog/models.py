from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return f"{self.caption}"

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_author = models.EmailField()

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, verbose_name=("Post author"), on_delete=models.SET_NULL, related_name="posts",null=True)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=50, verbose_name="Post's image")
    post_date = models.DateField(
        auto_now=True, auto_now_add=False, verbose_name="Upload Date and time")
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(verbose_name="Post content", validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag, verbose_name=("post tags"))

    class Meta:
        verbose_name=("Post")
        verbose_name_plural=("Posts")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
