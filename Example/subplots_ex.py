import matplotlib.pyplot as plt

# Tạo một figure và một mảng các subplot 2x2
fig, axs = plt.subplots(2, 2)

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Vẽ đồ thị trên từng subplot
axs[0, 0].plot(x, y, 'tab:blue')
axs[0, 0].set_title('Đồ thị 1')

axs[0, 1].scatter(x, y, color='tab:orange')
axs[0, 1].set_title('Đồ thị 2')

axs[1, 0].bar(x, y, color='tab:green')
axs[1, 0].set_title('Đồ thị 3')

axs[1, 1].hist(y, color='tab:red')
axs[1, 1].set_title('Đồ thị 4')

# Điều chỉnh khoảng cách giữa các subplot
plt.tight_layout()

# Hiển thị figure
plt.show()