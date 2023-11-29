# Generated by Django 4.2.7 on 2023-11-28 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categoria", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Produtos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=200, verbose_name="Nome do Produto"),
                ),
                ("marca", models.CharField(max_length=200)),
                ("preco", models.FloatField(verbose_name="Preço do Produto")),
                ("desconto", models.FloatField(blank=True, null=True)),
                (
                    "quantidade",
                    models.IntegerField(verbose_name="Quantidade em estoque"),
                ),
                ("slug", models.SlugField()),
                ("image", models.ImageField(upload_to="static/imgs")),
                (
                    "categoria",
                    models.ForeignKey(
                        default=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produtos.categoria",
                    ),
                ),
            ],
        ),
    ]