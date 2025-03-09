import concurrent.futures
import json
import logging
import time

logger = logging.getLogger(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        logger.exception(f"File '{file_path}' not found.")
        raise e
    except json.JSONDecodeError as e:
        logger.exception(f"Invalid JSON format in file '{file_path}'.")
        raise e
    except Exception as e:
        logger.exception(f"An error occurred while reading the file: {e}")
        raise e


def update_json_file(file_path, key, new_value):
    logger.info(f"Updating JSON file: '{file_path}'..")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # Update the value for the given key
        data[key] = new_value
        
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        
        logger.info(f"JSON file updated successfully in '{file_path}'.")
    except FileNotFoundError as e:
        logger.exception(f"File '{file_path}' not found.")
        raise e
    except json.JSONDecodeError as e:
        logger.exception(f"Invalid JSON format in file '{file_path}'.")
        raise e
    except Exception as e:
        logger.exception(f"An error occurred while updating the file: {e}")
        raise e
    
    
class ExecutionTimeMeasurer():

    def start(self):
        self._start_time = time.time()


    def get_elapsed_time(self):
        self._end_time = time.time()
        self._elapsed_time = self._end_time - self._start_time
        return self._elapsed_time
    

class CustomThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_running = True


    def shutdown(self, wait=True):
        super().shutdown(wait)
        self._is_running = False


    def is_running(self):
        return self._is_running


# class StoppableThread(threading.Thread):

#     def __init__(self,  *args, **kwargs):
#         super(StoppableThread, self).__init__(*args, **kwargs)
#         self._stop_event = threading.Event()


#     def stop(self):
#         self._stop_event.set()


#     def is_stopped(self):
#         return self._stop_event.is_set()