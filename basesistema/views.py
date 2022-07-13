from django.views.generic import ListView, DetailView
from basedados.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import *
def Filtros_Lista_Equipamentos(slug):
        if slug == 'Atribuidas':
            return redirect('Lista_Geral_Atribuidas_Equipamentos')
        elif slug == 'N_Atribuidas':
            return redirect('Lista_Geral_N_Atribuidas_Equipamentos')
        elif slug == 'Geral':
            return redirect('Lista_Geral_Equipamentos')
        elif slug == 'Analista':
            return redirect('Lista_Geral_Analista_Equipamentos')
class Lista_Geral_N_Atribuidas_Equipamentos(LoginRequiredMixin, ListView):
    model = tb_equipo_ressarc
    paginate_by = 30
    form_class = Analise_Form
    template_name = 'Lista_Geral_N_Atribuidas_Equipamentos.html'
    def post(self, request):
        qs_analise = tb_analise.objects.all()
        if request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                lista_responsavel_post = self.request.POST.get('Button_Lista_Responsavel').split(',')
                for i in range(len(lista_responsavel_post)):
                    try:
                        ID_ANALISE = qs_analise.filter(FK_tb_equipo_ressarc=lista_responsavel_post[i]).last().id
                        qs_analise.filter(id=ID_ANALISE).update(dt_finalizacao=datetime.now())
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                    except:
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                return redirect('Lista_Geral_N_Atribuidas_Equipamentos')
        return redirect('Lista_Geral_N_Atribuidas_Equipamentos')
    def get_context_data(self, *args, **kwargs):
        context = super(Lista_Geral_N_Atribuidas_Equipamentos, self).get_context_data(**kwargs)
        context.update({
            'form': Analise_Form(var_user=self.request.user.ds_secretaria),
            'qs_analise': tb_analise.objects.all(),
        })
        return context
    def get_queryset(self, **kwargs):
        tb_for_1 = tb_equipo_ressarc.objects.all()
        tb_for_2 = tb_analise.objects.all()
        post_list = tb_for_1.filter(Q(FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        #######################################################################################
        for xx in tb_for_2:
            for yy in tb_for_1:
                if xx.FK_tb_equipo_ressarc.nr_proposta == yy.nr_proposta:
                    post_list = post_list.filter(~Q(nr_proposta=yy.nr_proposta))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)
        else:
            post_list = sorted(post_list.order_by('-ano_portaria_habilitacao', '-valor_proposta', '-nr_proposta'),
                               reverse=True, key=lambda p: p.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Lista_Geral_Atribuidas_Equipamentos(LoginRequiredMixin, ListView):
    model = tb_analise
    paginate_by = 30
    form_class = Analise_Form
    template_name = 'Lista_Geral_Atribuidas_Equipamentos.html'
    def post(self, request):
        qs_analise = tb_analise.objects.all()
        if request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                lista_responsavel_post = self.request.POST.get('Button_Lista_Responsavel').split(',')
                for i in range(len(lista_responsavel_post)):
                    try:
                        ID_ANALISE = qs_analise.filter(FK_tb_equipo_ressarc=lista_responsavel_post[i]).last().id
                        qs_analise.filter(id=ID_ANALISE).update(dt_finalizacao=datetime.now())
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                    except:
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                return redirect('Lista_Geral_Atribuidas_Equipamentos')
        return redirect('Lista_Geral_Atribuidas_Equipamentos')
    def get_context_data(self, *args, **kwargs):
        context = super(Lista_Geral_Atribuidas_Equipamentos, self).get_context_data(**kwargs)
        context.update({
            'form': Analise_Form(var_user=self.request.user.ds_secretaria),
        })
        return context
    def get_queryset(self, **kwargs):
        post_list = tb_analise.objects.filter(Q(FK_tb_equipo_ressarc__FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)
        else:
            post_list = sorted(post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao',
                                                  '-FK_tb_equipo_ressarc__valor_proposta',
                                                  '-FK_tb_equipo_ressarc__nr_proposta'),
                               reverse=True, key=lambda p: p.FK_tb_equipo_ressarc.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Lista_Geral_Equipamentos(LoginRequiredMixin, ListView):
    model = tb_equipo_ressarc
    paginate_by = 30
    form_class = Analise_Form
    template_name = 'Lista_Geral_Equipamentos.html'
    def post(self, request):
        qs_analise = tb_analise.objects.all()
        if request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                lista_responsavel_post = self.request.POST.get('Button_Lista_Responsavel').split(',')
                for i in range(len(lista_responsavel_post)):
                    try:
                        ID_ANALISE = qs_analise.filter(FK_tb_equipo_ressarc=lista_responsavel_post[i]).last().id
                        qs_analise.filter(id=ID_ANALISE).update(dt_finalizacao=datetime.now())
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                    except:
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                return redirect('Lista_Geral_Equipamentos')
        return redirect('Lista_Geral_Equipamentos')
    def get_context_data(self, *args, **kwargs):
        context = super(Lista_Geral_Equipamentos, self).get_context_data(**kwargs)
        context.update({
            'form': Analise_Form(var_user=self.request.user.ds_secretaria),
            'qs_analise': tb_analise.objects.all(),
        })
        return context
    def get_queryset(self, **kwargs):
        post_list = tb_equipo_ressarc.objects.filter(Q(FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)
        else:
            post_list = sorted(post_list.order_by('-ano_portaria_habilitacao', '-valor_proposta', '-nr_proposta'),
                               reverse=True, key=lambda p: p.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Lista_Geral_Analista_Equipamentos(LoginRequiredMixin, ListView):
    model = tb_analise
    paginate_by = 30
    template_name = 'Lista_Geral_Analista_Equipamentos.html'
    def get_queryset(self, **kwargs):
        post_list = tb_analise.objects.filter(Q(FK_tb_equipo_ressarc__FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)
        else:
            post_list = sorted(post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao',
                                                  '-FK_tb_equipo_ressarc__valor_proposta',
                                                  '-FK_tb_equipo_ressarc__nr_proposta'),
                               reverse=True, key=lambda p: p.FK_tb_equipo_ressarc.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Detalha_Proposta_Equipamentos(LoginRequiredMixin, DetailView):
    model = tb_equipo_ressarc
    template_name = 'Detalha_Proposta_Equipamentos.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_restituido = val1 = val2 = 0
        if tb_reg_valores.objects.all():
            val1 = tb_reg_valores.objects.filter(cancelar_registro=0).last().vl_original
        if tb_reg_valores.objects.all():
            val2 = tb_reg_valores.objects.filter(cancelar_registro=0).last().vl_correcao
        if tb_reg_restituicao.objects.all():
            for objeto in tb_reg_restituicao.objects.all():
                if objeto.cancelar_registro == 0:
                    total_restituido = total_restituido+objeto.vl_restituido
        context.update({
            'lista_saldos': tb_equipo_saldo.objects.filter(nr_proposta=tb_equipo_ressarc.objects.filter(nr_proposta=self.kwargs['pk']).last().nr_proposta).last(),
            'lista_ob': tb_equipo_ob_parc.objects.filter(nr_proposta=tb_equipo_ressarc.objects.filter(nr_proposta=self.kwargs['pk']).last().nr_proposta).last(),
            'lista_valores': tb_reg_valores.objects.all().order_by('-data_registro').order_by('-data_registro'),
            'lista_acompanhamento': tb_reg_acompanhamento.objects.all().order_by('-data_registro'),
            'lista_fatos_geradores': tb_reg_fatos_geradores.objects.all().order_by('-data_registro'),
            'lista_reg_notificacao': tb_reg_notificacao.objects.all().order_by('-data_registro'),
            'lista_reg_edital_notif': tb_reg_edital_notif.objects.all().order_by('-data_registro'),
            'lista_reg_restituicao': tb_reg_restituicao.objects.all().order_by('-data_registro'),
            'last_lista_acomp': tb_reg_acompanhamento.objects.filter(cancelar_registro=0).last(),
            'last_lista_valores': tb_reg_valores.objects.filter(cancelar_registro=0).last(),
            'last_lista_restituicao': tb_reg_restituicao.objects.filter(cancelar_registro=0).last(),
            'last_lista_fatos_geradores': tb_reg_fatos_geradores.objects.filter(cancelar_registro=0).last(),
            'total_debito': val1 + val2,
            'total_restituido':total_restituido,
            'total_A_restituir':val1 + val2 - total_restituido,
            'qs_analise': tb_analise.objects.filter(FK_tb_equipo_ressarc=tb_equipo_ressarc.objects.filter(nr_proposta=self.kwargs['pk']).last().nr_proposta).last(),
        })
        return context
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            Value_acompanhamento = self.request.POST.get('lista_acompanhamento')
            Value_valores = self.request.POST.get('lista_valores')
            Value_fatos = self.request.POST.get('lista_fatos')
            Value_restituicao = self.request.POST.get('lista_restituicao')
            Value_notificacao = self.request.POST.get('lista_notificacao')
            Value_edital = self.request.POST.get('lista_edital')
            tb_reg_acompanhamento.objects.filter(pk=Value_acompanhamento).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_acompanhamento.objects.filter(pk=Value_acompanhamento).update(cancelar_registro='1')

            tb_reg_fatos_geradores.objects.filter(pk=Value_fatos).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_fatos_geradores.objects.filter(pk=Value_fatos).update(cancelar_registro='1')
            tb_reg_valores.objects.filter(pk=Value_valores).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_valores.objects.filter(pk=Value_valores).update(cancelar_registro='1')
            tb_reg_restituicao.objects.filter(pk=Value_restituicao).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_restituicao.objects.filter(pk=Value_restituicao).update(cancelar_registro='1')
            tb_reg_notificacao.objects.filter(pk=Value_notificacao).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_notificacao.objects.filter(pk=Value_notificacao).update(cancelar_registro='1')
            tb_reg_edital_notif.objects.filter(pk=Value_edital).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_edital_notif.objects.filter(pk=Value_edital).update(cancelar_registro='1')
        if tb_analise.objects.get(
                FK_tb_equipo_ressarc=self.kwargs['pk']).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
            return redirect('Detalha_Proposta_Equipamentos', self.kwargs['pk'])
        else:
            return redirect('Detalha_Proposta_Obras', self.kwargs['pk'])
def Filtros_Lista_Obras(slug):
        if slug == 'Atribuidas':
            return redirect('Lista_Geral_Atribuidas_Obras')
        elif slug == 'N_Atribuidas':
            return redirect('Lista_Geral_N_Atribuidas_Obras')
        elif slug == 'Geral':
            return redirect('Lista_Geral_Obras')
        elif slug == 'Analista':
            return redirect('Lista_Geral_Analista_Obras')
class Lista_Geral_N_Atribuidas_Obras(LoginRequiredMixin, ListView):
    model = tb_equipo_ressarc
    paginate_by = 30
    form_class = Analise_Form
    template_name = 'Lista_Geral_N_Atribuidas_Obras.html'
    def post(self, request):
        qs_analise = tb_analise.objects.all()
        if request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                lista_responsavel_post = self.request.POST.get('Button_Lista_Responsavel').split(',')
                for i in range(len(lista_responsavel_post)):
                    try:
                        ID_ANALISE = qs_analise.filter(FK_tb_equipo_ressarc=lista_responsavel_post[i]).last().id
                        qs_analise.filter(id=ID_ANALISE).update(dt_finalizacao=datetime.now())
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                    except:
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                return redirect('Lista_Geral_N_Atribuidas_Obras')
        return redirect('Lista_Geral_N_Atribuidas_Obras')
    def get_context_data(self, *args, **kwargs):
        context = super(Lista_Geral_N_Atribuidas_Obras, self).get_context_data(**kwargs)
        context.update({
            'form': Analise_Form(var_user=self.request.user.ds_secretaria),
            'qs_analise': tb_analise.objects.all(),
        })
        return context
    def get_queryset(self, **kwargs):
        tb_for_1 = tb_equipo_ressarc.objects.all()
        tb_for_2 = tb_analise.objects.all()
        post_list = tb_for_1.filter(~Q(FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        #######################################################################################
        for xx in tb_for_2:
            for yy in tb_for_1:
                if xx.FK_tb_equipo_ressarc.nr_proposta == yy.nr_proposta:
                    post_list = post_list.filter(~Q(nr_proposta=yy.nr_proposta))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)

        else:
            post_list = sorted(post_list.order_by('-ano_portaria_habilitacao', '-valor_proposta', '-nr_proposta'),
                               reverse=True, key=lambda p: p.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Lista_Geral_Atribuidas_Obras(LoginRequiredMixin, ListView):
    model = tb_analise
    paginate_by = 30
    form_class = Analise_Form
    template_name = 'Lista_Geral_Atribuidas_Obras.html'
    def post(self, request):
        qs_analise = tb_analise.objects.all()
        if request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                lista_responsavel_post = self.request.POST.get('Button_Lista_Responsavel').split(',')
                for i in range(len(lista_responsavel_post)):
                    try:
                        ID_ANALISE = qs_analise.filter(FK_tb_equipo_ressarc=lista_responsavel_post[i]).last().id
                        qs_analise.filter(id=ID_ANALISE).update(dt_finalizacao=datetime.now())
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                    except:
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                return redirect('Lista_Geral_Atribuidas_Obras')
        return redirect('Lista_Geral_Atribuidas_Obras')
    def get_context_data(self, *args, **kwargs):
        context = super(Lista_Geral_Atribuidas_Obras, self).get_context_data(**kwargs)
        context.update({
            'form': Analise_Form(var_user=self.request.user.ds_secretaria),
        })
        return context
    def get_queryset(self, **kwargs):
        post_list = tb_analise.objects.filter(~Q(FK_tb_equipo_ressarc__FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)

        else:
            post_list = sorted(post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao',
                                                  '-FK_tb_equipo_ressarc__valor_proposta',
                                                  '-FK_tb_equipo_ressarc__nr_proposta'),
                               reverse=True, key=lambda p: p.FK_tb_equipo_ressarc.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Lista_Geral_Obras(LoginRequiredMixin, ListView):
    model = tb_equipo_ressarc
    paginate_by = 30
    form_class = Analise_Form
    template_name = 'Lista_Geral_Obras.html'
    def post(self, request):
        qs_analise = tb_analise.objects.all()
        if request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                lista_responsavel_post = self.request.POST.get('Button_Lista_Responsavel').split(',')
                for i in range(len(lista_responsavel_post)):
                    try:
                        ID_ANALISE = qs_analise.filter(FK_tb_equipo_ressarc=lista_responsavel_post[i]).last().id
                        qs_analise.filter(id=ID_ANALISE).update(dt_finalizacao=datetime.now())
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                    except:
                        form = Analise_Form(self.request.POST)
                        post = form.save(commit=False)
                        post.save()
                        qs_analise.filter(id=post.id).update(ds_gestor=request.user.id)
                        qs_analise.filter(id=post.id).update(FK_tb_equipo_ressarc=lista_responsavel_post[i])
                return redirect('Lista_Geral_Obras')
        return redirect('Lista_Geral_Obras')
    def get_context_data(self, *args, **kwargs):
        context = super(Lista_Geral_Obras, self).get_context_data(**kwargs)
        context.update({
            'form': Analise_Form(var_user=self.request.user.ds_secretaria),
            'qs_analise': tb_analise.objects.all(),
        })
        return context
    def get_queryset(self, **kwargs):
        post_list = tb_equipo_ressarc.objects.filter(~Q(FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)
        else:
            post_list = sorted(post_list.order_by('-ano_portaria_habilitacao', '-valor_proposta', '-nr_proposta'),
                               reverse=True, key=lambda p: p.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Lista_Geral_Analista_Obras(LoginRequiredMixin, ListView):
    model = tb_analise
    paginate_by = 30
    template_name = 'Lista_Geral_Analista_Obras.html'
    def get_queryset(self, **kwargs):
        post_list = tb_analise.objects.filter(~Q(FK_tb_equipo_ressarc__FK_tipo_objeto__tipo_objeto='EQUIPAMENTO'))
        #######################################################################################
        ###### Filtro por Proposta ############################################################
        filtro_nr_proposta = self.request.GET.get('Pesquisa_Proposta', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__nr_proposta__icontains=filtro_nr_proposta))
        ###### Filtro por Município ############################################################
        filtro_municipio = self.request.GET.get('Pesquisa_Municipio', '')
        post_list = post_list.filter(Q(FK_tb_equipo_ressarc__FK_municipio__municipio__icontains=filtro_municipio))
        ###### Ordenamento por Coluna #########################################################
        # ordenação crescente
        sel_ordem = self.request.GET.get('sel_ordem', '')
        if sel_ordem == "ord_prop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__nr_proposta')
        elif sel_ordem == "ord_ano":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_proposta')
        elif sel_ordem == "ord_vltrans":
            post_list = post_list.order_by('-FK_tb_equipo_ressarc__valor_transferido')
        elif sel_ordem == "ord_risco":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao":
            post_list = sorted(post_list, reverse=False, key=lambda p: p.situacao)
        # decrescente
        elif sel_ordem == "ord_prop_D":
            post_list = post_list.order_by('nr_proposta')
        elif sel_ordem == "ord_ano_D":
            post_list = post_list.order_by('ano_portaria_habilitacao')
        elif sel_ordem == "ord_vlprop_D":
            post_list = post_list.order_by('valor_proposta')
        elif sel_ordem == "ord_vltrans_D":
            post_list = post_list.order_by('valor_transferido')
        elif sel_ordem == "ord_risco_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.risco)
        elif sel_ordem == "ord_situacao_D":
            post_list = sorted(post_list, reverse=True, key=lambda p: p.situacao)
        else:
            post_list = sorted(post_list.order_by('-FK_tb_equipo_ressarc__ano_portaria_habilitacao',
                                                  '-FK_tb_equipo_ressarc__valor_proposta',
                                                  '-FK_tb_equipo_ressarc__nr_proposta'),
                               reverse=True, key=lambda p: p.FK_tb_equipo_ressarc.risco)
        ##################################################################################################################
        ##################################################################################################################
        return post_list
class Detalha_Proposta_Obras(LoginRequiredMixin, DetailView):
    model = tb_equipo_ressarc
    template_name = 'Detalha_Proposta_Obras.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_restituido = val1 = val2 = 0
        if tb_reg_valores.objects.all():
            val1 = tb_reg_valores.objects.filter(cancelar_registro=0).last().vl_original
        if tb_reg_valores.objects.all():
            val2 = tb_reg_valores.objects.filter(cancelar_registro=0).last().vl_correcao
        if tb_reg_restituicao.objects.all():
            for objeto in tb_reg_restituicao.objects.all():
                if objeto.cancelar_registro == 0:
                    total_restituido = total_restituido + objeto.vl_restituido
        context.update({
            'lista_saldos': tb_equipo_saldo.objects.filter(nr_proposta=tb_equipo_ressarc.objects.filter(nr_proposta=self.kwargs['pk']).last().nr_proposta).last(),
            'lista_ob': tb_equipo_ob_parc.objects.filter(nr_proposta=tb_equipo_ressarc.objects.filter(nr_proposta=self.kwargs['pk']).last().nr_proposta).last(),
            'lista_valores': tb_reg_valores.objects.all().order_by('-data_registro').order_by('-data_registro'),

            'lista_acompanhamento': tb_reg_acompanhamento.objects.all().order_by('-data_registro'),

            'lista_fatos_geradores': tb_reg_fatos_geradores.objects.all().order_by('-data_registro'),
            'lista_reg_notificacao': tb_reg_notificacao.objects.all().order_by('-data_registro'),
            'lista_reg_edital_notif': tb_reg_edital_notif.objects.all().order_by('-data_registro'),
            'lista_reg_restituicao': tb_reg_restituicao.objects.all().order_by('-data_registro'),
            'last_lista_acomp': tb_reg_acompanhamento.objects.filter(cancelar_registro=0).last(),
            'last_lista_valores': tb_reg_valores.objects.filter(cancelar_registro=0).last(),
            'last_lista_restituicao': tb_reg_restituicao.objects.filter(cancelar_registro=0).last(),
            'last_lista_fatos_geradores': tb_reg_fatos_geradores.objects.filter(cancelar_registro=0).last(),
            'total_debito': val1 + val2,
            'total_restituido': total_restituido,
            'total_A_restituir': val1 + val2 - total_restituido,
            'qs_analise': tb_analise.objects.filter(FK_tb_equipo_ressarc=tb_equipo_ressarc.objects.filter(nr_proposta=self.kwargs['pk']).last().nr_proposta).last(),
        })
        return context
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            Value_acompanhamento = self.request.POST.get('lista_acompanhamento')
            Value_valores = self.request.POST.get('lista_valores')
            Value_fatos = self.request.POST.get('lista_fatos')
            Value_restituicao = self.request.POST.get('lista_restituicao')
            Value_notificacao = self.request.POST.get('lista_notificacao')
            Value_edital = self.request.POST.get('lista_edital')
            tb_reg_acompanhamento.objects.filter(pk=Value_acompanhamento).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_acompanhamento.objects.filter(pk=Value_acompanhamento).update(cancelar_registro='1')
            tb_reg_fatos_geradores.objects.filter(pk=Value_fatos).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_fatos_geradores.objects.filter(pk=Value_fatos).update(cancelar_registro='1')
            tb_reg_valores.objects.filter(pk=Value_valores).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_valores.objects.filter(pk=Value_valores).update(cancelar_registro='1')
            tb_reg_restituicao.objects.filter(pk=Value_restituicao).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_restituicao.objects.filter(pk=Value_restituicao).update(cancelar_registro='1')
            tb_reg_notificacao.objects.filter(pk=Value_notificacao).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_notificacao.objects.filter(pk=Value_notificacao).update(cancelar_registro='1')
            tb_reg_edital_notif.objects.filter(pk=Value_edital).update(registro_cancelamento=str(request.user)+str(datetime.now().strftime('\n%d/%m/%Y %H:%M')))
            tb_reg_edital_notif.objects.filter(pk=Value_edital).update(cancelar_registro='1')
        if tb_analise.objects.get(
                FK_tb_equipo_ressarc=self.kwargs['pk']).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
            return redirect('Detalha_Proposta_Equipamentos', self.kwargs['pk'])
        else:
            return redirect('Detalha_Proposta_Obras', self.kwargs['pk'])
def reg_valores(request, pk):
    tabela_equipo_ressarc_PK = tb_equipo_ressarc.objects.get(nr_proposta=pk)
    if request.method == "POST":
        form = ValoresForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.vl_proposta = float(tb_equipo_ressarc.objects.get(nr_proposta=pk).valor_proposta.replace(",", "."))
            post.vl_transferido = float(tb_equipo_ressarc.objects.get(nr_proposta=pk).valor_transferido.replace(",", "."))
            post.vl_nao_transferido = float(tb_equipo_ressarc.objects.get(nr_proposta=pk).valor_nao_transferido.replace(",", "."))
            post.save()
            tb_reg_valores.objects.filter(pk=post.id).update(FK_tb_analise=tb_analise.objects.filter(FK_tb_equipo_ressarc=pk).last().id)
            tb_reg_valores.objects.filter(pk=post.id).update(FK_tb_equipo_ressarc=pk)
            if tb_analise.objects.get(FK_tb_equipo_ressarc=pk).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
                return redirect('Detalha_Proposta_Equipamentos', pk=pk)
            else:
                return redirect('Detalha_Proposta_Obras', pk=pk)
    else:
        form = ValoresForm(instance=tb_reg_valores.objects.filter(cancelar_registro=0).last())
        return render(request, 'acompanhamento_histvalores.html', {'form': form, 'tabela_equipo_ressarc_PK': tabela_equipo_ressarc_PK})
def fatos_geradores(request, pk):
    if request.method == "POST":
        form = FatosGeradoresForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            tb_reg_valores.objects.filter(pk=post.id).update(FK_tb_analise=tb_analise.objects.filter(FK_tb_equipo_ressarc=pk).last().id)
            tb_reg_valores.objects.filter(pk=post.id).update(FK_tb_equipo_ressarc=pk)
            if tb_analise.objects.get(FK_tb_equipo_ressarc=pk).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
                return redirect('Detalha_Proposta_Equipamentos', pk=pk)
            else:
                return redirect('Detalha_Proposta_Obras', pk=pk)
    else:
        form = FatosGeradoresForm(instance=tb_reg_fatos_geradores.objects.filter(cancelar_registro=0).last())
        return render(request, 'acompanhamento_fatosgeradores.html', {'form': form})
def reg_notificacao(request, pk):
    if request.method == "POST":
        form = RegNotificacaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            tb_reg_notificacao.objects.filter(pk=post.id).update(FK_tb_analise=tb_analise.objects.filter(FK_tb_equipo_ressarc=pk).last().id)
            tb_reg_notificacao.objects.filter(pk=post.id).update(FK_tb_equipo_ressarc=pk)
            if tb_analise.objects.get(FK_tb_equipo_ressarc=pk).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
                return redirect('Detalha_Proposta_Equipamentos', pk=pk)
            else:
                return redirect('Detalha_Proposta_Obras', pk=pk)
    else:
        form = RegNotificacaoForm(instance=tb_reg_notificacao.objects.filter(cancelar_registro=0).last())
        return render(request, 'acompanhamento_registronotificacao.html', {'form': form})
def reg_restituicao(request, pk):
    if request.method == "POST":
        form = RegRestituicaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            tb_reg_restituicao.objects.filter(pk=post.id).update(FK_tb_analise=tb_analise.objects.filter(FK_tb_equipo_ressarc=pk).last().id)
            tb_reg_restituicao.objects.filter(pk=post.id).update(FK_tb_equipo_ressarc=pk)
            if tb_analise.objects.get(FK_tb_equipo_ressarc=pk).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
                return redirect('Detalha_Proposta_Equipamentos', pk=pk)
            else:
                return redirect('Detalha_Proposta_Obras', pk=pk)
    else:
        form = RegRestituicaoForm(instance=tb_reg_restituicao.objects.filter(cancelar_registro=0).last())
        return render(request, 'acompanhamento_restituicao.html', {'form': form})
def reg_edital_notif(request, pk):
    if request.method == "POST":
        form = EditalNotificacaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            tb_reg_edital_notif.objects.filter(pk=post.id).update(FK_tb_analise=tb_analise.objects.filter(FK_tb_equipo_ressarc=pk).last().id)
            tb_reg_edital_notif.objects.filter(pk=post.id).update(FK_tb_equipo_ressarc=pk)
            if tb_analise.objects.get(FK_tb_equipo_ressarc=pk).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto == 'EQUIPAMENTO':
                return redirect('Detalha_Proposta_Equipamentos', pk=pk)
            else:
                return redirect('Detalha_Proposta_Obras', pk=pk)
    else:
        form = EditalNotificacaoForm(instance=tb_reg_edital_notif.objects.filter(cancelar_registro=0).last())
        return render(request, 'acompanhamento_editalnotificacao.html', {'form': form})
def reg_acompanhamento(request, pk):
    object_check = tb_analise.objects.get(FK_tb_equipo_ressarc=pk).FK_tb_equipo_ressarc.FK_tipo_objeto.tipo_objeto
    if request.method == "POST":
        form = AcompanhamentoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            tb_reg_acompanhamento.objects.filter(pk=post.id).update(FK_tb_analise=tb_analise.objects.filter(FK_tb_equipo_ressarc=pk).last().id)
            tb_reg_acompanhamento.objects.filter(pk=post.id).update(FK_tb_equipo_ressarc=pk)
            if object_check == 'EQUIPAMENTO':
                return redirect('Detalha_Proposta_Equipamentos', pk=pk)
            else:
                return redirect('Detalha_Proposta_Obras', pk=pk)
    else:
        form = AcompanhamentoForm(instance=tb_reg_acompanhamento.objects.filter(cancelar_registro=0).last())
        return render(request, 'acompanhamento_histacompanhamento.html', {'form': form, 'object_check':object_check})