import aiogram.types.contact
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class Contact(StatesGroup):
    name = State()
    phone = State()
    username = State()
    gifted = False

    def __init__(self, gifted):
        self.gifted = gifted


class CommercialContact(Contact):

    def __init__(self, gifted):
        Contact.__init__(self, gifted)


class ChildrenContact(Contact):
    order = str()
    children_count = State()
    age = State()

    def __init__(self, gifted):
        Contact.__init__(self, gifted)


class AdultContact(Contact):

    def __init__(self, gifted):
        Contact.__init__(self, gifted)


class Mailing(StatesGroup):
    text = State()
    photo = State()