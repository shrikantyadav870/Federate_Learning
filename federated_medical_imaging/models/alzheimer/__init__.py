"""
Alzheimer's disease classification models package.
Exposes trainers, model architectures (VGG2D/3D), and transfer learning ensembles.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from models.alzheimer.trainer import AlzheimerTrainer
    from models.alzheimer.transfer_learning import AlzheimerEnsemble
    from models.alzheimer.vgg2d import build_vgg2d
    from models.alzheimer.vgg3d import build_vgg3d, build_vgg3d_small, build_conv_block
except ImportError:
    try:
        from federated_medical_imaging.models.alzheimer.trainer import AlzheimerTrainer
        from federated_medical_imaging.models.alzheimer.transfer_learning import AlzheimerEnsemble
        from federated_medical_imaging.models.alzheimer.vgg2d import build_vgg2d
        from federated_medical_imaging.models.alzheimer.vgg3d import build_vgg3d, build_vgg3d_small, build_conv_block
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        from models.alzheimer.trainer import AlzheimerTrainer
        from models.alzheimer.transfer_learning import AlzheimerEnsemble
        from models.alzheimer.vgg2d import build_vgg2d
        from models.alzheimer.vgg3d import build_vgg3d, build_vgg3d_small, build_conv_block

__all__ = [
    "AlzheimerTrainer",
    "AlzheimerEnsemble",
    "build_vgg2d",
    "build_vgg3d",
    "build_vgg3d_small",
    "build_conv_block",
]
