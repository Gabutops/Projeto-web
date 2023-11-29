from django.db import models

# Create your models here.


class Categoria(models.Model):
    categoria = models.CharField( max_length=200)

    def __str__(self) -> str:
        return self.categoria
    

class Produtos(models.Model):
    nome = models.CharField(verbose_name= 'Nome do Produto', max_length= 200)
    marca = models.CharField(max_length=200)
    preco = models.FloatField(verbose_name= 'Preço do Produto')
    desconto = models.FloatField(blank=True, null=True)
    quantidade = models.IntegerField('Quantidade em estoque')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=False, null=True)
    image = models.ImageField(upload_to = 'imgs/produtos')

    def __str__(self):
        return self.nome