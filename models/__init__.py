#!/usr/bin/python3
""" Initialize FileStorage Class for all models """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
