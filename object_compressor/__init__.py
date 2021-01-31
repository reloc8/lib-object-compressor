import zlib
import pickle

from base64 import b64decode, b64encode
from typing import Any, Type, TypeVar


A = TypeVar('A')


def compress(object_: Any, to_string: bool = True) -> Type[A]:
    """Compresses a picklable object

    :param object_:     Object to compress
    :param to_string:   If True the compressed object is base-64 encoded
    :return:            The compressed object
    :raises ValueError: If object is not picklable
    """

    try:
        object_ = pickle.dumps(object_)
    except AttributeError:
        raise ValueError

    compressed = zlib.compress(object_)

    return b64encode(compressed).decode('utf-8') if to_string else compressed


def decompress(object_: Type[A], from_string: bool = True) -> Any:
    """Decompresses an object

    :param object_:     Object to decompress
    :param from_string: If True the compressed object is base-64 decoded
    :return:            The decompressed object
    """

    return pickle.loads(zlib.decompress(b64decode(object_.encode('utf-8')) if from_string else object_))
