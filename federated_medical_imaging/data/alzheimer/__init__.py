# Alzheimer data pipeline
"""
Alzheimer's disease data pipeline package.
Exposes datasets, preprocessing, and federated splitting utilities.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from data.alzheimer.dataset import AlzheimerDataset
    from data.alzheimer.preprocessing import AlzheimerPreprocessor
    from data.alzheimer.federated_splitter import AlzheimerFederatedSplitter
    from data.alzheimer.download import verify_dataset_structure, verify_adni_data, verify_oasis_data
except ImportError:
    try:
        from federated_medical_imaging.data.alzheimer.dataset import AlzheimerDataset
        from federated_medical_imaging.data.alzheimer.preprocessing import AlzheimerPreprocessor
        from federated_medical_imaging.data.alzheimer.federated_splitter import AlzheimerFederatedSplitter
        from federated_medical_imaging.data.alzheimer.download import verify_dataset_structure, verify_adni_data, verify_oasis_data
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        from data.alzheimer.dataset import AlzheimerDataset
        from data.alzheimer.preprocessing import AlzheimerPreprocessor
        from data.alzheimer.federated_splitter import AlzheimerFederatedSplitter
        from data.alzheimer.download import verify_dataset_structure, verify_adni_data, verify_oasis_data

__all__ = [
    "AlzheimerDataset",
    "AlzheimerPreprocessor",
    "AlzheimerFederatedSplitter",
    "verify_dataset_structure",
    "verify_adni_data",
    "verify_oasis_data",
]
