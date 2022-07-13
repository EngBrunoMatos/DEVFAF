from django import template
from basedados.models import tb_equipo_saldo, tb_equipo_ressarc
from datetime import datetime, date
register = template.Library()
@register.filter(name='cnpj')
def cnpj_mask(item, mask="{}.{}.{}/{}-{}"):
    item = str(item)
    if item:
        return mask.format(
            item[0:2],
            item[2:5],
            item[5:8],
            item[8:12],
            item[12:14]
        )
    else:
        return None
@register.filter(name='FormataDATA')
def FormataDATA(value):
    dataFormatada = datetime.strptime(value, "%d/%m/%Y").date()
    if dataFormatada <= datetime.strptime("31/12/2016", "%d/%m/%Y").date():
        return "Plano 1"
    if datetime.strptime("01/01/2017", "%d/%m/%Y").date() <= dataFormatada <= datetime.strptime("30/06/2021", "%d/%m/%Y").date():
        return "Plano 2"
    else:
        return "Outro Plano"
@register.filter(name='FormataValor')
def FormataValor(value):
    return "R$ {:,.2f}".format(1*float(value.replace(',', '.'))).replace(",", "X").replace(".", ",").replace("X", ".")
@register.filter(name='FormataValorINT')
def FormataValorINT(value):
    if value:
        return "R$ {:,.2f}".format(1*float(str(value).replace(',', '.'))).replace(",", "X").replace(".", ",").replace("X", ".")
    else:
        return '---'
@register.filter(name='Risco')
def Risco(value):
    R_Pre = date.today().year - datetime.strptime(tb_equipo_ressarc.objects.get(id=value).data_portaria_habilitacao, "%d/%m/%Y").date().year
    if R_Pre<=5:
        R_Pre=1
    elif R_Pre==6:
        R_Pre=2
    elif R_Pre==7:
        R_Pre=4
    elif R_Pre==8:
        R_Pre=6
    elif R_Pre==9:
        R_Pre=8
    elif R_Pre==10:
        R_Pre=10
    else:
        R_Pre=12
    R_Mat = float(tb_equipo_ressarc.objects.get(id=value).valor_transferido.replace(',', '.'))
    if R_Mat<=1000:
        R_Mat=1
    elif R_Mat<=10000:
        R_Mat = 2
    elif R_Mat<=100000:
        R_Mat = 3
    elif R_Mat<=2000000:
        R_Mat = 4
    elif R_Mat<=5000000:
        R_Mat = 5
    else:
        R_Mat = 6
    return R_Pre+R_Mat
@register.filter(name='qqcoisa')
def qqcoisa(value, arg):
    var = (value)
    object2 = tb_equipo_saldo.objects.all()
    saldo_em_conta = 0
    for b in object2:
        if b.nr_proposta == var:
            string = b.vl_saldo_conta
            characters = "R$ ."
            string = ''.join(x for x in string if x not in characters)
            string = float(string.replace(',', '.'))
            saldo_em_conta = saldo_em_conta + string
            datam = b.dt_ult_pgto_prop
    saldo_em_conta = "R$ {:,.2f}".format(saldo_em_conta).replace(",", "X").replace(".", ",").replace("X", ".")
    if arg == "total_saldo_em_conta":
        return saldo_em_conta
    if arg == "data_finalizacao":
        return datam