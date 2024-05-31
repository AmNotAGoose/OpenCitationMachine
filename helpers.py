from datetime import datetime


def is_iso_string(string):
    try:
        datetime.fromisoformat(string)
    except:
        return False
    return True


def iso_to_dmy(iso_string):
    dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
    formatted_date = dt.strftime("%d-%m-%Y")
    return formatted_date
