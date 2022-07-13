from django.db import models
from datetime import datetime, date
from django.db.models import Q
from dateutil.relativedelta import relativedelta

class tb_equipo_saldo(models.Model):
    ano = models.CharField(max_length=100)
    nr_proposta = models.CharField(max_length=100)
    tipo_saldo = models.CharField(max_length=100)
    rotulo_conta = models.CharField(max_length=100)
    banco_prop = models.CharField(max_length=100)
    agencia_prop = models.CharField(max_length=100)
    conta_prop = models.CharField(max_length=100)
    dt_ult_pgto_prop = models.CharField(max_length=100)
    dt_saldo_prop = models.CharField(max_length=100)
    ds_secretaria = models.CharField(max_length=100)
    vl_saldo_conta = models.CharField(max_length=100)
class tb_equipo_ob_parc(models.Model):
    nr_proposta = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    tipo_ob = models.CharField(max_length=100)
    ds_situacao_proposta = models.CharField(max_length=100)
    ano_emissao_ob = models.CharField(max_length=100)
    nu_ob_siafi = models.CharField(max_length=100)
    dt_ob_siafi = models.CharField(max_length=100)
    vl_pago_ob_prop = models.CharField(max_length=100)
class tb_area_finalistica(models.Model):
    area_finalistica = models.CharField(max_length=100)
class tb_recebedor(models.Model):
    cnpj_recebedor = models.CharField(max_length=100)
    razao_social_recebedor= models.CharField(max_length=100)
class tb_uf(models.Model):
    uf = models.CharField(max_length=100)
class tb_esfera(models.Model):
    esfera = models.CharField(max_length=100)
class tb_municipio(models.Model):
    codigo_municipio= models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
class tb_tipo_objeto(models.Model):
    tipo_objeto = models.CharField(max_length=100)
class tb_equipo_ressarc(models.Model):
    nr_proposta = models.CharField(max_length=100, primary_key=True)

    PORTARIA_CANCELAMENTO = models.CharField(max_length=100)
    DT_PORTARIA_CANCELAMENTO = models.CharField(max_length=100)

    tipo_de_transferencia = models.CharField(max_length=100)
    nr_portaria_habilitacao = models.CharField(max_length=100)
    ano_portaria_habilitacao = models.CharField(max_length=100)
    data_portaria_habilitacao = models.CharField(max_length=100)
    valor_proposta = models.CharField(max_length=100)
    valor_transferido = models.CharField(max_length=100)
    valor_nao_transferido = models.CharField(max_length=100)
    FK_uf = models.ForeignKey(tb_uf, on_delete=models.PROTECT, null=True)
    FK_municipio = models.ForeignKey(tb_municipio, on_delete=models.PROTECT, null=True)
    FK_esfera = models.ForeignKey(tb_esfera, on_delete=models.PROTECT, null=True)
    FK_area_finalistica = models.ForeignKey(tb_area_finalistica, on_delete=models.PROTECT, null=True)
    FK_tipo_objeto = models.ForeignKey(tb_tipo_objeto, on_delete=models.PROTECT, null=True)
    FK_recebedor = models.ForeignKey(tb_recebedor, on_delete=models.PROTECT, null=True)
    def risco_calculado(self):
        R_Pre = date.today().year - datetime.strptime(self.data_portaria_habilitacao, "%d/%m/%Y").date().year
        if R_Pre <= 5:
            R_Pre = 1
        elif R_Pre == 6:
            R_Pre = 2
        elif R_Pre == 7:
            R_Pre = 4
        elif R_Pre == 8:
            R_Pre = 6
        elif R_Pre == 9:
            R_Pre = 8
        elif R_Pre == 10:
            R_Pre = 10
        else:
            R_Pre = 12
        R_Mat = float(self.valor_transferido.replace(',', '.'))
        if R_Mat <= 1000:
            R_Mat = 1
        elif R_Mat <= 10000:
            R_Mat = 2
        elif R_Mat <= 100000:
            R_Mat = 3
        elif R_Mat <= 2000000:
            R_Mat = 4
        elif R_Mat <= 5000000:
            R_Mat = 5
        else:
            R_Mat = 6
        return R_Pre + R_Mat
    risco = property(risco_calculado)
    def Plano(self):
        dataFormatada = datetime.strptime(self.data_portaria_habilitacao, "%d/%m/%Y").date()
        if dataFormatada <= datetime.strptime("31/12/2016", "%d/%m/%Y").date():
            return "Plano 1"
        if datetime.strptime("01/01/2017", "%d/%m/%Y").date() <= dataFormatada <= datetime.strptime("30/06/2021",
                                                                                                    "%d/%m/%Y").date():
            return "Plano 2"
        else:
            return "Outro Plano"
    plano = property(Plano)
    def saldo_conta(self):
        return tb_equipo_saldo.objects.filter(Q(nr_proposta=self.nr_proposta)).last()
    saldo = property(saldo_conta)
    def situacao_calculada(self):
        lista_ob_primeira = tb_equipo_ob_parc.objects.filter(Q(nr_proposta=self.nr_proposta)).first()
        data_ob_primeira = datetime.strptime(lista_ob_primeira.dt_ob_siafi, "%d/%m/%Y").date()
        saldo_em_conta = tb_equipo_saldo.objects.filter(Q(nr_proposta=self.nr_proposta)).first()
        hoje_24M = date.today() - relativedelta(months=24)
        if self.PORTARIA_CANCELAMENTO:
            situacao = 'Cancelada'
        elif self.FK_tipo_objeto.tipo_objeto == "EQUIPAMENTO":
            if data_ob_primeira > hoje_24M:
                situacao = 'Em Execução'
            else:
                if saldo_em_conta:
                    situacao = 'Vencida'
                else:
                    situacao = 'Executada'
        else:
            situacao = 'Ativa'
        return situacao
    situacao = property(situacao_calculada)