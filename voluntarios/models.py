#encoding: utf-8

from django.db import models



class Voluntarios(models.Model):

    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=50)
    email = models.EmailField(verbose_name=u'E-mail')
    telefone = models.CharField(verbose_name=u'Telefone',max_length=12)
    cidade = models.CharField(verbose_name=u'Cidade', max_length=30)
    estado = models.CharField(verbose_name=u'Estado', max_length=15)
    cpf = models.CharField(verbose_name=u'CPF', max_length=20, unique=True)
    curriculum = models.FileField(u"Curriculum", max_length=200,
        upload_to="curriculum")
    skills = models.TextField(verbose_name=u'Skills')
    linkedin = models.CharField(verbose_name=u'Linkedin', max_length=30)
    observacao = models.TextField(verbose_name=u'Observações')

    class Meta:
        abstract = True
    

class GTI(Voluntarios):
    github = models.CharField(verbose_name=u'Github', max_length=30)
    bitbucket = models.CharField(verbose_name=u'Bitbucket', max_length=30)
    gerenciar_projeto = models.BooleanField(verbose_name=u'Gerenciou Projeto')


    def __unicode__(self):
        return '%s' % self.title
    
    class Meta:
        verbose_name = u'Voluntários GTI'
        verbose_name_plural = u'Voluntários GTI'
        ordering = ['nome_completo']