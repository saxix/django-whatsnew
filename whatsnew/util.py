from types import StringTypes
import datetime
import pkg_resources
from whatsnew.models import WhatsNew
from django.db.models import Q
from .fields import Version

def display_message(request, package_name, cookie_name):
    today = datetime.datetime.today()

    last_seen = Version(request.COOKIES.get(cookie_name) or '0.0')
    current_version = Version(get_version(package_name))
    try:
        last = WhatsNew.objects.filter(enabled=True).filter(Q(expire__gte=today) | Q(expire=None)).latest()
        display = last.version.same(current_version) and last.version != last_seen
    except WhatsNew.DoesNotExist:
        display = False
    return display, last


def get_version(package_name):
    version = None
    try:
        version = pkg_resources.require(package_name)[0].version
    except pkg_resources.DistributionNotFound:
        module = __import__(package_name)
        try:
            func = getattr(module, 'get_version')
            version = func()
        except:
            for attempt in ('version', 'VERSION', '__version__'):
                try:
                    version = getattr(module, attempt)
                    if isinstance(version, (list, tuple)):
                        version = ".".join(version)
                except AttributeError:
                    pass

    if version:
        return str(version)
    else:
        raise pkg_resources.DistributionNotFound

