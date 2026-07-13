"""
Test suite package for federated medical imaging.
Includes unit and integration tests for models, data pipelines, configs, dashboard, and federated training.
"""

import os
import sys

# Try importing test modules supporting both standard and absolute import resolution paths
try:
    import tests.test_config as test_config
    import tests.test_utils as test_utils
    import tests.test_metrics as test_metrics
    import tests.test_federated as test_federated
    import tests.test_dashboard as test_dashboard
    import tests.test_alzheimer_models as test_alzheimer_models
    import tests.test_alzheimer_pipeline as test_alzheimer_pipeline
    import tests.test_brain_tumor_models as test_brain_tumor_models
    import tests.test_brain_tumor_pipeline as test_brain_tumor_pipeline
    import tests.test_integration as test_integration
except ImportError:
    try:
        import federated_medical_imaging.tests.test_config as test_config
        import federated_medical_imaging.tests.test_utils as test_utils
        import federated_medical_imaging.tests.test_metrics as test_metrics
        import federated_medical_imaging.tests.test_federated as test_federated
        import federated_medical_imaging.tests.test_dashboard as test_dashboard
        import federated_medical_imaging.tests.test_alzheimer_models as test_alzheimer_models
        import federated_medical_imaging.tests.test_alzheimer_pipeline as test_alzheimer_pipeline
        import federated_medical_imaging.tests.test_brain_tumor_models as test_brain_tumor_models
        import federated_medical_imaging.tests.test_brain_tumor_pipeline as test_brain_tumor_pipeline
        import federated_medical_imaging.tests.test_integration as test_integration
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import tests.test_config as test_config
        import tests.test_utils as test_utils
        import tests.test_metrics as test_metrics
        import tests.test_federated as test_federated
        import tests.test_dashboard as test_dashboard
        import tests.test_alzheimer_models as test_alzheimer_models
        import tests.test_alzheimer_pipeline as test_alzheimer_pipeline
        import tests.test_brain_tumor_models as test_brain_tumor_models
        import tests.test_brain_tumor_pipeline as test_brain_tumor_pipeline
        import tests.test_integration as test_integration

__all__ = [
    "test_config",
    "test_utils",
    "test_metrics",
    "test_federated",
    "test_dashboard",
    "test_alzheimer_models",
    "test_alzheimer_pipeline",
    "test_brain_tumor_models",
    "test_brain_tumor_pipeline",
    "test_integration",
]
