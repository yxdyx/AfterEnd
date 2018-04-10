from django.conf import settings
import base64

def upload_to(instance, filename):
    splitname = filename.split('.')
    namebase = base64.b64encode(splitname[0].encode('utf-8'))
    realname = str(namebase, 'utf-8') + '.' + splitname[len(splitname) - 1]
    return '/'.join([settings.STATIC_ROOT, 'images', 'chair', instance.chair_id, instance.img_year, realname])
