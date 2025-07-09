import time
from datetime import datetime
from typing import Union

def now_in_num(ago_seconds:int=0) -> int:
  """
  Returns the current timestamp in milliseconds since epoch.
  This format is compatible with Binance API requests.
  
  Returns:
    int: Current timestamp in milliseconds
  """
  return int(time.time() * 1000) - ago_seconds * 1000

def timestamp_to_datetime(timestamp: Union[int, float]) -> datetime:
  """
  Converts a Binance timestamp (milliseconds since epoch) to a datetime object.
  
  Args:
    timestamp (Union[int, float]): Timestamp in milliseconds
    
  Returns:
    datetime: Converted datetime object
  """
  # Convert milliseconds to seconds for datetime
  return datetime.fromtimestamp(timestamp / 1000)

def datetime_to_timestamp(dt: datetime) -> int:
  """
  Converts a datetime object to a Binance timestamp (milliseconds since epoch).
  
  Args:
    dt (datetime): Datetime object to convert
    
  Returns:
    int: Timestamp in milliseconds
  """
  return int(dt.timestamp() * 1000)