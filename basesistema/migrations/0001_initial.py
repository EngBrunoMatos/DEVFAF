# Generated by Django 3.2.8 on 2022-05-23 14:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basedados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_analise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_gestor', models.CharField(max_length=100, null=True)),
                ('ds_prazo', models.BigIntegerField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date joined')),
                ('dt_finalizacao', models.DateTimeField(blank=True, null=True)),
                ('FK_User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('FK_tb_equipo_ressarc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
        migrations.CreateModel(
            name='tb_reg_valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar_registro', models.BooleanField(blank=True, default=False)),
                ('registro_cancelamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('vl_original', models.FloatField()),
                ('vl_correcao', models.FloatField()),
                ('dt_apuracao', models.DateField()),
                ('FK_tb_analise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basesistema.tb_analise')),
                ('FK_tb_equipo_ressarc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
        migrations.CreateModel(
            name='tb_reg_restituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar_registro', models.BooleanField(blank=True, default=False)),
                ('registro_cancelamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('nr_gru', models.BigIntegerField()),
                ('vl_restituido', models.FloatField()),
                ('dt_restituicao', models.DateField()),
                ('nr_cpf_cnpj', models.BigIntegerField()),
                ('ds_razao_social', models.CharField(max_length=100)),
                ('FK_tb_analise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basesistema.tb_analise')),
                ('FK_tb_equipo_ressarc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
        migrations.CreateModel(
            name='tb_reg_notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar_registro', models.BooleanField(blank=True, default=False)),
                ('registro_cancelamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('nr_nup_oficio', models.BigIntegerField()),
                ('dt_ar', models.DateField()),
                ('dt_limite_notificacao', models.DateField()),
                ('nr_cpf_cnpj', models.BigIntegerField()),
                ('ds_razao_social', models.CharField(max_length=100)),
                ('notificacao', models.CharField(choices=[('E', 'Enviada'), ('N', 'Notificado não encontrado'), ('R', 'Respondida')], max_length=1)),
                ('resp_irregularidade', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('FK_tb_analise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basesistema.tb_analise')),
                ('FK_tb_equipo_ressarc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
        migrations.CreateModel(
            name='tb_reg_fatos_geradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar_registro', models.BooleanField(blank=True, default=False)),
                ('registro_cancelamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tp_irregularidade', models.CharField(max_length=100)),
                ('tp_responsabilidade', models.CharField(choices=[('S', 'Solidária')], max_length=1)),
                ('vl_dano', models.FloatField()),
                ('dt_fato_gerador', models.DateField()),
                ('nr_cpf_cnpj', models.BigIntegerField()),
                ('ds_razao_social', models.CharField(max_length=100)),
                ('FK_tb_analise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basesistema.tb_analise')),
                ('FK_tb_equipo_ressarc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
        migrations.CreateModel(
            name='tb_reg_edital_notif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar_registro', models.BooleanField(blank=True, default=False)),
                ('registro_cancelamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('nr_edital', models.BigIntegerField()),
                ('dt_edital', models.DateField()),
                ('dt_publicacao', models.DateField()),
                ('nr_cpf_cnpj', models.BigIntegerField()),
                ('ds_razao_social', models.CharField(max_length=100)),
                ('FK_tb_analise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basesistema.tb_analise')),
                ('FK_tb_equipo_ressarc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
        migrations.CreateModel(
            name='tb_reg_acompanhamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelar_registro', models.BooleanField(blank=True, default=False)),
                ('registro_cancelamento', models.CharField(blank=True, max_length=200)),
                ('data_registro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status_situacao', models.CharField(blank=True, choices=[('Pendente de Análise', 'Pendente de Análise'), ('Em Análise', 'Em Análise'), ('Medidas Administrativas de Cobrança', 'Medidas Administrativas de Cobrança'), ('Recursos restituídos', 'Recursos restituídos'), ('Sem constatação de débito', 'Sem constatação de débito'), ('Em parcelamento de débitos', 'Em parcelamento de débitos'), ('Em instrução para TCE', 'Em instrução para TCE'), ('Em instrução de cadastro de Débitos Inferiores', 'Em instrução de cadastro de Débitos Inferiores'), ('Enviado para Instauração de TCE', 'Enviado para Instauração de TCE')], max_length=46, null=True, verbose_name='Situação da Devolução')),
                ('tipo_irregularidade', models.CharField(blank=True, choices=[('Dano ou prejuízo ao Erário', 'Dano ou prejuízo ao Erário'), ('Desvio de Finalidade', 'Desvio de Finalidade'), ('Desvio do Objeto', 'Desvio do Objeto'), ('Recebimento Irregular', 'Recebimento Irregular')], max_length=26, null=True, verbose_name='Tipo de Irregularidade')),
                ('status_instrucao', models.CharField(blank=True, choices=[('TCE Instaurada', 'TCE Instaurada'), ('Julgado Regular – TCU', 'Julgado Regular – TCU'), ('Julgado Irregular – TCU', 'Julgado Irregular – TCU'), ('Arquivado – TCU', 'Arquivado – TCU'), ('Quitado – AGU', 'Quitado – AGU'), ('Arquivado - AGU', 'Arquivado - AGU'), ('Cadastro de Débitos Inferiores - CDI', 'Cadastro de Débitos Inferiores - CDI'), ('CDI – Enviado para medidas judiciais', 'CDI – Enviado para medidas judiciais'), ('Em cobrança judicial', 'Em cobrança judicial')], max_length=36, null=True, verbose_name='Status da Instrução')),
                ('entidade_autora', models.CharField(blank=True, max_length=100, null=True, verbose_name='Entidade Auditora')),
                ('nup_rel_auditoria', models.CharField(blank=True, max_length=12, null=True, verbose_name='NUP Relatório de Auditoria')),
                ('motivo_analise', models.CharField(blank=True, max_length=540, null=True, verbose_name='Motivo do Ressarcimento:')),
                ('analise_auditada', models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, null=True, verbose_name='Proposta Auditada?')),
                ('prt_cancelamento', models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, null=True, verbose_name='Possui Portaria de Cancelamento?')),
                ('FK_tb_analise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basesistema.tb_analise')),
                ('FK_tb_equipo_ressarc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='basedados.tb_equipo_ressarc')),
            ],
        ),
    ]
