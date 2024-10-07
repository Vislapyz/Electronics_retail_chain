from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели User с помощью метода ViewSet"""
    serializer_class = UserSerializer
    # Получаем все данне из БД
    queryset = User.objects.all()
