# House Price Prediction - MLOps Project

A production-ready machine learning project for predicting house sale prices using a scikit-learn ML pipeline, FastAPI, Docker, and AWS deployment.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Training](#training)
- [API](#api)
- [Deployment](#deployment)
- [Testing](#testing)
- [Configuration](#configuration)

## 🎯 Overview

This project implements an end-to-end machine learning solution for house price prediction with:
- **Data Processing**: Automated feature engineering and preprocessing pipeline
- **Model Training**: Multiple ML algorithms with hyperparameter optimization
- **API Service**: FastAPI-based REST API for real-time predictions
- **AWS Deployment**: Lambda function deployment for serverless prediction
- **CI/CD**: Automated workflows for training, testing, and deployment
- **Containerization**: Docker support for local and cloud deployment

## 📁 Project Structure

```
house_predict/
├── src/                           # Source code
│   ├── app.py                    # FastAPI application
│   ├── train.py                  # Training pipeline
│   ├── predict.py                # Prediction service
│   ├── preprocessing.py           # Data preprocessing
│   ├── feature_pipeline.py        # Feature engineering
│   ├── model_factory.py           # Model instantiation
│   ├── trainer.py                 # Training logic
│   ├── evaluator.py               # Model evaluation
│   ├── schema.py                  # Pydantic models
│   ├── config.py                  # Configuration loader
│   ├── logger.py                  # Logging setup
│   └── utils.py                   # Utility functions
├── tests/                         # Test suite
│   ├── test_api.py               # API tests
│   ├── test_lambda.py            # Lambda handler tests
│   └── test_preprocessing.py      # Preprocessing tests
├── notebooks/                     # Jupyter notebooks
│   └── eda.ipynb                 # Exploratory data analysis
├── data/                          # Data directory
│   ├── raw/                      # Original data
│   └── processed/                # Processed data splits
├── models/                        # Trained models
│   ├── house_pipeline.pkl        # Scikit-learn pipeline
│   ├── metrics.json              # Model metrics
│   └── model_summary.csv         # Training summary
├── configs/                       # Configuration files
│   └── config.yaml               # Project configuration
├── .github/workflows/             # CI/CD workflows
│   └── mlops.yml                 # GitHub Actions pipeline
├── Dockerfile.local              # Local development
├── Dockerfile.lambda             # AWS Lambda deployment
├── requirements.txt              # Python dependencies
└── README.md                      # This file
```

## ✨ Features

- **Multiple ML Algorithms**: Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Extra Trees, Gradient Boosting
- **Hyperparameter Optimization**: Grid search with cross-validation
- **Data Validation**: Input validation using Pydantic schemas
- **Logging & Monitoring**: Structured logging for debugging and monitoring
- **REST API**: FastAPI with `/health`, `/predict`, and root endpoints
- **AWS Lambda Integration**: Serverless prediction capability
- **Docker Support**: Containerized deployment for local and cloud environments
- **CI/CD Pipeline**: Automated testing, training, and deployment

## 🚀 Setup & Installation

### Prerequisites

- Python 3.10+
- Docker (for containerized deployment)
- AWS CLI (for AWS deployment)
- AWS credentials configured

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd house_predict
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 💻 Usage

### Running the API Locally

```bash
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

View interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Health Check

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy"
}
```

### Making Predictions

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "MSSubClass": 20,
    "MSZoning": "RL",
    "LotArea": 8450,
    ...
  }'
```

## 🏋️ Training

### Run Training Pipeline

```bash
python -m src.train
```

This will:
1. Load data from `data/raw/train.csv`
2. Perform train/validation split
3. Build and train the feature pipeline
4. Train multiple models
5. Perform hyperparameter optimization
6. Save the best model to `models/`
7. Export metrics to `models/metrics.json`

### Configuration

Edit `configs/config.yaml` to customize:
- Data paths
- Train/validation split ratio
- Model selection
- Hyperparameter search settings
- Output directories

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| POST | `/predict` | Make predictions |

### Prediction Request Schema

See [src/schema.py](src/schema.py) for the complete `HouseFeatures` schema.

## 📦 Deployment

### Docker - Local Development

```bash
docker build -f Dockerfile.local -t house-price-api:local .
docker run -p 8000:8000 house-price-api:local
```

### AWS Lambda

1. **Build Lambda image**
   ```bash
   docker build -f Dockerfile.lambda -t house-price-api:lambda .
   ```

2. **Push to ECR**
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
   docker tag house-price-api:lambda <account-id>.dkr.ecr.us-east-1.amazonaws.com/house-price-api:latest
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/house-price-api:latest
   ```

3. **Update Lambda function**
   ```bash
   aws lambda update-function-code \
     --function-name house-price-api \
     --image-uri <account-id>.dkr.ecr.us-east-1.amazonaws.com/house-price-api:latest
   ```

### GitHub Actions CI/CD

The project includes automated workflows that:
1. Run on push to `main` branch
2. Download dataset from S3
3. Execute training pipeline
4. Run test suite
5. Build and push Docker image to ECR
6. Deploy to AWS Lambda

Trigger manual retraining:
```bash
gh workflow run mlops.yml
```

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run specific tests:

```bash
pytest tests/test_api.py -v          # API tests
pytest tests/test_preprocessing.py    # Preprocessing tests
pytest tests/test_lambda.py           # Lambda tests
```

Generate coverage report:

```bash
pytest tests/ --cov=src --cov-report=html
```

## ⚙️ Configuration

### config.yaml

Key configuration options:

```yaml
data:
  train_path: data/raw/train.csv
  target: SalePrice

split:
  test_size: 0.20
  random_state: 42

model:
  models:
    - random_forest
    - gradient_boosting

training:
  hyperparameter_search: true
  n_iter: 5
  cv: 3
```

### Environment Variables

```
AWS_REGION=us-east-1
S3_BUCKET=house-price-data-<account-id>
LOG_LEVEL=INFO
```

## 📊 Model Performance

Training outputs metrics to `models/metrics.json`:
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- Cross-validation scores

## 🔧 Development

### Code Quality

Format code:
```bash
black src/ tests/
```

Lint code:
```bash
flake8 src/ tests/
```

Type checking:
```bash
mypy src/
```

### Adding New Features

1. Create feature in `src/features.py`
2. Add to preprocessing pipeline in `src/preprocessing.py`
3. Update schema in `src/schema.py`
4. Add tests in `tests/`
5. Update configuration in `configs/config.yaml`

## 📝 Logging

Logs are managed by `src/logger.py` and output to `logs/` directory.

Configure log level in `config.yaml`:
```yaml
logging:
  level: INFO
```

## 🤝 Contributing

1. Create a feature branch
2. Make changes and add tests
3. Ensure all tests pass
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 📞 Support

For issues and questions, please:
- Check existing issues
- Create a new GitHub issue with detailed information
- Include error logs and reproduction steps
