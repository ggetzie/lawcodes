from django.db import models


class CodeLegalText(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=100)
    pd_prom = models.CharField("Place and Date of Promulgation", max_length=200)

    class Meta:
        verbose_name = "Code or Legal Text"

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.long_name


class Manuscript(models.Model):
    code = models.CharField(max_length=5, default="")
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code}: {self.title}"


class Editor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.name


class Translation(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    translator = models.ForeignKey(Editor, on_delete=models.CASCADE)

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.title
