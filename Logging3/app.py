import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log', mode='w')
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)
console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


console_handler.warning("You are given a warning")
file_handler.info('you have info')