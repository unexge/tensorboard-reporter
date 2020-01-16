from typing import Dict, Iterable, List
from collections import defaultdict

import numpy as np  # type: ignore

from tbr.loader import Summary


def running_mean(x, N):
    """
    taken from https://stackoverflow.com/a/27681394
    """
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)


def group_by_tag(summaries: Iterable[Summary]) -> Dict[str, List[Summary]]:
    tags: Dict[str, List[Summary]] = defaultdict(list)

    for summary in summaries:
        tags[summary.tag].append(summary)

    return tags
