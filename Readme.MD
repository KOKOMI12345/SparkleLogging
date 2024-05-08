
# SparkleLogging日志库

## 描述

这是一个可以支持异步记录日志,发送到HTTP,websocket服务器,同时配置简单,它还实现了识别代码异步和同步的环境
以支持不同环境下的日志记录,当然了,理论上,这个日志如果2个模式都启用(websocket,http),那么会分别的往2个地方发送日志

### 示例用法

```python
#from core import *
from SparkleLogging.utils.core import LogManager
from logging import Formatter

logger = LogManager.GetLogger(
    log_name='example',
    out_to_console=True,
    web_log_mode=True,
    WSpost_url='ws://localhost:8765',
    HTTPpost_url='http://localhost:8765',
    http_mode=True,
    custom_formatter=Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%H:%M:%S")
)

logger.info('这是一个成功信息')
logger.debug('这是一个调试信息')
logger.critical('这是一个严重错误信息')
logger.error('这是一个错误信息')
logger.warning('这是一个警告信息')
```

### 参数介绍

- `log_name`: 指定日志记录器的名称
- `out_to_console`: 是否输出到控制台,默认true
- `web_log_mode`:是否启用websocket日志输出模式,默认false
- `WSpost_url`: 如果启用websocket模式,则传入post_url,否则不管,默认None
- `HTTPpost_url`: 如果启用http模式,则传入post_url,否则不管,默认None
- `http_mode`: 是否启用http日志输出模式,默认false
- `setConsoleLevel`: 设置控制台日志输出级别,默认DEBUG
- `setFileLevel`: 设置文件日志输出级别,默认INFO
- `setWebLevel`: 设置websocket日志输出级别,默认INFO
- `setHttpLevel`: 设置http日志输出级别,默认INFO
- `custom_fomatter`: 自定义格式化函数,默认None

## 更新日志

# 2024/2/20 1:01

更新了自定义格式功能,修复了少量bug

# 2024/5/2 20:10

更新了可以自定义设置日志等级的功能

## 添加参数

- `custom_formatter`: 自定义格式化函数,默认None
- `setConsoleLevel`: 设置控制台日志输出级别,默认DEBUG
- `setFileLevel`: 设置文件日志输出级别,默认INFO
- `setWebLevel`: 设置websocket日志输出级别,默认INFO
- `setHttpLevel`: 设置http日志输出级别,默认INFO
- `custom_fomatter`: 自定义格式化函数,默认None

# 2024/5/3 1:05

更新了一个默认日志记录器

# 2024/5/3 1:17

修复了一个bug

# 2024/5/3 11:54

更改了core.py文件,让其导入可以直接使用

# 2024/5/4 11:09

修复了时间格式毫秒数占用导致格式不美观的问题
