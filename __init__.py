from datetime import datetime
from threading import Event, Thread
from functools import wraps


def chunk_generator(_list, size):
    for i in xrange(0, len(_list), size):
        yield _list[i:i+size]


def dict_path(dct, k, default=None):
    """
    Turns dotted 'path' into dict key.
    snippet.thumbnails.default ->
        dct['snippet']['thumbnails']['default']
    """
    parts = k.split('.')
    out = dct
    for p in parts:
        try:
            out = out[p]
        except KeyError:
            return default
    return out


def write_dict_path(dct, k, value):
    parts = k.split('.')
    valkey = parts.pop()
    out = dct
    for p in parts:
        try:
            out = out[p]
        except KeyError:
            out[p] = {}
            out = out[p]
    out[valkey] = value


def cron_daynumber(day):
    return {
        'sunday': 0,
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
    }[day.lower()]


def cron_to_python_daynumber(d):
    """
    cron day number to stupid python day number
    cron: Sunday: 0 - Saturday: 6
    python: Monday: 0 - Sunday: 6
    """
    return (d+6) % 7


def parse_cron(spec):
    return dict(zip(['minute', 'hour', 'day_of_month', 'month', 'day_of_week'], spec.split(' ')))


def cron(spec, dt=None):
    if isinstance(spec, basestring):
        cronspec = parse_cron(spec)
    else:
        cronspec = spec

    checks = []
    if dt is None:
        dt = datetime.utcnow()

    cronspec = dict(filter(lambda x: x[1] != '*', cronspec.items()))

    for k, v in cronspec.items():
        try:
            v = int(v)
        except ValueError:
            # This should only happen if day of week is a string
            v = cron_daynumber(v)

        if k == 'day_of_week' and dt.weekday() == cron_to_python_daynumber(v):
            checks.append(True)
        elif k == 'day_of_month' and dt.day == v:
            checks.append(True)
        elif k == 'month' and dt.month == v:
            checks.append(True)
        elif k == 'hour' and dt.hour == v:
            checks.append(True)
        elif k == 'minute' and dt.minute == v:
            checks.append(True)
        else:
            checks.append(False)

    return all(checks)


def set_interval(interval):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            stopped = Event()

            def loop():
                while not stopped.wait(interval):
                    f(*args, **kwargs)

            t = Thread(target=loop)
            t.daemon = True
            t.start()
            return stopped
        return wrapper
    return decorator
