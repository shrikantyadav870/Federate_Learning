"""
Utilities package for federated medical imaging.
Exposes common helpers, config loader, logger, metrics, and visualization tools.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from utils.common import set_seed, get_device, count_parameters, ensure_dir, save_json, load_json, format_metrics
    from utils.config_loader import ConfigLoader, DotDict
    from utils.logger import get_logger, TrainingLogger
    from utils.metrics import (
        dice_coefficient, dice_loss, multiclass_dice, sensitivity, specificity,
        compute_all_metrics, compute_segmentation_metrics, print_classification_report
    )
    from utils.visualization import (
        plot_training_curves, plot_confusion_matrix, plot_roc_curve,
        plot_segmentation_overlay, plot_federated_rounds, plot_comparison_bar
    )
except ImportError:
    try:
        from federated_medical_imaging.utils.common import set_seed, get_device, count_parameters, ensure_dir, save_json, load_json, format_metrics
        from federated_medical_imaging.utils.config_loader import ConfigLoader, DotDict
        from federated_medical_imaging.utils.logger import get_logger, TrainingLogger
        from federated_medical_imaging.utils.metrics import (
            dice_coefficient, dice_loss, multiclass_dice, sensitivity, specificity,
            compute_all_metrics, compute_segmentation_metrics, print_classification_report
        )
        from federated_medical_imaging.utils.visualization import (
            plot_training_curves, plot_confusion_matrix, plot_roc_curve,
            plot_segmentation_overlay, plot_federated_rounds, plot_comparison_bar
        )
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.common import set_seed, get_device, count_parameters, ensure_dir, save_json, load_json, format_metrics
        from utils.config_loader import ConfigLoader, DotDict
        from utils.logger import get_logger, TrainingLogger
        from utils.metrics import (
            dice_coefficient, dice_loss, multiclass_dice, sensitivity, specificity,
            compute_all_metrics, compute_segmentation_metrics, print_classification_report
        )
        from utils.visualization import (
            plot_training_curves, plot_confusion_matrix, plot_roc_curve,
            plot_segmentation_overlay, plot_federated_rounds, plot_comparison_bar
        )

__all__ = [
    "set_seed",
    "get_device",
    "count_parameters",
    "ensure_dir",
    "save_json",
    "load_json",
    "format_metrics",
    "ConfigLoader",
    "DotDict",
    "get_logger",
    "TrainingLogger",
    "dice_coefficient",
    "dice_loss",
    "multiclass_dice",
    "sensitivity",
    "specificity",
    "compute_all_metrics",
    "compute_segmentation_metrics",
    "print_classification_report",
    "plot_training_curves",
    "plot_confusion_matrix",
    "plot_roc_curve",
    "plot_segmentation_overlay",
    "plot_federated_rounds",
    "plot_comparison_bar",
]
