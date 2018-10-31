try:
    from MXshop.settings.pro import *
except ImportError:
    try:
        from MXshop.settings.dev import *
    except ImportError:
        from MXshop.settings.base import *

