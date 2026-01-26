def strtobool(value):
    """Convert a string representation of truth to True or False.

    Replaces deprecated https://github.com/python/cpython/blob/3.10/Lib/distutils/util.py#L308
    """
    value = value.lower()
    if value in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    if value in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    raise ValueError(f"invalid truth value {value!r}")
