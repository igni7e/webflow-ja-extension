#!/usr/bin/env python3
# シンプルなアイコン画像を作成するスクリプト

import struct

def create_png(width, height, color_r, color_g, color_b):
    """Create a simple solid color PNG image"""

    # PNG signature
    png_signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr_crc = 0  # Simplified, actual CRC calculation omitted
    ihdr_chunk = struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)

    # IDAT chunk - simplified single color
    # For a proper implementation, we'd need zlib compression
    # Using a workaround with base64 encoded minimal PNG

    return png_signature + ihdr_chunk

# Better approach: use base64 encoded minimal PNGs
import base64

# Blue icon with "W" letter (Webflow)
# These are minimal valid PNG files created externally and base64 encoded

# 16x16 blue icon
icon16_base64 = """
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAKklEQVR42mNk+M/wn4EIwDgyStKI
QV5BngEJjJI0YpBXkGdAAqMkDTcAALBnBQHqHQK3AAAAAElFTkSuQmCC
"""

# 48x48 blue icon
icon48_base64 = """
iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAALklEQVR42u3OQQ0AAAgDIL/6lwaI
qQHMYPbH9kWAAQMGDBgwYMCAAQMGDBgwYOAHA+YEAfZjQWIAAAAASUVORK5CYII=
"""

# 128x128 blue icon
icon128_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAMElEQVR42u3BAQEAAACCIP+vbkhA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwGaQoAAXxJdL4AAAAASUVORK5CYII=
"""

# Write icon files
with open('icon16.png', 'wb') as f:
    f.write(base64.b64decode(icon16_base64.strip()))

with open('icon48.png', 'wb') as f:
    f.write(base64.b64decode(icon48_base64.strip()))

with open('icon128.png', 'wb') as f:
    f.write(base64.b64decode(icon128_base64.strip()))

print("Icons created successfully!")
print("Note: These are minimal placeholder icons.")
print("For production, please create proper icons with 'W' or 'WJ' text.")
