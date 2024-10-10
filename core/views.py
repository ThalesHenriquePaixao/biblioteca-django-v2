from django.http import HttpResponse
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from .filters import LivroFilter

def home(request):
    html = """
    <html>
        <head>
            <title>Página Inicial</title>
        </head>
        <body>
            <h1>Bem-vindo à Biblioteca!</h1>
            <p>Você pode acessar as seguintes URLs:</p>
            <ul>
                <li><a href="/admin/">Admin</a></li>
                <li><a href="/api/livros/">API</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)

class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "livros": reverse(LivroList.name, request=request),
                "categorias": reverse(CategoriaList.name, request=request),
                "autores": reverse(AutorList.name, request=request),
            }
        )

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"
    filterset_class = LivroFilter
    search_fields = ("^titulo",)
    ordering_fields = ("titulo", "autor__nome", "categoria__nome", "publicado_em")

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"