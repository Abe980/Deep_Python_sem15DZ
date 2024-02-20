import logging

FORMAT = "{asctime} - {levelname}: {msg}"

logging.basicConfig(filename='logs.txt', filemode='w', encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger()