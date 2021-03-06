import urllib2
import logging
from mysql_artist import Artist
from mysql_artist import Session
from buffer_models import ArtistBuffer
from autocomplete import find
from flask import Flask
from flask import request


SLICE = 10
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)


@app.route('/hello')
def hello(self):
    return 'hello world'


@app.route('/')
def migrate():
    limit =  int(request.args.get('limit', 0))
    soffset =  int(request.args.get('offset', 0))

    artists = Session.query(Artist).order_by('id').limit(limit).offset(offset)
    logging.info('offset is: %s, limit is: %s' % (offset, limit))
    cnt = 0

    for artist in artists:
        cnt = cnt + 1
        ArtistBuffer.objects.create(
            artist_id=artist.id,
            name=artist.name,
            first_name=artist.first_name,
            last_name=artist.last_name,
            name_index=artist.name_index,
            name_normalized=artist.name_normalized,
            name_search=artist.name_search,
            photo=artist.photo,
            biography=artist.biography,
            biography_full=artist.biography_full,
            sex=artist.sex,
            birth_date=artist.birth_date,
            death_date=artist.death_date,
            is_approved=artist.is_approved,
            number=artist.number,
            source=artist.source,
            website=artist.website,
            company=artist.company,
            galleries=artist.galleries,
            desc1=artist.desc1,
            extra=artist.extra,
            is_curated=artist.is_curated,

            name_result=find(artist.name) if artist.name else None,
            last_name_result=find(artist.last_name) if artist.last_name else None,
            name_index_result=find(artist.name_index) if artist.name_index else None,
            first_name_result=find(artist.first_name) if artist.first_name else None,
            name_search_result=find(artist.name_search) if artist.name_search else None,
            name_normalized_result=find(artist.name_normalized) if artist.name_normalized else None
        )
        Session.expunge_all()
        if cnt % 10 == 0:
            logging.info('This is a log message. %s' % cnt)

        offset += SLICE
        urllib2.urlopen('http://calm-scrubland-3271.herokuapp.com/?offset=%s&limit=%s' % (offset, limit))
    return 'Migrated: %s' % cnt + limit


@app.route('/clear')
def clear():
    ArtistBuffer.objects.all().delete()
    return 'Cleared'
