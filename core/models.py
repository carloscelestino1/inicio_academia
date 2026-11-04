from django.db import models


class Aluno(models.Model):
    nome = models.CharField("nome completo", max_length=150)
    cpf = models.CharField("CPF", max_length=14, unique=True, blank=True, null=True)
    email = models.EmailField("e-mail", blank=True)
    telefone = models.CharField("telefone", max_length=20, blank=True)
    data_nascimento = models.DateField("data de nascimento", blank=True, null=True)
    ativo = models.BooleanField("ativo", default=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "aluno"
        verbose_name_plural = "alunos"

    def __str__(self):
        return self.nome


class Plano(models.Model):
    nome = models.CharField("nome", max_length=100, unique=True)
    descricao = models.TextField("descrição", blank=True)
    duracao_dias = models.PositiveIntegerField("duração em dias", default=30)
    preco = models.DecimalField("preço", max_digits=8, decimal_places=2)
    ativo = models.BooleanField("ativo", default=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "plano"
        verbose_name_plural = "planos"

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    class Status(models.TextChoices):
        ATIVA = "ativa", "Ativa"
        ENCERRADA = "encerrada", "Encerrada"
        CANCELADA = "cancelada", "Cancelada"
        TRANCADA = "trancada", "Trancada"

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        related_name="matriculas",
        verbose_name="aluno",
    )
    plano = models.ForeignKey(
        Plano,
        on_delete=models.PROTECT,
        related_name="matriculas",
        verbose_name="plano",
    )
    data_inicio = models.DateField("data de início")
    data_fim = models.DateField("data de término", blank=True, null=True)
    status = models.CharField(
        "status",
        max_length=10,
        choices=Status.choices,
        default=Status.ATIVA,
    )
    observacoes = models.TextField("observações", blank=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["-data_inicio"]
        verbose_name = "matrícula"
        verbose_name_plural = "matrículas"

    def __str__(self):
        return f"{self.aluno} — {self.plano}"


class Pagamento(models.Model):
    class Status(models.TextChoices):
        PENDENTE = "pendente", "Pendente"
        PAGO = "pago", "Pago"
        ATRASADO = "atrasado", "Atrasado"
        CANCELADO = "cancelado", "Cancelado"

    class FormaPagamento(models.TextChoices):
        DINHEIRO = "dinheiro", "Dinheiro"
        CARTAO = "cartao", "Cartão"
        PIX = "pix", "Pix"
        TRANSFERENCIA = "transferencia", "Transferência"
        OUTRA = "outra", "Outra"

    matricula = models.ForeignKey(
        Matricula,
        on_delete=models.PROTECT,
        related_name="pagamentos",
        verbose_name="matrícula",
    )
    valor = models.DecimalField("valor", max_digits=8, decimal_places=2)
    data_vencimento = models.DateField("data de vencimento")
    data_pagamento = models.DateField("data do pagamento", blank=True, null=True)
    forma_pagamento = models.CharField(
        "forma de pagamento",
        max_length=15,
        choices=FormaPagamento.choices,
        blank=True,
    )
    status = models.CharField(
        "status",
        max_length=10,
        choices=Status.choices,
        default=Status.PENDENTE,
    )
    observacoes = models.TextField("observações", blank=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["data_vencimento"]
        verbose_name = "pagamento"
        verbose_name_plural = "pagamentos"

    def __str__(self):
        return f"{self.matricula.aluno} — R$ {self.valor}"
