class ConfigManager:
    # attribute to store the single instance
    _instance = None

    def __new__(cls):
        # Check if an instance already exists
        if cls._instance is None: # often cls is used in convention
            # new instance with superclass's __new__ method
            cls._instance = super().__new__(cls)
            # create a settings collection
            cls._instance.settings = {}

        return cls._instance


a = ConfigManager()
b = ConfigManager()
a.settings["theme"] = "dark"
print(b.settings["theme"])  # "dark"