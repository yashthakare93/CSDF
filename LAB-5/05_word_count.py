import logging

def word_count(myfile):
    logging.basicConfig(
        level=logging.DEBUG,
        filename='word_count_logger.log',
        format='%(asctime)s %(levelname)s: %(message)s',
        filemode='w'
    )

    try:
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split()
            num_words = len(words)
            logging.debug("This file has %d words", num_words)
            return num_words
    except OSError as e:
        logging.error("Error reading the file: %s", e)
        return None  # Return None to indicate an error occurred

if __name__ == "__main__":
    count = word_count("words.txt")
    if count is not None:
        print(f"The file contains {count} words.")
    else:
        print("An error occurred while counting words.")
