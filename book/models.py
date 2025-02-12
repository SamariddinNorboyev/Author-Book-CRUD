from django.db import models
# Create your models here.[]


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Author"
        ordering = ["-created_at"]


class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Book"
        ordering = ["-created_at"]
