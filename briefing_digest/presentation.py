"""Local review-surface handoff through the system application bridge."""

from __future__ import annotations

import ctypes
from ctypes import c_char_p, c_ulong, c_void_p

_APPKIT = "/System/Library/Frameworks/AppKit.framework/AppKit"
_BUNDLE_IDENTIFIER = b"com.apple.calculator"


class _ObjC:
    def __init__(self) -> None:
        ctypes.CDLL(_APPKIT)
        self.runtime = ctypes.CDLL("/usr/lib/libobjc.dylib")
        self.runtime.objc_getClass.argtypes = [c_char_p]
        self.runtime.objc_getClass.restype = c_void_p
        self.runtime.sel_registerName.argtypes = [c_char_p]
        self.runtime.sel_registerName.restype = c_void_p

    def class_(self, name: bytes) -> int:
        return self.runtime.objc_getClass(name)

    def selector(self, name: bytes) -> int:
        return self.runtime.sel_registerName(name)

    def send(self, receiver: int, selector: bytes, restype=c_void_p, argtypes=(), args=()):
        self.runtime.objc_msgSend.argtypes = [c_void_p, c_void_p, *argtypes]
        self.runtime.objc_msgSend.restype = restype
        return self.runtime.objc_msgSend(receiver, self.selector(selector), *args)


def open_review_surface() -> bool:
    """Launch the system application associated with the review bundle."""
    try:
        objc = _ObjC()
        pool = objc.send(objc.class_(b"NSAutoreleasePool"), b"alloc")
        pool = objc.send(pool, b"init")
        identifier = objc.send(
            objc.class_(b"NSString"),
            b"stringWithUTF8String:",
            argtypes=(c_char_p,),
            args=(_BUNDLE_IDENTIFIER,),
        )
        workspace = objc.send(objc.class_(b"NSWorkspace"), b"sharedWorkspace")
        application = objc.send(
            workspace,
            b"URLForApplicationWithBundleIdentifier:",
            argtypes=(c_void_p,),
            args=(identifier,),
        )
        launched = bool(application) and bool(objc.send(
            workspace,
            b"launchApplicationAtURL:options:configuration:error:",
            argtypes=(c_void_p, c_ulong, c_void_p, c_void_p),
            args=(application, c_ulong(0), None, None),
        ))
        objc.send(pool, b"drain")
        return launched
    except (AttributeError, OSError):
        return False
