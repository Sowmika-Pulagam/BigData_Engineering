from logger import logging

def add(a,b):
    logging.debug("The add operation is taking place")
    return a+b

logging.debug("The add function is being called")
add(10,15)