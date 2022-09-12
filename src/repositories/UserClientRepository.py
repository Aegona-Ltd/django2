from .BaseRepository import BaseRepository
from src.models import UserClient


class Repository(BaseRepository):
    def __init__(self):
        self.model = UserClient
