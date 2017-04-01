#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Init signature: io.BytesIO(initial_bytes=b'')
Docstring:      Buffered I/O implementation using an in-memory bytes buffer.
Type:           type
"""

import io


b = io.BytesIO()
b.write(b'helloworld\n')
data = b.getvalue()
print(data)
