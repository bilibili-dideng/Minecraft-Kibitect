# ===== 彩色日志配置 =====
import os
import logging
import sys

# 导入 colorlog
import colorlog

LOG_DIR = os.getcwd() + "\\logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 定义日志颜色格式
log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',  # 红底白字
}

# 创建彩色格式器
formatter = colorlog.ColoredFormatter(
    fmt="[%(asctime)s] %(log_color)s%(levelname)s:%(reset)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors=log_colors_config,
    reset=True
)

# 配置日志
logger = logging.getLogger("Minecraft Kibitect")
logger.setLevel(logging.DEBUG)

# 避免重复添加 handler
if not logger.handlers:
    # 文件处理器（不带颜色，纯文本）
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, "Minecraft Kibitect--log.log"), encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(file_formatter)

    # 控制台处理器（带颜色）
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


def debug(msg):
    logger.debug(msg)

def info(msg):
    logger.info(msg)

def warning(msg):
    logger.warning(msg)

def error(msg):
    logger.error(msg)

def critical(msg):
    logger.critical(msg)