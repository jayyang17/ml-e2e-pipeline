from dataclasses import dataclass
from pathlib import Path

# Data ingestion 
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# Data validation 
@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: Path
    all_schema: dict

# Data transformation
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path