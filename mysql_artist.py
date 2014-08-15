from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Table
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import settings

Model = declarative_base()
mysql_engine = create_engine('postgres://zobzgeddxcapwp:gQvhHVvFqORe6dsDqUUwLfAqhd@ec2-54-197-241-96.compute-1.amazonaws.com:5432/d2efq4ja8ot0s9')
Session = scoped_session(sessionmaker(bind=mysql_engine))


class Artist(Model):
    __tablename__ = 'collectrium_artist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    name_index = Column(String(255))
    name_normalized = Column(String(255))
    name_search = Column(String(255))
    photo = Column(String(255))
    biography = Column(String(255))
    biography_full = Column(String(255))
    sex = Column(String(10))
    birth_date = Column(Integer)
    death_date = Column(Integer)
    is_approved = Column(Boolean, server_default='FALSE')
    number = Column(String(11))
    source = Column(String(200))
    source_id = Column(Integer)
    website = Column(String(255))
    company = Column(String(255))
    galleries = Column(String(255))
    desc1 = Column(String(255))
    extra = Column(LONGTEXT)
    create_time = Column(DateTime)
    is_curated = Column(Integer)
    import_id = Column(String(255))
