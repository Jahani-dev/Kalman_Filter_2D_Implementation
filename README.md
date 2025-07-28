# 2D Kalman Filter: Object Tracking in Python
This project implements a 2D Kalman Filter to estimate the position and velocity of a moving object using noisy measurements. It's a step-by-step educational implementation to build intuition around state estimation, noise modeling, and filter design.

## Description
We simulate an object moving in 2D space with constant velocity. The object’s true position is not directly observable. Instead, we receive noisy position measurements (like from GPS or a camera). The Kalman filter combines these measurements with a model of motion to estimate the true state: position and velocity over time.

## Features
- Constant velocity motion model
- Gaussian noise in measurements
- Full Kalman filter: prediction and update steps
- Visualization of:
  - True path
  - Noisy measurements
  - Filtered (estimated) trajectory

## How It Works
1. **State Vector**: `[x_position, y_position, x_velocity, y_velocity]`
2. **Prediction**: Estimates the next state based on motion model
3. **Correction**: Updates the estimate using the new noisy observation
4. **Kalman Gain**: Balances trust between model and sensor

## Example Output
The plot shows:
- Orange line: noisy sensor data
- Blue line: true (simulated) object path
- Green line: estimated path using Kalman filter

## Files

- `2DKalmanFilter.py` — full implementation and visualization
- `Figure.png` — the example output plot
- `README.md` — this file

## Requirements

- Python 3.x
- NumPy
- Matplotlib
