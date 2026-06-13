import logging

# configure logging settings
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"), 
        logging.StreamHandler(), 
    ]
)

logger = logging.getLogger("arthimeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"Addition {a} + {b}= {result}")
    return result

def sub(a,b):
    result = a - b
    logger.debug(f"Subtraction {a} - {b}= {result}")
    return result

def mul(a,b):
    result = a - b
    logger.debug(f"Multiplication {a} * {b}= {result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None



add(10,15)
sub(15,10)
mul(10,20)
divide(20,0)