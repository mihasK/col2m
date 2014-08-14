import json
from mysql_artist import Artist
from mysql_artist import Session
from core.artist.autocomplete import find


def main():
    artists = Session.query(Artist).filter(Artist.name.isnot(None))[:1000]

    #all artists fields
    #name, name_index, last_name, name_search, name_normalized
    #if name is empty then: name_result = Null
    #else name_result = find(artist.name_result)

    with open('an.json', 'w') as f:
        f.write('[')
        for artist in artists:
            if artist.name and find(artist.name):
                result = find(artist.name)
                f.write(
                    json.dumps({'name': artist.name}, {'name_result': result}) + ','
                )

            elif artist.name_index and find(artist.name_index):
                result = find(artist.name)
                f.write(
                    json.dumps([{'name_index': artist.name_index}, {'name_index_result': result}]) + ','
                )

        f.write(']')


if __name__ == '__main__':
    main()
