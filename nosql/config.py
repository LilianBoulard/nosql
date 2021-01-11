# -*- coding: UTF8 -*-


class Config:
    # Length ID
    id_len: int = 16

    # The range in which we want to cast the hash.
    hash_range: int = 100

    # Absolute or relative path to a directory, where database files will be stored.
    # Created on the fly if not already existing.
    databases_directory = "db/"
