from io import BufferedReader
from typing import Union


def dos2unix(x: Union[BufferedReader, bytes]) -> bytes:
    """
    Convert a DOS (CRLF) file to a Unix (LF) file.
    :x: The file handle (mode must be "rb" or "rb+") or byte array.
    :return: The converted contents of the file.
    """
    if isinstance(x, bytes):
        return _pydos2unix_bytes(x, b"\x0A")
    else:
        return _pydos2unix_io(x, b"\x0A")


def unix2dos(x: Union[BufferedReader, bytes]) -> bytes:
    """
    Convert a Unix (LF) file to a DOS (CRLF) file.
    :x: The file handle (mode must be "rb") or byte array.
    :return: The converted contents of the file.
    """
    if isinstance(x, bytes):
        return _pydos2unix_bytes(x, b"\x0D\x0A")
    else:
        return _pydos2unix_io(x, b"\x0D\x0A")


def _pydos2unix_bytes(x: bytes, lineend: bytes) -> bytes:
    return b"".join(line + lineend for line in x.splitlines())


def _pydos2unix_io(x: BufferedReader, lineend: bytes) -> bytes:
    if "rb" not in x.mode:
        raise TypeError("BufferedReader must be in read bytes mode")

    return b"".join(line + lineend for line in x.read().splitlines())
