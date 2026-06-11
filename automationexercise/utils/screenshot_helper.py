import os
from datetime import datetime

def capture(page, name):

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    page.screenshot(
        path=f"screenshots/{name}_{timestamp}.png"
    )