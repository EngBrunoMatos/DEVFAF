from django.db import models
from cpf_field.models import CPFField
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    LEITOR='LEI'
    ANALISTA='ANA'
    GESTOR='GES'
    opcoes_grupo = [(LEITOR, 'Leitor'),
                    (ANALISTA, 'Analista'),
                    (GESTOR, 'Gestor'),]
    ds_grupo = models.CharField(max_length=3, choices=opcoes_grupo, verbose_name="Grupo", blank=False, null=False, default="LEI")
    SE='Secretaria Executiva - MS'
    FNS='Fundo Nacional de Saúde - FNS'
    SAPS='Secretaria de Atenção Primária à Saúde - SAPS'
    SAES='Secretaria de Atenção Especializada à Saúde - SAES'
    SCTIE='Secretaria de Ciência, Tecnologia, Inovação e Insumos Estratégicos em Saúde - SCTIE'
    SVS='Secretaria de Vigilância em Saúde - SVS'
    SESAI='Secretaria Especial de Saúde Indígena - SESAI'
    SGTES='Secretaria de Gestão do Trabalho e da Educação na Saúde - SGTES'
    SECOVID='Secretaria Extraordinária de Enfrentamento à Covid-19 - SECOVID'
    opcoes_secretaria = [(SE, 'Secretaria Executiva - MS'),
                         (FNS, 'Fundo Nacional de Saúde - FNS'),
                         (SAPS, 'Secretaria de Atenção Primária à Saúde - SAPS'),
                         (SAES, 'Secretaria de Atenção Especializada à Saúde - SAES'),
                         (SCTIE, 'Secretaria de Ciência, Tecnologia, Inovação e Insumos Estratégicos em Saúde - SCTIE'),
                         (SVS, 'Secretaria de Vigilância em Saúde - SVS'),
                         (SESAI, 'Secretaria Especial de Saúde Indígena - SESAI'),
                         (SGTES, 'Secretaria de Gestão do Trabalho e da Educação na Saúde - SGTES'),
                         (SECOVID, 'Secretaria Extraordinária de Enfrentamento à Covid-19 - SECOVID'),]
    ds_secretaria = models.CharField(max_length=83, choices=opcoes_secretaria, verbose_name="Secretaria", blank=False, null=False,)
    username = CPFField(_('CPF'), unique=True)
    first_name = models.CharField(_('Nome'), max_length=30)
    last_name = models.CharField(_('Sobrenome'), max_length=30)
    email = models.EmailField(_('E-mail'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False, help_text=_('Designates whether this user has confirmed his account.'))
    #Esse bloco de código acrescenta o campo is_trusty, que nos dirá se o usuário confirmou o email, ou seja, se é um usuário confiável.
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = UserManager()
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    def get_short_name(self):
        return self.first_name
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    #USERNAME_FIELD: essa variável recebe o campo do model que será utilizado pelo Django para autenticação. É aqui que ao invés de username do model default, eu coloco email para fazer o login pelo email do usuário.
    #REQUIRED_FIELDS: os campos que são obrigatórios desse model. Nenhuma dúvida quanto isso, certo?
    #class Meta, verbose_name e verbose_plural: aqui a gente define a taxonomia que nosso model terá para o Django no singular e no plural.
    #get_full_name, get_short_name e email_user: são métodos de apoio que facilitam nossa vida. Se eu não me engano, elas são obrigatórias para o sistema do Django.

