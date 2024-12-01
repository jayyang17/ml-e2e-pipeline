# ML End-to-End Pipeline

This repository implements a complete end-to-end Machine Learning (ML) pipeline, designed to streamline the process of data ingestion, validation, transformation, model training, evaluation, and deployment. The pipeline is modular, scalable, and follows industry best practices for MLOps.

## Features

- **Data Ingestion**: Collect and prepare data from multiple sources.
- **Data Validation**: Validate data quality using a predefined schema.
- **Data Transformation**: Clean and preprocess data for model consumption.
- **Model Training**: Train machine learning models with configurable parameters.
- **Model Evaluation**: Assess performance metrics for trained models.
- **Deployment**: Package and deploy models for inference in production.

## Repository Structure

```plaintext
.
├── .github/workflows/    # CI/CD workflows using GitHub Actions
├── config/               # Configuration files for pipeline steps
├── research/             # Notebooks and experimental code
├── src/datascience/      # Core ML pipeline source code
├── templates/            # Template files for pipeline components
├── .gitignore            # Files and directories to ignore in version control
├── Dockerfile            # Docker configuration for containerized environments
├── LICENSE               # License information (GPL-2.0)
├── README.md             # Project documentation
├── app.py                # Flask app for serving models
├── main.py               # Entry point to execute the ML pipeline
├── params.yaml           # Hyperparameters and model configurations
├── requirements.txt      # Python dependencies
├── schema.yaml           # Schema definition for data validation
├── setup.py              # Installation script for the project
└── template.py           # Boilerplate for new pipeline components
```

## Development Workflow
### Add New Features:

Use template.py to quickly scaffold new components.
Update configuration files and main.py to integrate the new component.

### CI/CD Integration:

Push changes to trigger workflows in .github/workflows.

### Testing:

Include unit tests for new features and run tests before pushing.

### Acknowledgements
Special thanks to krishnaik06 for the tutorial that guided the structure of this project.
