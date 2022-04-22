from datetime import datetime, timedelta


def get_indian_time():
    return datetime.utcnow() + timedelta(hours=5, minutes=30)
