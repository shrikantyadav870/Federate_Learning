"""
Brain tumor segmentation and classification models package.
Exposes U-Net model architectures, feature extractors, and ensemble classifiers.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from models.brain_tumor.trainer import BrainTumorTrainer
    from models.brain_tumor.unet2d import build_unet2d
    from models.brain_tumor.unet3d import build_unet3d, dice_loss_tf, combined_loss, SqueezeExcitation3D
    from models.brain_tumor.densenet_extractor import build_densenet_extractor, InceptionMultiscaleBlock, SpatialAttention, extract_features
    from models.brain_tumor.ensemble_classifier import BrainTumorEnsembleClassifier
except ImportError:
    try:
        from federated_medical_imaging.models.brain_tumor.trainer import BrainTumorTrainer
        from federated_medical_imaging.models.brain_tumor.unet2d import build_unet2d
        from federated_medical_imaging.models.brain_tumor.unet3d import build_unet3d, dice_loss_tf, combined_loss, SqueezeExcitation3D
        from federated_medical_imaging.models.brain_tumor.densenet_extractor import build_densenet_extractor, InceptionMultiscaleBlock, SpatialAttention, extract_features
        from federated_medical_imaging.models.brain_tumor.ensemble_classifier import BrainTumorEnsembleClassifier
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        from models.brain_tumor.trainer import BrainTumorTrainer
        from models.brain_tumor.unet2d import build_unet2d
        from models.brain_tumor.unet3d import build_unet3d, dice_loss_tf, combined_loss, SqueezeExcitation3D
        from models.brain_tumor.densenet_extractor import build_densenet_extractor, InceptionMultiscaleBlock, SpatialAttention, extract_features
        from models.brain_tumor.ensemble_classifier import BrainTumorEnsembleClassifier

__all__ = [
    "BrainTumorTrainer",
    "build_unet2d",
    "build_unet3d",
    "dice_loss_tf",
    "combined_loss",
    "SqueezeExcitation3D",
    "build_densenet_extractor",
    "InceptionMultiscaleBlock",
    "SpatialAttention",
    "extract_features",
    "BrainTumorEnsembleClassifier",
]
