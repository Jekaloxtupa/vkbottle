from . import base
import typing
from enum import Enum
from ..base import BaseModel
from vkbottle.types import objects


class Note(BaseModel):
    read_comments: int = None
    can_comment: "base.BoolInt" = None
    comments: int = None
    date: int = None
    id: int = None
    owner_id: int = None
    text: str = None
    text_wiki: str = None
    title: str = None
    view_url: str = None


class NoteComment(BaseModel):
    date: int = None
    id: int = None
    message: str = None
    nid: int = None
    oid: int = None
    reply_to: int = None
    uid: int = None