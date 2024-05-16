#!/usr/bin/env python3
""" Redis module """

from uuid import uuid4
import redis
from typing import Union


class Cache():
    """ Redis class """
    def __init__(self) -> None:
        """ start the redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store the input data in Redis and return the key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
