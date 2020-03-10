from typing import NamedTuple, Optional, Callable, List
from datetime import datetime


class Summary(NamedTuple):
    wall_time: float
    step: int
    value: float
    tag: str


def wall_time_in_range(
    *, min: Optional[datetime], max: Optional[datetime]
) -> Callable[[Summary], bool]:
    def predicate(x: Summary) -> bool:
        if min is not None and min.timestamp() > x.wall_time:
            return False

        if max is not None and max.timestamp() < x.wall_time:
            return False

        return True

    return predicate


def tag(tag: str) -> Callable[[Summary], bool]:
    return lambda x: x.tag == tag


def tags(tags: List[str]) -> Callable[[Summary], bool]:
    return lambda x: x.tag in tags
