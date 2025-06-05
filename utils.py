from datetime import datetime
import pytz

def convert_ist_to_timezone(dt: datetime, target_tz: str):
    ist = pytz.timezone("Asia/Kolkata")
    dt = ist.localize(dt)
    return dt.astimezone(pytz.timezone(target_tz))