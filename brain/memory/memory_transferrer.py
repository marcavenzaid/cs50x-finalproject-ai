import shutil
import os
import time
import logging
import definitions

logger = logging.getLogger(__name__)

class MemoryTransferrer:
    
    def __init__(self):
        self._short_term_memory_folder_path = definitions.SHORT_TERM_MEMORY_LAST_THOUGHT_PATH
        self._long_term_memory_folder_path = definitions.LONG_TERM_MEMORY_PATH
        self._age_in_days_to_transfer = 1
        # self._age_in_days_to_transfer_in_seconds = self._age_in_days_to_transfer * 86400   # Convert days to seconds
        self._age_in_days_to_transfer_in_seconds = 120 # temporarily set to 120 seconds (2 minutes) for testing.


    def transfer_stm_to_ltm(self):
        """
        After a specific amount of time, transfers the file from the short-term memory folder to the long-term memory folder.
        """

        current_time = time.time()
        files_in_dir = os.listdir(self._short_term_memory_folder_path)

        # Create a list of (file_path, creation_time) tuples
        files_with_ctime = []
        for file_name in files_in_dir:
            file_path = os.path.join(self._short_term_memory_folder_path, file_name)
            creation_time = os.path.getctime(file_path)
            files_with_ctime.append((file_path, creation_time))

        # Sort the list by creation_time (oldest first)
        sorted_files_with_ctime = sorted(files_with_ctime, key=lambda x: x[1])

        # Iterate over the sorted list and transfer the memory files if they are past the age in days to transfer
        for file_path, creation_time in sorted_files_with_ctime:
            age_in_seconds = creation_time + self._age_in_days_to_transfer_in_seconds
            if current_time > age_in_seconds:
                self._move_file_from_stm_to_ltm(file_name)
                logger.debug(f"Short-term memory file {file_path} was transferred to Long-term memory {self._long_term_memory_folder_path}.")


    def _move_file_from_stm_to_ltm(self, file_name):
        """
        Move the file from the short-term memory folder to the long-term memory folder.
        """

        source_path = os.path.join(self._short_term_memory_folder_path, file_name)

        if os.path.isfile(source_path):
            dest_path = os.path.join(self._long_term_memory_folder_path, file_name)

            shutil.move(source_path, dest_path)
