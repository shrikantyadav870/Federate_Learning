"""
Execution and pipeline scripts package for federated medical imaging.
Includes scripts for preprocessing, training, federated simulation, and dashboard execution.
"""

import os
import sys

# Try importing scripts supporting both standard and absolute import resolution paths
try:
    import scripts.run_federated as run_federated
    import scripts.run_full_pipeline as run_full_pipeline
    import scripts.run_dashboard as run_dashboard
    import scripts.preprocess_alzheimer as preprocess_alzheimer
    import scripts.preprocess_brain_tumor as preprocess_brain_tumor
    import scripts.train_alzheimer as train_alzheimer
    import scripts.train_brain_tumor as train_brain_tumor
    import scripts.train_alzheimer_final as train_alzheimer_final
    import scripts.train_brain_tumor_final as train_brain_tumor_final
    import scripts.evaluate_results as evaluate_results
    import scripts.generate_synthetic_data as generate_synthetic_data
    import scripts.predict_client as predict_client
except ImportError:
    try:
        import federated_medical_imaging.scripts.run_federated as run_federated
        import federated_medical_imaging.scripts.run_full_pipeline as run_full_pipeline
        import federated_medical_imaging.scripts.run_dashboard as run_dashboard
        import federated_medical_imaging.scripts.preprocess_alzheimer as preprocess_alzheimer
        import federated_medical_imaging.scripts.preprocess_brain_tumor as preprocess_brain_tumor
        import federated_medical_imaging.scripts.train_alzheimer as train_alzheimer
        import federated_medical_imaging.scripts.train_brain_tumor as train_brain_tumor
        import federated_medical_imaging.scripts.train_alzheimer_final as train_alzheimer_final
        import federated_medical_imaging.scripts.train_brain_tumor_final as train_brain_tumor_final
        import federated_medical_imaging.scripts.evaluate_results as evaluate_results
        import federated_medical_imaging.scripts.generate_synthetic_data as generate_synthetic_data
        import federated_medical_imaging.scripts.predict_client as predict_client
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import scripts.run_federated as run_federated
        import scripts.run_full_pipeline as run_full_pipeline
        import scripts.run_dashboard as run_dashboard
        import scripts.preprocess_alzheimer as preprocess_alzheimer
        import scripts.preprocess_brain_tumor as preprocess_brain_tumor
        import scripts.train_alzheimer as train_alzheimer
        import scripts.train_brain_tumor as train_brain_tumor
        import scripts.train_alzheimer_final as train_alzheimer_final
        import scripts.train_brain_tumor_final as train_brain_tumor_final
        import scripts.evaluate_results as evaluate_results
        import scripts.generate_synthetic_data as generate_synthetic_data
        import scripts.predict_client as predict_client

__all__ = [
    "run_federated",
    "run_full_pipeline",
    "run_dashboard",
    "preprocess_alzheimer",
    "preprocess_brain_tumor",
    "train_alzheimer",
    "train_brain_tumor",
    "train_alzheimer_final",
    "train_brain_tumor_final",
    "evaluate_results",
    "generate_synthetic_data",
    "predict_client",
]
