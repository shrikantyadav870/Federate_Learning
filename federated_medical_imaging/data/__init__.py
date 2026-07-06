"""
Brain Tumor segmentation and classification data pipeline package.
Exposes datasets, augmentation, preprocessing, and federated splitting utilities.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from data.brain_tumor.dataset import BraTSDataset, FigshareDataset
    from data.brain_tumor.preprocessing import BrainTumorPreprocessor
    from data.brain_tumor.augmentation import BrainTumorAugmentor
    from data.brain_tumor.federated_splitter import FederatedDataSplitter
    from data.brain_tumor.download import download_figshare, verify_directory_structure
except ImportError:
    try:
        from federated_medical_imaging.data.brain_tumor.dataset import BraTSDataset, FigshareDataset
        from federated_medical_imaging.data.brain_tumor.preprocessing import BrainTumorPreprocessor
        from federated_medical_imaging.data.brain_tumor.augmentation import BrainTumorAugmentor
        from federated_medical_imaging.data.brain_tumor.federated_splitter import FederatedDataSplitter
        from federated_medical_imaging.data.brain_tumor.download import download_figshare, verify_directory_structure
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        from data.brain_tumor.dataset import BraTSDataset, FigshareDataset
        from data.brain_tumor.preprocessing import BrainTumorPreprocessor
        from data.brain_tumor.augmentation import BrainTumorAugmentor
        from data.brain_tumor.federated_splitter import FederatedDataSplitter
        from data.brain_tumor.download import download_figshare, verify_directory_structure

__all__ = [
    "BraTSDataset",
    "FigshareDataset",
    "BrainTumorPreprocessor",
    "BrainTumorAugmentor",
    "FederatedDataSplitter",
    "download_figshare",
    "verify_directory_structure",
]
