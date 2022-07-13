from django import forms
from django.forms import ModelForm
from .models import *
class Analise_Form(forms.ModelForm):
    class Meta:
        model = tb_analise
        fields = '__all__'
        labels = {
            'FK_tb_equipo_ressarc': ('Proposta'),
            'FK_User': ('Analista Responsável'),
            'ds_gestor': ('Gestor'),
            'ds_prazo': ('Prazo (em dias)'),
        }
        exclude = {'ds_gestor',
                   'date_joined',
                   'FK_tb_equipo_ressarc',
                   'dt_finalizacao',
                   'ds_prazo',
                   }
    def __init__(self, *args, var_user=None, **kwargs):
        super(Analise_Form, self).__init__(*args, **kwargs)
        if var_user is not None:
            self.fields['FK_User'].queryset = User.objects.filter(ds_secretaria=var_user)
class AcompanhamentoForm(ModelForm):
    class Meta:
        model = tb_reg_acompanhamento
        fields = '__all__'
        exclude = ['FK_tb_analise','FK_tb_equipo_ressarc', 'data_registro', 'cancelar_registro']
class FatosGeradoresForm(ModelForm):
    class Meta:
        model = tb_reg_fatos_geradores
        fields = '__all__'
        exclude = ['FK_tb_analise','FK_tb_equipo_ressarc', 'data_registro', 'cancelar_registro']
class RegNotificacaoForm(ModelForm):
    class Meta:
        model = tb_reg_notificacao
        fields = '__all__'
        exclude = ['FK_tb_analise','FK_tb_equipo_ressarc', 'data_registro', 'cancelar_registro']
class EditalNotificacaoForm(ModelForm):
    class Meta:
        model = tb_reg_edital_notif
        fields = '__all__'
        exclude = ['FK_tb_analise','FK_tb_equipo_ressarc', 'data_registro', 'cancelar_registro']
class RegRestituicaoForm(ModelForm):
    class Meta:
        model = tb_reg_restituicao
        fields = '__all__'
        exclude = ['FK_tb_analise','FK_tb_equipo_ressarc', 'data_registro', 'cancelar_registro']
class ValoresForm(ModelForm):
    class Meta:
        model = tb_reg_valores
        fields = '__all__'
        exclude = ['FK_tb_analise','FK_tb_equipo_ressarc', 'data_registro', 'cancelar_registro','vl_proposta','vl_transferido','vl_nao_transferido']