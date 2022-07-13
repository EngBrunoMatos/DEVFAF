from account.models import User
from basedados.models import tb_equipo_ressarc
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime

class tb_analise(models.Model):
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT, null=True)
    FK_User = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    ds_gestor = models.CharField(max_length=100, null=True) #gestor estará logado
    ds_prazo = models.BigIntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now, null=True)
    dt_finalizacao = models.DateTimeField(blank=True,null=True,)

class tb_reg_acompanhamento(models.Model):
    FK_tb_analise = models.ForeignKey(tb_analise, on_delete=models.PROTECT, null=True)
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT, null=True)
    cancelar_registro = models.BooleanField(default=False, blank=True)
    registro_cancelamento = models.CharField(max_length=200, blank=True)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    PENDENTE_ANALISE = 'Pendente de Análise'
    EM_ANALISE = 'Em Análise'
    ADMINISTRATIVAS_COBRANCA = 'Medidas Administrativas de Cobrança'
    RECURSOS_RESTITUIDOS = 'Recursos restituídos'
    SEM_CONSTATACAO_DEBITO = 'Sem constatação de débito'
    PARCELAMENTO_DEBITOS = 'Em parcelamento de débitos'
    INSTRUCAO_TCE = 'Em instrução para TCE'
    CADASTRO_DEBITOS_INFERIORES = 'Em instrução de cadastro de Débitos Inferiores'
    INSTAURACAO_TCE = 'Enviado para Instauração de TCE'
    opcoes_situacao = [(PENDENTE_ANALISE, 'Pendente de Análise'), (EM_ANALISE, 'Em Análise'),
                       (ADMINISTRATIVAS_COBRANCA, 'Medidas Administrativas de Cobrança'),
                       (RECURSOS_RESTITUIDOS, 'Recursos restituídos'),
                       (SEM_CONSTATACAO_DEBITO, 'Sem constatação de débito'),
                       (PARCELAMENTO_DEBITOS, 'Em parcelamento de débitos'),
                       (INSTRUCAO_TCE, 'Em instrução para TCE'),
                       (CADASTRO_DEBITOS_INFERIORES, 'Em instrução de cadastro de Débitos Inferiores'),
                       (INSTAURACAO_TCE, 'Enviado para Instauração de TCE'), ]
    status_situacao = models.CharField(max_length=46,
                                       choices=opcoes_situacao,
                                       verbose_name="Situação da Devolução",blank=True,null=True,)
    PREJUIZO_ERARIO = 'Dano ou prejuízo ao Erário'
    DESVIO_FINALIDADE = 'Desvio de Finalidade'
    DESVIO_OBJETO = 'Desvio do Objeto'
    RECEBIMENTO_IRREGULAR = 'Recebimento Irregular'
    opcoes_irregularidade = [(PREJUIZO_ERARIO, 'Dano ou prejuízo ao Erário'),
                             (DESVIO_FINALIDADE, 'Desvio de Finalidade'),
                             (DESVIO_OBJETO, 'Desvio do Objeto'),
                             (RECEBIMENTO_IRREGULAR, 'Recebimento Irregular')]
    tipo_irregularidade = models.CharField(max_length=26,
                                           choices=opcoes_irregularidade,
                                           verbose_name="Tipo de Irregularidade",blank=True,null=True,)
    TCE_INSTAURADA = 'TCE Instaurada'
    JULGADO_REGULAR_TCU = 'Julgado Regular – TCU'
    JULGADO_IRREGULAR_TCU = 'Julgado Irregular – TCU'
    ARQUIVADO_TCU = 'Arquivado – TCU'
    QUITADO_AGU = 'Quitado – AGU'
    ARQUIVADOR_AGU = 'Arquivado - AGU'
    CDI = 'Cadastro de Débitos Inferiores - CDI'
    CDI_MEDIDAS_JUDICIAIS = 'CDI – Enviado para medidas judiciais'
    COBRANCA_JUDICIAL = 'Em cobrança judicial'
    opcoes_instrucao = [(TCE_INSTAURADA, 'TCE Instaurada'), (JULGADO_REGULAR_TCU, 'Julgado Regular – TCU'),
                        (JULGADO_IRREGULAR_TCU, 'Julgado Irregular – TCU'), (ARQUIVADO_TCU, 'Arquivado – TCU'),
                        (QUITADO_AGU, 'Quitado – AGU'), (ARQUIVADOR_AGU, 'Arquivado - AGU'),
                        (CDI, 'Cadastro de Débitos Inferiores - CDI'),
                        (CDI_MEDIDAS_JUDICIAIS, 'CDI – Enviado para medidas judiciais'),
                        (COBRANCA_JUDICIAL, 'Em cobrança judicial')]
    status_instrucao = models.CharField(max_length=36,
                                       choices=opcoes_instrucao,
                                       verbose_name="Status da Instrução",blank=True,null=True,)
    entidade_autora = models.CharField(max_length=100, verbose_name='Entidade Auditora',blank=True,null=True,)
    nup_rel_auditoria = models.CharField(max_length=12, verbose_name='NUP Relatório de Auditoria',blank=True,null=True,)
    motivo_analise = models.CharField(max_length=540, verbose_name="Motivo do Ressarcimento:",blank=True,null=True,)
    SIM = 'S'
    NAO = 'N'
    opcoes_auditado = [(SIM, 'Sim'), (NAO, 'Não'), ]
    analise_auditada = models.CharField(max_length=1,
                                        choices=opcoes_auditado,
                                        verbose_name="Proposta Auditada?",
                                        blank=True,
                                        null=True,)
    SIM = 'S'
    NAO = 'N'
    opcoes_prt_cancelamento = [(SIM, 'Sim'), (NAO, 'Não'), ]
    prt_cancelamento = models.CharField(max_length=1,
                                        choices=opcoes_prt_cancelamento,
                                        verbose_name="Possui Portaria de Cancelamento?",
                                        blank=True,
                                        null=True,)

class tb_reg_restituicao(models.Model):
    FK_tb_analise = models.ForeignKey(tb_analise, on_delete=models.PROTECT, null=True)
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT, null=True)
    cancelar_registro = models.BooleanField(default=False, blank=True)
    registro_cancelamento = models.CharField(max_length=200, blank=True)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    nr_gru = models.BigIntegerField()
    vl_restituido = models.FloatField()
    dt_restituicao = models.DateField()
    nr_cpf_cnpj = models.BigIntegerField()
    ds_razao_social = models.CharField(max_length=100)

class tb_reg_edital_notif(models.Model):
    FK_tb_analise = models.ForeignKey(tb_analise, on_delete=models.PROTECT)
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT)
    cancelar_registro = models.BooleanField(default=False, blank=True)
    registro_cancelamento = models.CharField(max_length=200, blank=True)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    nr_edital = models.BigIntegerField()
    dt_edital = models.DateField()
    dt_publicacao = models.DateField()
    nr_cpf_cnpj = models.BigIntegerField()
    ds_razao_social = models.CharField(max_length=100)

class tb_reg_notificacao(models.Model):
    FK_tb_analise = models.ForeignKey(tb_analise, on_delete=models.PROTECT, null=True)
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT, null=True)
    cancelar_registro = models.BooleanField(default=False, blank=True)
    registro_cancelamento = models.CharField(max_length=200, blank=True)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    nr_nup_oficio = models.BigIntegerField()
    dt_ar = models.DateField()
    dt_limite_notificacao = models.DateField()
    nr_cpf_cnpj = models.BigIntegerField()
    ds_razao_social = models.CharField(max_length=100)
    Enviada = 'E'
    Notificada = 'N'
    Respondida = 'R'
    opcoes_notificacao = [(Enviada, 'Enviada'), (Notificada, 'Notificado não encontrado'),(Respondida, 'Respondida'),]
    notificacao = models.CharField(max_length=1, choices=opcoes_notificacao)
    SIM = 'S'
    NAO = 'N'
    opcoes_resp_irregularidade = [(SIM, 'Sim'), (NAO, 'Não'),]
    resp_irregularidade = models.CharField(max_length=1,choices=opcoes_resp_irregularidade)

class tb_reg_fatos_geradores(models.Model):
    FK_tb_analise = models.ForeignKey(tb_analise, on_delete=models.PROTECT, null=True)
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT, null=True)
    cancelar_registro = models.BooleanField(default=False, blank=True)
    registro_cancelamento = models.CharField(max_length=200, blank=True)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    tp_irregularidade = models.CharField(max_length=100)
    SOLIDARIA = 'S'
    opcoes_responsabilidade = [(SOLIDARIA, 'Solidária'),]
    tp_responsabilidade = models.CharField(max_length=1,choices=opcoes_responsabilidade)
    vl_dano = models.FloatField()
    dt_fato_gerador = models.DateField()
    nr_cpf_cnpj = models.BigIntegerField()
    ds_razao_social = models.CharField(max_length=100)
class tb_reg_valores(models.Model):
    FK_tb_analise = models.ForeignKey(tb_analise, on_delete=models.PROTECT, null=True)
    FK_tb_equipo_ressarc = models.ForeignKey(tb_equipo_ressarc, on_delete=models.PROTECT, null=True)
    cancelar_registro = models.BooleanField(default=False, blank=True)
    registro_cancelamento = models.CharField(max_length=200, blank=True)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    vl_original = models.FloatField()
    vl_correcao = models.FloatField()
    dt_apuracao = models.DateField()