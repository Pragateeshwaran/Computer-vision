import cv2
import numpy as np

# Create a blank image (500x500) with black background
image = np.zeros((500, 500, 3), dtype=np.uint8)

# 1️⃣ Line
cv2.line(image, 
         (20, 50),  # Start point (x1, y1)
         (200, 50), # End point (x2, y2)
         (255, 0, 0), # Color (Blue)
         3)          # Thickness
# (x, y, z) -> (B, G, R) in OpenCV
# 2️⃣ Rectangle
cv2.rectangle(image, 
              (250, 30),   # Top-left corner (x1, y1)
              (450, 100),  # Bottom-right corner (x2, y2)
              (0, 255, 0), # Color (Green)
              2)           # Thickness

# 3️⃣ Filled Rectangle
cv2.rectangle(image, 
              (20, 120),   # Top-left corner
              (150, 200),  # Bottom-right corner
              (0, 255, 255), # Color (Yellow)
              -1)            # -1 fills the rectangle

# 4️⃣ Circle
cv2.circle(image, 
           (350, 170),   # Center point (x, y)
           50,           # Radius
           (0, 0, 255),  # Color (Red)
           3)            # Thickness

# 5️⃣ Filled Circle
cv2.circle(image, 
           (100, 300),   # Center point
           40,           # Radius
           (255, 0, 255), # Color (Magenta)
           -1)            # Filled circle

# 6️⃣ Ellipse
cv2.ellipse(image, 
            (350, 300),     # Center point (x, y)
            (60, 30),       # Axes lengths (width, height)
            45,             # Rotation angle (in degrees)
            270, 0,         # Start and end angles
            (0, 255, 255),  # Color (Cyan)
            2)              # Thickness

# 7️⃣ Polygon (Outline)
points = np.array([[250, 250], [400, 350], [300, 400], [200, 350]])
cv2.polylines(image, 
              [points],     # Array of points
              True,         # isClosed = True (closed polygon)
              (255, 100, 0),# Color (Orange)
              3)            # Thickness

# 8️⃣ Filled Polygon
filled_pts = np.array([[20, 400], [80, 470], [150, 450]], np.int32)
cv2.fillPoly(image, 
             [filled_pts],    # Array of points
             (200, 100, 255)) # Color (Pink)

# 9️⃣ Arrowed Line
cv2.arrowedLine(image, 
                (20, 450),     # Start point
                (200, 450),    # End point
                (0, 200, 200), # Color (Teal)
                3,             # Thickness
                tipLength=0.1) # Length of the arrowhead

# 🔟 Text
cv2.putText(image, 
            "OpenCV Shapes", # Text content
            (150, 490),      # Starting position (x, y)
            cv2.FONT_HERSHEY_SIMPLEX, # Font style
            1,               # Font size
            (200, 200, 200), # Color (Gray)
            2)               # Thickness

# Display the result
cv2.imshow("All Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
