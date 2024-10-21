import logging

# Configure logging only once
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='basic_logger.log',
    filemode='w'  # Use 'w' to overwrite the log file or 'a' to append
)

# Log messages at different levels
logging.debug("Debug message")
logging.info("Informative message")
logging.error("Error message")

# Create a custom logger
LogWithLevelName = logging.getLogger('myLoggerSample')
LogWithLevelName.setLevel(logging.INFO)

# Log messages using the custom logger
LogWithLevelName.debug("This debug message will not be shown since the level is set to INFO.")
LogWithLevelName.info("This is an informative message from my custom logger.")
LogWithLevelName.error("This is an error message from my custom logger.")
