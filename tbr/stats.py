from typing import List, Optional

import numpy as np  # type: ignore

from tbr.loader import Summary


def current_mean(summaries: List[Summary], fraction=0.1) -> Optional[float]:
    if len(summaries) == 0:
        return None

    last_part = max(1, int(len(summaries) * fraction))

    return np.mean(summaries[-last_part:])
