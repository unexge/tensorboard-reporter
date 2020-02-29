from typing import Iterable, Dict, List
import os
from glob import glob
from collections import defaultdict

import tensorflow as tf  # type: ignore
from tensorflow.core.util import event_pb2  # type: ignore

from tensorboard_reporter.summary import Summary


def load_summaries(run_dir: str) -> Iterable[Summary]:
    event_files = glob(os.path.join(run_dir, "*.tfevents.*"))

    it = filter(
        lambda x: x.WhichOneof("what") == "summary",
        map(
            lambda x: event_pb2.Event.FromString(x.numpy()),  # type: ignore
            tf.data.TFRecordDataset(event_files),
        ),
    )

    for elem in it:
        for value in elem.summary.value:
            if value.WhichOneof("value") == "simple_value":
                yield Summary(
                    wall_time=elem.wall_time,
                    step=elem.step,
                    tag=value.tag,
                    value=value.simple_value,
                )
            elif value.WhichOneof("value") == "tensor":
                try:
                    yield Summary(
                        wall_time=elem.wall_time,
                        step=elem.step,
                        tag=value.tag,
                        value=float(tf.make_ndarray(value.tensor)),
                    )
                except ValueError:
                    continue


def group_by_tag(summaries: Iterable[Summary]) -> Dict[str, List[Summary]]:
    tags: Dict[str, List[Summary]] = defaultdict(list)

    for summary in summaries:
        tags[summary.tag].append(summary)

    return tags
