# Slack Webhooks API Client

A small api for interacting with Slack Webhooks

## Example

```py
from webhooks import IncomingWebhook
webhook_url = `https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYYY/ZZZZZZZZZZZZZZZZZZZZZZZZ`
wh = IncomingWebhook(url=webhook_url)
r = wh.message('test message')
print(r.text)
```

## Installation

```sh
$ pip install slack-webhooks
```

or

```sh
$ python setup.py install
```

## Resources

- https://api.slack.com/incoming-webhooks
- https://api.slack.com/docs/message-formatting
