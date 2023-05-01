from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    # conjunto de datos
    queryset = Project.objects.all()
    # clases que tienen permisos de consulta
    permission_classes = [permissions.AllowAny]
    # determino como los vamos a serializar pasando nuestro serializador
    serializer_class = ProjectSerializer

