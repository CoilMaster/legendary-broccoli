from django.db import models

# Create your models here.

class Category(MPTTModel):
    class Meta:
        verbose_name = "Kategorie grzałek"
        verbose_name_plural = "Kategorie grzałek"

    name = model.Charfield(max_length=40, null=True, vorbose_name="Kategorie grzałek")

    def __str__(self):
        return self.name

class Coil(models.Model):
    class Meta:
        verbose_name = "Grzałki"
        verbose_name_plural = "Grzałki"

    name = model.Charfield(max_length=40, null=True, vorbose_name="Nazwa")
    category = model.TreeForeignKey(Category,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='product_set',
                              verbose_name="Kategoria")
    spiral = model.IntegerField(verbose_name="Ilość zwoji")


    def __str__(self):
        return self.name
