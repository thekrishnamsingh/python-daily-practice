from logger_setup import setup_logger

logger = setup_logger()

def divide(a, b):
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attempted division by zero")
        return None


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(5, 0))
