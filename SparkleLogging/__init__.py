from SparkleLogging.utils._logger import LogManager ,DEFAUIT_FOMATTER
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL,FATAL ,Formatter

class 符玄: ...

__version__ = "1.1.0"

c = 符玄()

# 默认的日志记录器
logger = LogManager.GetLogger(
    log_name='main',
    setConsoleLevel=DEBUG,
    setFileLevel=INFO,
    setWebsocketLevel=INFO,
    setHTTPLevel=INFO,
    out_to_console=True,
    web_log_mode=False,
    WSpost_url="",
    HTTPpost_url="",
    http_mode=False,
    custom_formatter=DEFAUIT_FOMATTER
)