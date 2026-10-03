"""Compatibility helper for GenLayer Direct Mode on Windows."""

import inspect
import os
import sys

if sys.platform == "win32":
    _unlink = os.unlink

    def _compat_unlink(path, *args, **kwargs):
        try:
            return _unlink(path, *args, **kwargs)
        except PermissionError:
            callers = [frame.filename.replace("\\", "/") for frame in inspect.stack()]
            if any(name.endswith("/gltest/direct/loader.py") for name in callers):
                return None
            raise

    os.unlink = _compat_unlink
