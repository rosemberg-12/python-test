
import base64
import typing


def _build_default_headers(params: typing.Dict[str,typing.Any]):
    headers={
            "Accept": "value",
            "content-type": "value",
            **params
    }
    return headers

other_dict={
    "test": "Test"
}

print (_build_default_headers(other_dict))