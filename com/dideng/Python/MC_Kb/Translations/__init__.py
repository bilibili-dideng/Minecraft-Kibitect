# com/dideng/Python/MC_Kb/GUI/Translations/__init__.py

import json
import os
from typing import Literal, Dict

from com.dideng.Python.MC_Kb.logger import info, error, debug

# 支持的语言
LanguageType = Literal["en_us", "zh_cn"]

# 获取项目根目录
ROOT_DIR = os.getcwd()
LANG_DIR = os.path.join(ROOT_DIR, "data", "lang")

translation_table:dict[str, str] = {}
Attempts = 0
print = "123"
def load_language(language: LanguageType) -> Dict[str, str]:
    """
    加载语言文件，返回翻译表
    """
    file_path = os.path.join(LANG_DIR, f"{language}.json")
    info(f"正在加载: {file_path}")
    def Does_it_exist(file_path):
        global Attempts
        if not os.path.exists(file_path):
            info(f"文件不存在: {file_path}")
            if Attempts == 1:
                return {}
            info("二次尝试")
            ROOT_DIR = os.path.abspath(__file__)
            LANG_DIR = os.path.join(ROOT_DIR, "data", "lang")
            file_path = os.path.join(LANG_DIR, f"{language}.json")
            debug(f"正在加载: {file_path}")
            Attempts += 1
            Does_it_exist(file_path)

    Does_it_exist(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read().strip()
            debug(f"文件内容 (repr): {repr(content[:200])}")

            data = json.loads(content)
            if not isinstance(data, dict):
                error("解析结果不是字典")
                return {}

            debug(f"成功加载 {len(data)} 个词条")
            return data  # 直接返回，不依赖 global

    except Exception as e:
        error(f"加载失败: {e}")
        return {}


def tr(key: str, translation_table: Dict[str, str], default: str = None) -> str:
    """
    翻译函数
    :param key: 翻译键
    :param translation_table: 翻译表（由 load_language 返回）
    :param default: 默认值
    :return: 翻译结果
    """
    debug(translation_table)
    value = translation_table.get(key)
    if value is not None:
        info(f"找到翻译: '{value}'")
        return value
    else:
        info(f"未找到 '{key}'，返回默认值: '{default}'")
        return default or key