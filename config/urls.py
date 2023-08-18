from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import include, path

from usuario.router import router as usuario_router

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from livraria.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)