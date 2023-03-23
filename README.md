# pydos2unix

Convert DOS (CRLF) files to Unix (LF) files and vice vera, written in Python.

## Example Usage

```py
from pydos2unix import dos2unix, unix2dos

# Convert example.txt from CRLF to LF
with open("example1.txt", "rb") as src:
    buffer = dos2unix(src)
with open("example1.txt", "wb") as dest:
    dest.write(buffer)

# Convert a LF byte array to CRLF
with open("example2.txt", "wb") as dest:
    buffer = unix2dos(b"Line 1\nLine 2\nLine 3\n")
    dest.write(buffer)
```
