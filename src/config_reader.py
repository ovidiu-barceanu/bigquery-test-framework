import yaml

def get_env_config(env_name):
    with open("config/environments.yaml") as f:
        config = yaml.safe_load(f)

    return config[env_name]