from mongoengine import IntField
from mongoengine import Document
from mongoengine import ListField
from mongoengine import FloatField
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import ReferenceField


class ArtistBuffer(Document):
    artist_id = IntField()
    member_id = IntField()
    name = StringField()
    first_name = StringField()
    last_name = StringField()
    name_index = StringField()
    name_normalized = StringField()
    name_search = StringField()
    photo = StringField()
    biography = StringField()
    biography_full = StringField()
    sex = StringField()
    birth_date = IntField()
    death_date = IntField()
    role_id = IntField()
    is_approved = BooleanField(default=False)
    create_time = DateTimeField()
    number = StringField()
    source = StringField()
    website = StringField()
    company = StringField()
    galleries = StringField()
    desc1 = StringField()
    extra = StringField()
    is_curated = IntField()

    name_result = ListField()
    name_index_result = ListField()
    last_name_result = ListField()
    name_search_result = ListField()
    name_normalized_result = ListField()
