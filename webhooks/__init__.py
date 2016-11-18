import re

import requests

DEFAULT_TIMEOUT = 10

__all__ = ["IncomoingWebhook"]


class IncomingWebhook(object):
    """
    https://api.slack.com/incoming-webhooks
    https://api.slack.com/docs/message-formatting
    """

    def __init__(self, url=None, timeout=DEFAULT_TIMEOUT):
        self.url = url
        self.timeout = timeout

    def post(self, data):
        """
        Posts message with payload formatted in accordance with
        this documentation https://api.slack.com/incoming-webhooks
        """
        if not self.url:
            raise Exception('URL for incoming webhook is undefined')

        resp = requests.post(self.url, json=data,
                             timeout=self.timeout)
        if resp.ok:
            return resp
        else:
            raise Exception(resp.text)

    def message(self, text,
                pretext=None,
                username=None,
                icon_emoji=None,
                icon_url=None,
                channel=None,
                mrkdwn=True,
                mrkdwn_in=None):
        """
        :param str text: The message text
        :param str text: The message text
        :param str username: The username to use
        :param str icon_emoji: The icon emoji to use
        :param str icon_url: The icon url to use
        :param str channel: The channel or user to post to
        :param bool mrkdwn: Whether or not to enable markdown formatting
        :param list mrkdwn_in: Fields in which to enable markdown formatting
        :raise Exception: icon_emoji and icon_url cannot be used together
        :raise Exception: icon_emoji must start and end with colons
        :raise Exception: mkrdwn_in has invalid fields
        """
        data = {
            "text": text,
        }
        if pretext:
            data["pretext"] = pretext
        if username:
            data["username"] = username
        if icon_emoji and icon_url:
            raise Exception("Please provide either icon_emoji or icon_url, not both")  # noqa
        if icon_emoji:
            if not re.match(r'^:[\w-]+:$', icon_emoji):
                raise Exception("Please provide a valid emjoi")
            data["icon_emoji"] = icon_emoji
        if icon_url:
            data["icon_url"] = icon_url
        if channel:
            data["channel"] = channel
        if not mrkdwn:
            data["mrkdwn"] = mrkdwn
        if isinstance(mrkdwn_in, (list, tuple)):
            valid_mrkdwn_fields = ("pretext", "text", "fields")
            if (set(mrkdwn_in) <= valid_mrkdwn_fields):
                data["mrkdwn_in"] = mrkdwn_in
            else:
                diff = set(mrkdwn_in) - valid_mrkdwn_fields
                raise Exception("Invalid fields: {}".format(', '.join(diff)))
        return self.post(data)
