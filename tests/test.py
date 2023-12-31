"""
route="Gnm7nYfB2Ckw4UYTcUV"

"""
from polite_lib.notify import quigley_notify

MSG="<h1>hello world</h1>"
URL="https://api-dev.alix.lol"
ROOM_ID="!lYUxSzLlxYFiUkgYRJ:squid-ink.us"
ROOM_ID="!egljOPRjhdPSyYTvgg:squid-ink.us"


def run():
    # notify = quigley_notify.send_notification(
    #     MSG,
    #     url=URL
    # )
    print("sending to URL: %s" % URL)
    print("room_id: %s" % ROOM_ID)
    notify = quigley_notify.send_notification(
        MSG,
        room_id=ROOM_ID,
        url=URL
    )
    print(notify)


if __name__ == "__main__":
    run()

