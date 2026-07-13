"""
Federated learning aggregation strategies package.
Exposes custom aggregation strategies like FedAvg with logging and FedProx.
"""
import os
import sys
# Try importing components supporting both standard and absolute import resolution paths
try:
    from federated.strategies.fedavg_custom import FedAvgWithLogging
    from federated.strategies.fedprox import FedProx
    from federated.strategies.fedprox import FedProx, FedProxClient, create_fedprox_loss
except ImportError:
    try:
        from federated_medical_imaging.federated.strategies.fedavg_custom import FedAvgWithLogging
        from federated_medical_imaging.federated.strategies.fedprox import FedProx
        from federated_medical_imaging.federated.strategies.fedprox import FedProx, FedProxClient, create_fedprox_loss
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        from federated.strategies.fedavg_custom import FedAvgWithLogging
        from federated.strategies.fedprox import FedProx
        from federated.strategies.fedprox import FedProx, FedProxClient, create_fedprox_loss
__all__ = [
    "FedAvgWithLogging",
    "FedProx",
    "FedProxClient",
    "create_fedprox_loss",
]
