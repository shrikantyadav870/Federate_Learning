Federate_Learning/
├── .gitignore                          # Excludes datasets, models, venv, etc.
└── federated_medical_imaging/
    ├── README.md                       # Full project documentation
    ├── requirements.txt                # Python dependencies
    ├── setup.py                        # Package setup
    ├── config/                         # YAML configs (Alzheimer, Brain Tumor, FL)
    ├── dashboard/                      # Flask web dashboard (app, CSS, JS, HTML)
    │   ├── static/reference_images/    # Reference brain scan images
    │   └── templates/                  # HTML templates
    ├── data/                           # Data loaders & preprocessors
    ├── federated/                      # FL server, client, FedAvg, FedProx
    ├── models/                         # 3D U-Net, 3D VGG, DenseNet, Ensemble
    ├── scripts/                        # Training, pipeline, dashboard scripts
    ├── tests/                          # Full pytest test suite (12 files)
    └── utils/                          # Logger, metrics, visualization
