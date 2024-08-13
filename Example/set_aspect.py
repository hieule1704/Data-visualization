import matplotlib.pyplot as plt

# Tạo dữ liệu cho một hình tròn
import numpy as np
theta = np.linspace(0, 2 * np.pi, 100)
r = 1
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()

# Vẽ hình tròn
ax.plot(x, y)

# Thiết lập tỷ lệ khung hình bằng nhau
ax.set_aspect('equal')

# Đặt tiêu đề và nhãn
ax.set_title('Hình Tròn với Tỷ Lệ Khung Hình Bằng Nhau')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
