from mongoengine import IntField
from mongoengine import Document
from mongoengine import ListField
from mongoengine import FloatField
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import ReferenceField


class ImageBuffer(Document):
    is_cover = BooleanField(default=False)
    original_image = StringField()
    thumbnail_url = StringField()
    large_url = StringField()
    small_url = StringField()
    medium_url = StringField()
    optimized_url = StringField()


class DimensionBuffer(Document):
    type = StringField(default='basic')
    height = FloatField()
    width = FloatField()
    depth = FloatField()
    measurement_qualifier = StringField()


class EditionBuffer(Document):
    size = StringField()
    number = StringField()
    description = StringField()


class CollectableBuffer(Document):
    title = StringField()
    member_id = IntField()
    description = StringField()
    collectable_type = StringField()
    creation_date_start = DateTimeField()
    creation_date_end = DateTimeField()
    provenance = StringField()
    medium = StringField()
    signature_description = StringField()

    editions = ListField(ReferenceField(EditionBuffer, dbref=False))
    dimensions = ListField(ReferenceField(DimensionBuffer, dbref=False))
    images = ListField(ReferenceField(ImageBuffer, dbref=False))


class NameBuffer(Document):
    member_id = IntField()
    full_name = StringField()
    first_name = StringField()
    last_name = StringField()


class EmailBuffer(Document):
    member_id = IntField()
    email = StringField()
    priority = IntField(default=0)
    is_verified = BooleanField()


class PhoneBuffer(Document):
    member_id = IntField()
    phone_number = StringField()
    priority = IntField(default=0)


class WebLocationBuffer(Document):
    member_id = IntField(default=0)
    url = StringField()
    priority = IntField(default=0)


class SocialMediaNameBuffer(Document):
    member_id = IntField(default=0)
    name = StringField()
    type = StringField()


class GeoLocationBuffer(Document):
    member_id = IntField(default=0)
    street_name = StringField()
    priority = IntField()
    post_town = StringField()
    state = StringField()
    postal_code = StringField()
    country = StringField()


class ContactBuffer(Document):
    member_id = IntField(default=0)
    is_company = BooleanField(default=True)
    department = StringField()
    job_title = StringField()

    phones = ListField(ReferenceField(PhoneBuffer, dbref=False))
    emails = ListField(ReferenceField(EmailBuffer, dbref=False))
    names = ListField(ReferenceField(NameBuffer, dbref=False))
    web_locations = ListField(ReferenceField(WebLocationBuffer, dbref=False))
    geo_locations = ListField(ReferenceField(GeoLocationBuffer, dbref=False))
    social_media_names = ListField(ReferenceField(SocialMediaNameBuffer, dbref=False))


class UserBuffer(Document):
    member_id = IntField(default=0)
    name = StringField()
    email = StringField()

    contacts = ListField(ReferenceField(ContactBuffer, dbref=False))
    phones = ListField(ReferenceField(PhoneBuffer, dbref=False))
    emails = ListField(ReferenceField(EmailBuffer, dbref=False))
    web_locations = ListField(ReferenceField(WebLocationBuffer, dbref=False))
    social_media_names = ListField(ReferenceField(SocialMediaNameBuffer, dbref=False))


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
