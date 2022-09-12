from .BaseRepository import BaseRepository
from src.models import Contact


class ContactRepository(BaseRepository):
    def __init__(self):
        self.model = Contact
