import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.animation import FuncAnimation
import random
import time

# Function to simulate real-time data stream
def generate_real_time_data():
    while True:
        # Simulating a sine wave with some noise and occasional spikes (anomalies)
        noise = random.uniform(-0.5, 0.5)
        spike = random.choice([0, 10 * random.uniform(-1, 1)])  # Random spike
        value = np.sin(time.time()) + noise + spike
        yield value

# Real-time Anomaly Detection Class
class RealTimeAnomalyDetector:
    def __init__(self, window_size=50, threshold=2.5):
        self.window_size = window_size
        self.threshold = threshold
        self.window = deque(maxlen=window_size)
        self.mean = 0
        self.std_dev = 1

    def detect_anomaly(self, value):
        self.window.append(value)
        if len(self.window) < self.window_size:
            return False
        
        self.mean = np.mean(self.window)
        self.std_dev = np.std(self.window)
        z_score = (value - self.mean) / self.std_dev
        
        return abs(z_score) > self.threshold

# Visualization function for real-time plot update
def update_plot(frame):
    value = next(data_stream)
    is_anomaly = detector.detect_anomaly(value)

    data.append(value)
    if len(data) > max_frames:
        data.pop(0)

    data_line.set_data(np.arange(len(data)), data)

    if is_anomaly:
        anomaly_points.append((len(data) - 1, value))
        anomaly_scatter.set_offsets(anomaly_points)

    return data_line, anomaly_scatter

# Main code for real-time anomaly detection and visualization
if __name__ == "__main__":
    # Create real-time data generator
    data_stream = generate_real_time_data()

    # Initialize detector, data storage, and plot
    detector = RealTimeAnomalyDetector(window_size=50, threshold=2.5)
    data = []
    anomaly_points = []

    max_frames = 100  # Number of frames to display in the window

    # Set up plot
    fig, ax = plt.subplots()
    data_line, = ax.plot([], [], lw=2)
    anomaly_scatter = ax.scatter([], [], color='red')
    ax.set_xlim(0, max_frames)
    ax.set_ylim(-2, 12)  # Adjust according to the expected range of values
    ax.set_title('Real-Time Anomaly Detection')

    # Start the real-time animation
    ani = FuncAnimation(fig, update_plot, frames=np.arange(1000), interval=100, blit=True)

    plt.show()
