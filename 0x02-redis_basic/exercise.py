#!/usr/bin/env python3
""" Redis module """

from uuid import uuid4
import redis
from typing import Union, Callable


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

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """ fn is used to convert the data back to the desired format. """
        if (fn):
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ convert value to str """
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """ convert value to int """
        return int(self._redis.get(key))
