import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))