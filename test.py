from SparkleLogging.utils.core import LogManager
from logging import Formatter

logger = LogManager.GetLogger(
    log_name='example',
    out_to_console=True,
    web_log_mode=True,
    WSpost_url='ws://localhost:8765',
    HTTPpost_url='http://localhost:8765',
    http_mode = True,
    custom_formatter=Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt="%H:%M:%S")
)

logger.info('这是一个成功信息')
logger.debug('这是一个调试信息')
logger.critical('这是一个严重错误信息')
logger.error('这是一个错误信息')
logger.warning('这是一个警告信息')