# Efficient Data Stream Anomaly Detection

## Project Description
This project involves developing a Python script to detect anomalies in a continuous data stream. The stream simulates real-time sequences of floating-point numbers, representing metrics such as financial transactions or system metrics.

## Objectives
- **Algorithm Selection**: Implement the Z-Score method for anomaly detection.
- **Data Stream Simulation**: Generate data with regular patterns, seasonal elements, and noise.
- **Anomaly Detection**: Flag anomalies in real-time.
- **Optimization**: Ensure efficient algorithm performance.
- **Visualization**: Real-time plot for data and detected anomalies.

## Setup
1. Clone the repository.
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:
    ```bash
    python main.py
    ```

## Dependencies
- `numpy`
- `matplotlib`
