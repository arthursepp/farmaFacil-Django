from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Usuario, Farmacia, Produto

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
    # return HttpResponse("Hello world!")

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def cadastro(request):  
    # template = loader.get_template('cadastro.html')
    # return HttpResponse(template.render())
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        dataNasc = request.POST.get('dataNasc')
        endereco = request.POST.get('endereco')
        complemento = request.POST.get('complemento')
        cep = request.POST.get('cep')
        senha = request.POST.get('senha')
        
        usuario = Usuario(nome=nome, email=email, cpf=cpf, dataNasc=dataNasc, endereco=endereco, complemento=complemento, cep=cep, senha=senha)
        usuario.save()
        
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def cadastroFarmacia (request):
    # template = loader.get_template('cadastro-farma.html')
    # return HttpResponse(template.render())        
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        cep =  request.POST.get('cep')
        endereco = request.POST.get('endereco')
        senha = request.POST.get('senha')
        
        farmacia = Farmacia(nome=nome, telefone=telefone, cnpj=cnpj, email=email, cep=cep, endereco=endereco, senha=senha)
        farmacia.save()        
        
        return redirect('login')
    else:
        return render(request, 'cadastroFarmacia.html')
    

def cadastroProduto(request):
    template = loader.get_template('cadastro-produto.html')
    return HttpResponse(template.render())

def produtos(request):
    produto = Produto.objects.all()
    template = loader.get_template('produtos.html')
    context = {
        'produto': produto,
    }
    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    produto = Produto.objects.get(id=id)
    template = loader.get_template('detalhes.html')
    context = {
        'produto': produto,
    }
    return HttpResponse(template.render(context, request))
