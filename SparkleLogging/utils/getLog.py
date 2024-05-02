from SparkleLogging.utils.plugins_for_core import *

FOMATTER = '[%(asctime)s.%(msecs)d| %(levelname)-8s |%(threadName)s|%(name)s.%(funcName)s|%(filename)s:%(lineno)d]: %(message)s'

class LogManager:
    def __init__(self) -> None:
        self.public_formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)d| %(levelname)-8s |%(threadName)s|%(name)s.%(funcName)s|%(filename)s:%(lineno)d]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def GetLogger(self, log_name: str = "default",
                  setConsoleLevel: int = logging.DEBUG,
                  setFileLevel: int = logging.INFO,
                  setWebsocketLevel: int = logging.INFO,
                  setHTTPLevel: int = logging.INFO,
                  out_to_console: bool = True,
                  web_log_mode: bool = False,
                  WSpost_url: str = "",
                  HTTPpost_url: str = "",
                  http_mode: bool = False,
                  custom_formatter: logging.Formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)d| %(levelname)-8s |%(threadName)s|%(name)s.%(funcName)s|%(filename)s:%(lineno)d]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )):
        # 确保日志名称有效
        log_name = log_name if log_name else "default"
        if out_to_console:
            log_folder = f'./logs/{log_name}'
            if not os.path.exists(log_folder):
                os.makedirs(log_folder, exist_ok=True)

        logger = logging.getLogger(log_name)
        if logger.hasHandlers():
            # Logger已经配置过处理器，避免重复配置
            return logger

        # 颜色配置
        log_color_config = {
            'DEBUG': 'bold_blue', 'INFO': 'bold_cyan',
            'WARNING': 'bold_yellow', 'ERROR': 'red',
            'CRITICAL': 'bold_red', 'RESET': 'reset',
            'asctime': 'green'
        }
        if out_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(setConsoleLevel)
            console_formatter = colorlog.ColoredFormatter(
                fmt='%(log_color)s [%(asctime)s.%(msecs)d| %(levelname)-8s |%(threadName)s|%(name)s.%(funcName)s|%(fileName)s:%(lineno)d]: %(message)s %(reset)s',
                datefmt='%H:%M:%S',
                log_colors=log_color_config
            )
            if custom_formatter:
                console_formatter = custom_formatter

            if isinstance(console_handler, logging.StreamHandler):
                console_formatter = colorlog.ColoredFormatter(fmt=f"%(log_color)s {console_formatter._fmt} %(reset)s",datefmt=console_formatter.datefmt, log_colors=log_color_config)
                console_handler.setFormatter(console_formatter)

            logger.setLevel(setConsoleLevel)
            logger.addHandler(console_handler)

        
        file_handler = TimedRotatingFileHandler(f'./logs/{log_name}/{log_name}.log',encoding="utf-8", when='midnight', interval=1, backupCount=7)
        file_handler.setLevel(setFileLevel)
        file_handler.setFormatter(self.public_formatter)

        if custom_formatter:
            file_handler.setFormatter(custom_formatter)

        # 检查代码是否在异步环境中运行
        if asyncio.iscoroutinefunction(logging.Handler.emit):
            queue = asyncio.Queue()
            queue_handler = QueueHandler(queue)
            queue_listener = QueueListener(queue, file_handler)
            logger.addHandler(queue_handler)
            asyncio.ensure_future(queue_listener.start())
        else:
            logger.addHandler(file_handler)

        if web_log_mode and WSpost_url:
            websocket_handler = WebsocketHandler(WSpost_url)
            websocket_handler.setLevel(setWebsocketLevel)
            formatter = self.public_formatter
            if custom_formatter:
                formatter = custom_formatter
            websocket_handler.setFormatter(formatter)
            logger.addHandler(websocket_handler)

        if http_mode and HTTPpost_url:
            # 检查代码是否在异步环境中运行
            if asyncio.iscoroutinefunction(logging.Handler.emit):
                async_http_hander = AsyncHTTPhandler(HTTPpost_url)
                async_http_hander.setLevel(setHTTPLevel)
                formatter = self.public_formatter
                if custom_formatter:
                    formatter = custom_formatter
                async_http_hander.setFormatter(formatter)
                logger.addHandler(async_http_hander)
            http_handler = HTTPhandler(HTTPpost_url)
            http_handler.setLevel(setHTTPLevel)
            formatter = self.public_formatter
            if custom_formatter:
                formatter = custom_formatter
            http_handler.setFormatter(formatter)
            logger.addHandler(http_handler)

        return logger