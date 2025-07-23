import logging, os, datetime
def setup_logger(name="app", log_dir="logs"):
    os.makedirs(log_dir, exist_ok=True)
    log_filename = datetime.datetime.now().strftime(f"{name}_%Y-%m-%d.log")
    log_path = os.path.join(log_dir, log_filename)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Ghi cả DEBUG trở lên
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
    return logger