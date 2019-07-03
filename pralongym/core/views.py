from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cliente

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

#verifica dados do login
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return redirect('/login/')

#retorna todos os dados
def dados_all(request):
    cliente = Cliente.objects.filter(ativo=True)
    return render(request,'dados.html', {'cliente':cliente})

#mostra separadamente os dados de um cliente
def dados_detail(request, id):
    cliente = Cliente.objects.get(ativo=True, id=id)
    print(cliente.id)
    return render(request,'cliente.html', {'cliente':cliente} )

#leva para a página de registro
def register_dados(request):
    return render(request, 'cadastro.html')


@login_required(login_url='/login/')
def set_cliente(request):
    nome = request.POST.get('nome')
    sexo = request.POST.get('sexo')
    data = request.POST.get('data')
    peso = request.POST.get('peso')
    altura = request.POST.get('altura')
    imc = request.POST.get('imc')
    avaliacao_do_IMC = request.POST.get('avaliacao')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')
    plano = request.POST.get('plano')
    meta = request.POST.get('meta')
    file = request.FILES.get('file')
    id = request.POST.get('id')
    user = request.user
    if id:
        cliente = Cliente.objects.get(id=id)
        if user == cliente.user:
            cliente.nome = nome
            cliente.sexo = sexo
            cliente.data = data
            cliente.peso = peso
            cliente.altura = altura
            cliente.imc = imc
            cliente.avaliacao = avaliacao_do_IMC
            cliente.endereco = endereco
            cliente.telefone = telefone
            cliente.plano = plano
            cliente.meta = meta
            if file:
                cliente.photo = file
                cliente.save()
    else:
        cliente = Cliente.objects.create(nome=nome, sexo=sexo, data=data, peso=peso, altura=altura, imc=imc, avaliacao=avaliacao_do_IMC, endereco=endereco, telefone=telefone, plano=plano, meta=meta, user=user, photo=file )
    url = '/dados/detail/{}/'.format(cliente.id)
    return redirect(url)

@login_required(login_url='/login/')
def edit_cliente(request, id):
    nome = request.POST.get('nome')
    sexo = request.POST.get('sexo')
    data = request.POST.get('data')
    peso = request.POST.get('peso')
    altura = request.POST.get('altura')
    imc = request.POST.get('imc')
    avaliacao_do_IMC = request.POST.get('avaliacao')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')
    plano = request.POST.get('plano')
    meta = request.POST.get('meta')
    file = request.FILES.get('file')
    id = request.POST.get('id')
    user = request.user
    if id:
        cliente = Cliente.objects.get(id=id)
        if user == cliente.user:
            cliente.nome = nome
            cliente.sexo = sexo
            cliente.data = data
            cliente.peso = peso
            cliente.altura = altura
            cliente.imc = imc
            cliente.avaliacao = avaliacao_do_IMC
            cliente.endereco = endereco
            cliente.telefone = telefone
            cliente.plano = plano
            cliente.meta = meta
            if file:
                cliente.photo = file
                cliente.save()
    else:
        cliente = Cliente.objects.update(nome=nome, sexo=sexo, data=data, peso=peso, altura=altura, imc=imc, avaliacao=avaliacao_do_IMC, endereco=endereco, telefone=telefone, plano=plano, meta=meta, user=user, photo=file )
    url = '/dados/detail/{}/'.format(cliente.id)
    return redirect(url)

#leva para a pagina de edicao de cadastro
@login_required(login_url='/login/')
def dados_edit(request, id):
    cliente = Cliente.objects.get(ativo=True, id=id)
    return render(request, 'cadastro.html', {'cliente': cliente})

#deleta os dados do cliente
@login_required(login_url='/login/')
def dados_delete(request, id):
    cliente = Cliente.objects.get(ativo=True, id=id).delete()
    return redirect('/dados/all/')

#leva a página de planos da academia
def planos (request):
    return render(request, 'planos.html')