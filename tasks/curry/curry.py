from typing import Callable, Any


def curry(
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any
) -> Callable[..., Any]:
    """
    Returns a new function with some arguments pre-applied.

    Args:
        func: The function to partially apply arguments to.
        *args: Positional arguments to pre-apply.
        **kwargs: Keyword arguments to pre-apply.

    Returns:
        A new function that takes the remaining arguments and calls `func`
        with both pre-applied and new arguments.
    """

    def curried(*new_args: Any, **new_kwargs: Any) -> Any:
        all_args = args + new_args
        all_kwargs = {**kwargs, **new_kwargs}
        return func(*all_args, **all_kwargs)

    return curried
