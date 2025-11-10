"""
Example 3 – Animated Gradient Demo
----------------------------------
Demonstrates static and animated gradient text using RGBText and GradientText.
"""

import time
from rgbterminal import GradientText, animated_gradient_print

# Define a gradient (you can modify the colors)
gradient_colors = [
    (255, 0, 100),   # Pinkish red
    (255, 165, 0),   # Orange
    (0, 255, 255),   # Cyan
    (0, 128, 255),   # Blue
    (255, 0, 255)    # Magenta
]

# Create gradient text
gt = GradientText("RGBTerminal | makes your CLI glow!", rgb_stops=gradient_colors, truecolor=True)

# Print static version
print("Static Gradient Example:")
print(gt)

# Small delay before animation
time.sleep(1.2)

# Animate the gradient sliding effect
print("\nAnimated Gradient Example:")
animated_gradient_print(gt, duration=5, fps=30, speed=3.0, resolution=15)

print("Done!")
