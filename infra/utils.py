
import yaml

def read_yaml(config_path="./config_templates.yaml"):
    with open(config_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
