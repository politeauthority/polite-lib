"""
    Quigley Notify
    Example method for sending a notification to the Quigley Api

"""
import json
import logging
import os

import requests


BASIC_AUTH = os.environ.get("QUIGLEY_API_BASIC_AUTH")


def send_notification(
        message: str, 
        message_unformatted: str = None,
        route: str = None,
        room_id: str = None
    ):
    """Send a notifcation to the Quigley Api. This requires QUIGLEY_API_BASIC_AUTH env var to be
    set.

    :param message: (str) Message to be sent, this can contain html.
    :param message_unformatted: (str) message to be sent, this will show up in push notifications
        and shouldnt be formated.
    :param room_id: (str) The full url for the Matrix room to send the message. 
            Note: the bot must be invited and accepted the room invite.
            Example: !WVaUYDOloEvKklWuhG:squid-ink.us
    """
    if not BASIC_AUTH:
        print("ERROR: Missing env var: QUIGLEY_API_BASIC_AUTH")
        return False
    API_URL = "https://api.alix.lol"
    if not route:
        route = "notify"
    headers = {
        "Authorization": "Basic %s" % BASIC_AUTH,
        "Content-Type": "application/json"
    }
    data = {
        "message": message_unformatted,
        "message_formatted": message
    }
    response = requests.post(
        "%s/%s" % (API_URL, route),
        data=json.dumps(data),
        headers=headers)
    
    if response.status_code not in [200, 201]:
        logging.error("Error sending notification: %s" % response.text)
        return False
    else:
        logging.info("Notification sent successfully: %s response.json()")
        return True


# End File: polite-lib/src/polite_lib/notify/quigley_notify.py
