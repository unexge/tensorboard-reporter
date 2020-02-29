from typing import List, Optional

import numpy as np  # type: ignore

from tensorboard_reporter.summary import Summary


def current_mean(summaries: List[Summary], fraction: float = 0.1) -> Optional[float]:
    if len(summaries) == 0:
        return None

    last_part = max(1, int(len(summaries) * fraction))

    return float(np.mean(list(map(lambda x: x.value, summaries[-last_part:]))))
