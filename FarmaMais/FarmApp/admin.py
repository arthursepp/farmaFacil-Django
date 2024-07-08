from django.contrib import admin
from .models import Usuario, Farmacia, Produto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Farmacia)
admin.site.register(Produto)
