import matplotlib.pyplot as plt

# Vẽ biểu đồ năm số lập phương đầu tiên
input_values_small = [1, 2, 3, 4, 5]
cubes_small = [x**3 for x in input_values_small]

plt.style.use('ggplot')  # Chọn kiểu biểu đồ
fig, ax = plt.subplots() #Nay tuong tu voi dung plot() nhung dung subplot co them ax sau nay dể mo expand
ax.plot(input_values_small, cubes_small, marker='o', linestyle='-', color='b', linewidth=2)

# Đặt tiêu đề và nhãn trục
ax.set_title('Five Cubic Numbers', fontsize=16)
ax.set_xlabel('Number', fontsize=12)
ax.set_ylabel('Cubic Number', fontsize=12)

# Đặt kích thước nhãn trục
ax.tick_params(labelsize=12)

plt.show()

# Vẽ biểu đồ năm nghìn số lập phương đầu tiên
input_values_large = list(range(1, 5001))
cubes_large = [x**3 for x in input_values_large]

plt.style.use('ggplot')  # Chọn kiểu biểu đồ
fig, ax = plt.subplots()
scatter = ax.scatter(input_values_large, cubes_large, c=cubes_large, cmap=plt.cm.Greens, s=10)

# Đặt tiêu đề và nhãn trục
ax.set_title('First 5,000 Cubic Numbers', fontsize=16)
ax.set_xlabel('Number', fontsize=12)
ax.set_ylabel('Cubic Number', fontsize=12)

# Đặt kích thước nhãn trục
ax.tick_params(labelsize=12)

# Thêm thanh màu để hiển thị bản đồ màu
fig.colorbar(scatter, ax=ax, label='Cubic Number')

plt.show()
