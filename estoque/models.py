from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from produto.models import Produto
# Create your models here.

MOVIMENTO=(
    ('e','entrada'),
    ('s','saida')
)

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveBigIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering=('-created',)
    
    def __str__(self):
        return str(self.pk)

class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.pk,self.estoque.pk,self.produto)