import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.animation import FuncAnimation

# Function to generate data stream
def generate_data_stream(n=1000):
    x = np.linspace(0, 4 * np.pi, n)
    seasonal = np.sin(x) + np.cos(x)
    noise = np.random.normal(0, 0.5, n)
    data = seasonal + noise
    return data

# Anomaly detection class
class AnomalyDetector:
    def __init__(self, window_size=100, threshold=3.0):
        self.window_size = window_size
        self.threshold = threshold
        self.window = deque(maxlen=window_size)
        self.mean = 0
        self.std_dev = 1

    def update(self, value):
        self.window.append(value)
        if len(self.window) < self.window_size:
            return False
        
        self.mean = np.mean(self.window)
        self.std_dev = np.std(self.window)
        z_score = (value - self.mean) / self.std_dev

        return abs(z_score) > self.threshold

# Visualization function
def update_plot(frame):
    value = data[frame]
    is_anomaly = detector.update(value)
    data_line.set_xdata(np.arange(frame))
    data_line.set_ydata(data[:frame])
    
    if is_anomaly:
        anomaly_points.append((frame, value))
        anomaly_scatter.set_offsets(anomaly_points)
    
    return data_line, anomaly_scatter

# Main code
if __name__ == "__main__":
    data = generate_data_stream()
    
    # Set up plot
    fig, ax = plt.subplots()
    data_line, = ax.plot([], [], lw=2)
    anomaly_scatter = ax.scatter([], [], color='red')
    ax.set_xlim(0, len(data))
    ax.set_ylim(min(data) - 1, max(data) + 1)
    ax.set_title('Real-Time Data Stream with Anomalies')
    
    # Initialize detector and plot
    detector = AnomalyDetector(window_size=100, threshold=3.0)
    anomaly_points = []
    ani = FuncAnimation(fig, update_plot, frames=range(len(data)), blit=True, interval=100)
    
    plt.show()
