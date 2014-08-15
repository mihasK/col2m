import json

import settings
import urllib2


def get_artists(name):
    return json.load(urllib2.urlopen(
            '{domain}/v1/subjects/suggest_completion?query={name}&type=Artists'.format(
                name=name.encode('utf-8'), domain=settings.REFERENCE_DATA_HOST)))

def find(name):
    result = set.intersection(*[
        set((json.dumps(resp) for resp in get_artists(name)))
        for name in name.split()
    ])

    return [json.loads(item) for item in result]
