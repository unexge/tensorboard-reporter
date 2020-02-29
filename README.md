# TensorBoard Reporter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Get reports for your training process via Slack.

```bash
SLACK_BOT_TOKEN="xoxb-abc-1232" tensorboard-reporter \
 --run_dir ./ray_results/PPO_your_env_2020-01-18_08-49-01gdbkyles \
 --tag ray/tune/episode_reward_mean \
 --interval_hour 1 --slack_channel "#tensorboard-reports"
```
