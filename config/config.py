import utilities.utilities as utilities

class Config:

    def __init__(self, config_path):
        self._config_path = config_path

        self._load_config_variables()


    def _load_config_variables(self):
        """
        Call this at the initial load of Config class and also whenever you 
        change a value in the config.json to reload the variables in the this Config class.
        """
        self._config_json = utilities.read_json_file(self._config_path)
