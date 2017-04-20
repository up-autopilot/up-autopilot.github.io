from up.registrar import UpRegistrar


class Registrar(UpRegistrar):
    # Name of the config created for this Cog
    CONFIG_FILE_NAME = 'android.yml'

    # Keys present in the config
    PORT_KEY = 'general port'
    ORIENTATION_PORT_KEY = 'orientation port'
    STOP_KEY = 'stop if orientation connection is lost'
    STOP_DELAY_KEY = 'stop delay (s)'
    ONBOARD_FORWARD_KEY = 'forward interval for onboard device (ms)'

    # Default config content
    CONFIG_TEMPLATE = """\
%s: 50001
%s: 50000
%s: True
%s: 10
%s: 500
""" % (PORT_KEY, ORIENTATION_PORT_KEY, STOP_KEY, STOP_DELAY_KEY, ONBOARD_FORWARD_KEY)

    def __init__(self):
        super().__init__('android_cog')

    def register(self):
        # Loads the external_modules.yml file of your app 
        external_modules = self._load_external_modules()

        # check whether the config has been successfully loaded
        if external_modules is not None:
            # Writes the registered Modules from the registered_modules.yml of the Cog
            self._register_modules_from_file()
            
            # Creates a YAML config with file name CONFIG_FILE_NAME and content CONFIG_TEMPLATE
            # if such file exists, is is NOT modified
            self._create_config(self.CONFIG_FILE_NAME, self.CONFIG_TEMPLATE)
            
            # Indicates everything was registered
            return True
    
        # Indicates there has been an error during registration
        return False
