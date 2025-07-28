#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Denoising a Simulated Signal Using Kalman Filter

Created on Sat June 12 12:16:27 2023

@author: Sahar Jahani

Description:
This script demonstrates the application of a 1D Kalman Filter to denoise a 
simulated time-series signal (a noisy sine wave). It compares a manual 
implementation of the Kalman filter against the built-in Kalman filter from 
the -filterpy- library to validate correctness.

Features:
- Simulates noisy sine wave signal
- Applies Kalman filter for denoising (manual & built-in)
- Visualizes and compares both filtered outputs

"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

ns = np.linspace(0, 10, 100) 
True_signal = 2 * np.sin(0.8 * np.pi * ns)
Noisy_signal = np.random.randn(100) + True_signal # noisy sine wave


"Kalman Filter Initialization"
A = 1 # State transition
H = 1 # Measurement matrix
Q = 1e-3 # Process noise covariance
R = 0.7e-2 # Measurement noise covariance
P = 1 # Covariance (Uncertainty Initialization)
x_est = np.zeros(100) # State Initialization

for k in range (1, len(ns)):
    
    "Prediction Step"
    x_pred = A * x_est[k-1]
    P_pred = A * P * A + Q
    
    "Kalman Gain"
    K = P_pred * H / (H * P_pred * H + R)
    
    "Update Step"
    x_est[k] = x_pred + K * (Noisy_signal[k] - H * x_pred)
    P = (1 - K * H) * P_pred
   
plt.plot(ns, Noisy_signal, label='Noisy Signal')
plt.plot(ns, True_signal, label='De-noised Signal')
plt.plot(ns, x_est, label='True Signal', )


"We test our implementation with the Built-in Kalman Filter"
from filterpy.kalman import KalmanFilter


kf = KalmanFilter(dim_x=1, dim_z=1)
kf.x = np.array([[0.]])       # Initial state
kf.F = np.array([[1.]])       # State transition matrix
kf.H = np.array([[1.]])       # Observation matrix
kf.P = np.array([[1.]])       # Initial uncertainty
kf.R = np.array([[0.7e-2]])   # Measurement noise
kf.Q = np.array([[1e-3]])     # Process noise

filterpy_estimates = []
for z in Noisy_signal:
    kf.predict()
    kf.update(z)
    filterpy_estimates.append(kf.x[0, 0])
    
    
plt.plot(ns, filterpy_estimates, label='denoised Signal using built-in Kalman Filter', linestyle='--')
plt.xlim([0, 11])
plt.ylim([-5, 7])
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.legend()



