"""
Data pipeline package for federated medical imaging.
Exposes Alzheimer's disease and Brain Tumor datasets and preprocessors.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from data.alzheimer import AlzheimerDataset, AlzheimerPreprocessor, AlzheimerFederatedSplitter
    from data.brain_tumor import BraTSDataset, FigshareDataset, BrainTumorPreprocessor, BrainTumorAugmentor, FederatedDataSplitter
except ImportError:
    try:
        from federated_medical_imaging.data.alzheimer import AlzheimerDataset, AlzheimerPreprocessor, AlzheimerFederatedSplitter
        from federated_medical_imaging.data.brain_tumor import BraTSDataset, FigshareDataset, BrainTumorPreprocessor, BrainTumorAugmentor, FederatedDataSplitter
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from data.alzheimer import AlzheimerDataset, AlzheimerPreprocessor, AlzheimerFederatedSplitter
        from data.brain_tumor import BraTSDataset, FigshareDataset, BrainTumorPreprocessor, BrainTumorAugmentor, FederatedDataSplitter

__all__ = [
    "AlzheimerDataset",
    "AlzheimerPreprocessor",
    "AlzheimerFederatedSplitter",
    "BraTSDataset",
    "FigshareDataset",
    "BrainTumorPreprocessor",
    "BrainTumorAugmentor",
    "FederatedDataSplitter",
]
