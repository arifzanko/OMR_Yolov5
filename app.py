from omrDetection.logger import logging
from omrDetection.exception import AppException
import sys

try:
    a = 3 / "str"

except Exception as e:
    raise AppException(e, sys)