# TensorBoard Reporter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![PyPI Link https://pypi.org/project/tensorboard-reporter/](https://img.shields.io/pypi/v/tensorboard-reporter)](https://pypi.org/project/tensorboard-reporter/)

Get reports for your training process via Slack.

## Setup

Install TensorBoard Reporter from pip

```bash
pip install tensorboard-reporter
```

Configure your report

```bash
SLACK_BOT_TOKEN="xoxb-abc-1232" tensorboard-reporter \
 --run_dir ./runs/Mar10_15-00-24_ip-127-0-0-1 \
 --tag "Test/loss" --tag "Train/loss" \
 --interval_hour 1 --slack_channels "#tensorboard-reports"
```

And get reports to your Slack periodically

![Example](./example.png)
