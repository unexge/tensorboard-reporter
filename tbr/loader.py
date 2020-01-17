from typing import Iterable, NamedTuple
import os
from glob import glob

import tensorflow as tf  # type: ignore
from tensorflow.core.util import event_pb2  # type: ignore


class Summary(NamedTuple):
    wall_time: float
    step: int
    value: float
    tag: str


def load_summaries(run_dir: str) -> Iterable[Summary]:
    event_files = glob(os.path.join(run_dir, "*.tfevents.*"))

    it = filter(
        lambda x: x.WhichOneof("what") == "summary",
        map(
            lambda x: event_pb2.Event.FromString(x.numpy()),
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
