"""
Federated learning package for medical imaging.
Exposes client, server, and simulation components.
"""

import os
import sys

# Try importing components supporting both standard and absolute import resolution paths
try:
    from federated.client import MedicalImagingClient
    from federated.server import FederatedServer
    from federated.simulation import FederatedSimulation
except ImportError:
    try:
        from federated_medical_imaging.federated.client import MedicalImagingClient
        from federated_medical_imaging.federated.server import FederatedServer
        from federated_medical_imaging.federated.simulation import FederatedSimulation
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from federated.client import MedicalImagingClient
        from federated.server import FederatedServer
        from federated.simulation import FederatedSimulation

__all__ = [
    "MedicalImagingClient",
    "FederatedServer",
    "FederatedSimulation",
]
