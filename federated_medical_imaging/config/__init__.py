"""
Configuration package for federated medical imaging.
Provides path references and helpers to load YAML configurations.
"""

import os
import sys

# Try importing ConfigLoader from utils.config_loader supporting both standard and modified path structures
try:
    from utils.config_loader import ConfigLoader
except ImportError:
    try:
        from federated_medical_imaging.utils.config_loader import ConfigLoader
    except ImportError:
        # Fallback to absolute/relative import resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.config_loader import ConfigLoader

# Define base configuration directory and yaml file paths
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
ALZHEIMER_CONFIG_PATH = os.path.join(CONFIG_DIR, "alzheimer_config.yaml")
BRAIN_TUMOR_CONFIG_PATH = os.path.join(CONFIG_DIR, "brain_tumor_config.yaml")
FEDERATED_CONFIG_PATH = os.path.join(CONFIG_DIR, "federated_config.yaml")

def load_alzheimer_config():
    """Load the Alzheimer's disease classification configuration."""
    return ConfigLoader.load(ALZHEIMER_CONFIG_PATH)

def load_brain_tumor_config():
    """Load the Brain Tumor segmentation configuration."""
    return ConfigLoader.load(BRAIN_TUMOR_CONFIG_PATH)

def load_federated_config():
    """Load the Federated learning configuration."""
    return ConfigLoader.load(FEDERATED_CONFIG_PATH)

__all__ = [
    "ConfigLoader",
    "ALZHEIMER_CONFIG_PATH",
    "BRAIN_TUMOR_CONFIG_PATH",
    "FEDERATED_CONFIG_PATH",
    "load_alzheimer_config",
    "load_brain_tumor_config",
    "load_federated_config",
]
