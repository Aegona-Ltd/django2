from .BaseRepository import BaseRepository
from src.models import UserClient


class UserClientRepository(BaseRepository):
    def __init__(self):
        self.model = UserClient
