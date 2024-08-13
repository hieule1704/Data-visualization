import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, 'bo-', label='Dữ liệu')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')
plt.title('Đồ thị đường')
plt.legend()
plt.show()
