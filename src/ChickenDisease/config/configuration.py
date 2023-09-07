from ChickenDisease.constants import *
from ChickenDisease.utils.common import read_yaml , create_directories
from ChickenDisease.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        dataingestion_config = self.config.data_ingestion

        create_directories([dataingestion_config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=dataingestion_config.root_dir,
            source_URL=dataingestion_config.source_URL,
            local_data_file=dataingestion_config.local_data_file,
            unzip_dir=dataingestion_config.unzip_dir 
        )

        return data_ingestion_config