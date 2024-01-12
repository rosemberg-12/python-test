import functools
from typing import Any, Callable, Dict, Optional, TypeVar, cast

_DecoratedFunc = TypeVar("_DecoratedFunc", bound=Callable[..., Any])


def transactional_log(
    method: str, path: str, params: Optional[Dict[str, Any]] = None
) -> Callable[[_DecoratedFunc], _DecoratedFunc]:
    def decorator(func: _DecoratedFunc) -> _DecoratedFunc:
        @functools.wraps(func)
        def on_call(self: Any, *args: Any, **kwargs: Any) -> Any:
            print(f"Entra {method}-{path}")
            result = func(self, *args, **kwargs)
            print(f"Sale {method}-{path}")
            return result

        return cast(_DecoratedFunc, on_call)

    return decorator


@transactional_log(method="GET", path="/kyc")
def a():
    print("Entra A")


class Test:
    def __init__(self) -> None:
        pass

    @transactional_log(method="POST", path="/kyc")
    def b(self: "Test", value: str):
        print("Entra B")
        print(value)


test = Test()
test.b(value="valor")
