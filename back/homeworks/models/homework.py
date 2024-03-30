from django.db import models

from typing import Final

from users.models import Usuario


# Lookup table
TIPO_TRABALHO: Final[dict[int, str]] = {
    1: "Apresentação",
    2: "Prova",
    3: "Tarefa"
}


class Homework(models.Model):
    class TipoTrabalho(models.IntegerChoices):
        APRESENTACAO = 1, "Apresentação"
        PROVA = 2, "Prova"
        TAREFA = 3, "Tarefa"

    nome_trabalho = models.CharField("Nome do trabalho",
                                     max_length=50, blank=False, null=False)
    materia_trabalho = models.CharField("Matéria do trabalho",
                                        max_length=50, blank=True, null=True)
    tipo_trabalho = models.IntegerField("Tipo do trabalho",
                                        choices=TipoTrabalho.choices,
                                        blank=False, null=False,
                                        default=TipoTrabalho.TAREFA)
    anotacoes = models.TextField("Anotações",
                                 max_length=100, blank=True, null=True)
    data_entrega = models.DateField("Data de entrega",
                                    blank=False, null=False)
    # usuario = models.ForeignKey(Usuario)

    def __str__(self) -> str:
        return f"""[{self.data_entrega}] {self.materia_trabalho}:
                    {self.nome_trabalho}"""
