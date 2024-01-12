import functools
import time
from typing import Any, Callable, Dict, Optional, TypeVar, cast

import kyc_logger as log

_DecoratedFunc = TypeVar("_DecoratedFunc", bound=Callable[..., Any])


def transactional_log(
    route: str,
    params: Optional[Dict[str, Any]] = None,
) -> Callable[[_DecoratedFunc], _DecoratedFunc]:
    def decorator(func: _DecoratedFunc) -> _DecoratedFunc:
        @functools.wraps(func)
        def on_call(self: Any, *args: Any, **kwargs: Any) -> Any:
            _LOGGER = log.get_lambda_logger()
            _LOGGER.info("[%s] Operation Started", route)
            start = time.time()
            result = func(self, *args, **kwargs)
            _LOGGER.info(
                "[%s] Operation Finished, Elapsed time: %s seconds",
                route,
                time.time() - start,
            )
            return result

        return cast(_DecoratedFunc, on_call)

    return decorator


_stages_executors: Dict[str, int] = {}

example: str = _stages_executors.get("lo que sea")
