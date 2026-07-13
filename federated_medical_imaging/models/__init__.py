"""
Models package for federated medical imaging.
Exposes trainers, architectures, and ensembles for Alzheimer's classification
and Brain Tumor segmentation.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from models.brain_tumor.trainer import BrainTumorTrainer
    from models.brain_tumor.unet3d import build_unet3d
    from models.brain_tumor.unet2d import build_unet2d
    from models.brain_tumor.densenet_extractor import build_densenet_extractor
    from models.brain_tumor.ensemble_classifier import BrainTumorEnsembleClassifier
    from models.alzheimer.trainer import AlzheimerTrainer
    from models.alzheimer.vgg3d import build_vgg3d, build_vgg3d_small
    from models.alzheimer.vgg2d import build_vgg2d
    from models.alzheimer.transfer_learning import AlzheimerEnsemble
except ImportError:
    try:
        from federated_medical_imaging.models.brain_tumor.trainer import BrainTumorTrainer
        from federated_medical_imaging.models.brain_tumor.unet3d import build_unet3d
        from federated_medical_imaging.models.brain_tumor.unet2d import build_unet2d
        from federated_medical_imaging.models.brain_tumor.densenet_extractor import build_densenet_extractor
        from federated_medical_imaging.models.brain_tumor.ensemble_classifier import BrainTumorEnsembleClassifier
        from federated_medical_imaging.models.alzheimer.trainer import AlzheimerTrainer
        from federated_medical_imaging.models.alzheimer.vgg3d import build_vgg3d, build_vgg3d_small
        from federated_medical_imaging.models.alzheimer.vgg2d import build_vgg2d
        from federated_medical_imaging.models.alzheimer.transfer_learning import AlzheimerEnsemble
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from models.brain_tumor.trainer import BrainTumorTrainer
        from models.brain_tumor.unet3d import build_unet3d
        from models.brain_tumor.unet2d import build_unet2d
        from models.brain_tumor.densenet_extractor import build_densenet_extractor
        from models.brain_tumor.ensemble_classifier import BrainTumorEnsembleClassifier
        from models.alzheimer.trainer import AlzheimerTrainer
        from models.alzheimer.vgg3d import build_vgg3d, build_vgg3d_small
        from models.alzheimer.vgg2d import build_vgg2d
        from models.alzheimer.transfer_learning import AlzheimerEnsemble

__all__ = [
    "BrainTumorTrainer",
    "build_unet3d",
    "build_unet2d",
    "build_densenet_extractor",
    "BrainTumorEnsembleClassifier",
    "AlzheimerTrainer",
    "build_vgg3d",
    "build_vgg3d_small",
    "build_vgg2d",
    "AlzheimerEnsemble",
]
