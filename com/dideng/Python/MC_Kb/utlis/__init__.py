# utils.py
import locale

def auto_detect_language() -> str:
    try:
        lang = locale.getdefaultlocale()[0]
        return "zh_cn" if lang.startswith("zh") else "en_us"
    except Exception:
        return "en_us"