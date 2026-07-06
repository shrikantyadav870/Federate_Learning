"""
Dashboard package for federated medical imaging monitoring and analysis.
Exposes application creation and execution entrypoints.
"""

import os
import sys

# Try importing create_app and run_dashboard supporting multiple path configurations
try:
    from dashboard.app import create_app, run_dashboard
except ImportError:
    try:
        from federated_medical_imaging.dashboard.app import create_app, run_dashboard
    except ImportError:
        # Fallback path resolution
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from dashboard.app import create_app, run_dashboard

__all__ = [
    "create_app",
    "run_dashboard",
]
