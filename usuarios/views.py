# experiencein/usuarios/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil

class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        #preenche o form
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            #verifa se eh valido
            dados_form = form.data
            #cria o usuario
            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

            #cria o perfil
            perfil = Perfil(nome=dados_form['nome'],
                           telefone=dados_form['telefone'],
                           nome_empresa=dados_form['nome_empresa'],
                           usuario=usuario)
            #grava no banco
            perfil.save()
            #redireciona para index
            return redirect('index')
            #so checa se nao for valido
            #vamos devolver o form mostrar o formulario valido
        return render(request, self.template_name, {'form' : form})
        