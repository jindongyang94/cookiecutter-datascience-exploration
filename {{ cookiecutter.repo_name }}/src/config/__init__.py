import os
import yaml
from glob import glob

# Class to encapsulate the config functions
class __Config__:
    """
    Config Class to grab all yaml files dynamically.
    """
    def __init__(self):
        self.yaml_dict = {}
        # Directories
        self.CONFIG_ML_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ml_config')
        self.CONFIG_WORKFLOW_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'workflow_config')

    def get(self, configname):
        """
        configname: name of the config file (without the config extension - .yaml)
        return the config in dictionary format

        - we will not add recursive find here cos if there config files are segregated further, just add the folder prefix at the start.
        - this is because if there are config names with the same name but under different folders, the recursive function would be meaningless.
        - we should change this function to find the first config name matching the one searched.
        """
        yaml_file = glob(os.path.join(self.CONFIG_ML_DIR, f'{configname}.yaml'))
        print (yaml_file)
        config = None

        if yaml_file:
            yaml_file = yaml_file[0]
            with open(yaml_file, 'r') as yaml_obj:
                config = yaml.load(yaml_obj, Loader=yaml.FullLoader)
        
        if not config:
            raise KeyError("Config File not found. Please put your config file under the config folder ('src/config/) \
                or make sure the name is spelt correctly.")

        return config

    def get_api_config(self):
        """
        get api config from workflow_config folder
        """
        yaml_file = glob(os.path.join(self.CONFIG_WORKFLOW_DIR, 'api.yaml'))
        print (yaml_file)
        config = None

        if yaml_file:
            yaml_file = yaml_file[0]
            with open(yaml_file, 'r') as yaml_obj:
                config = yaml.load(yaml_obj, Loader=yaml.FullLoader)
        
        if not config:
            raise KeyError("Config File not found. Please put your config file under the config folder ('src/config/) \
                or make sure the name is spelt correctly.")

        return config

    def get_all_yaml_configs(self):
        """
        Encapsulating function to return a dictionary of dictionaries, with each dictionary representing one config yaml file.
        E.g. If config folder has a file called "model1.yaml", edit the file and reload the module.
        import config from src.config and the model parameters will be represented as a dictionary under config['model1'].

        all templates (any yaml file with template in its name) will be not considered in loading process.
        """
        yaml_files = glob(os.path.join(self.CONFIG_ML_DIR, '*.yaml'))
        yaml_files.extend(glob(os.path.join(self.CONFIG_WORKFLOW_DIR, '*.yaml')))
        # Remove template files from list of yaml files loaded.
        yaml_files = list(set(filter(lambda x: 'template' not in x, yaml_files)))

        if yaml_files:
            for yaml_file in yaml_files:
                yaml_basename = os.path.basename(yaml_file)
                yaml_key = yaml_basename.split('.')[0]
                with open(yaml_file, 'r') as yaml_obj:
                    yaml_value = yaml.load(yaml_obj, Loader=yaml.FullLoader)
                    self.yaml_dict[yaml_key] = yaml_value

        if not self.yaml_dict:
            # No YAML files in directory - return None
            return None
        
        return self.yaml_dict

config = __Config__()