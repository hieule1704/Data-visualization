import matplotlib.pyplot as plt
from datetime import datetime
import csv
from pathlib import Path

# Hàm đọc dữ liệu từ tệp CSV và trả về danh sách ngày và nhiệt độ
def read_weather_data(filename):
    date_index, temp_low_index, temp_high_index = check_index(filename)
    dates, temp_lows, temp_highs = [], [], []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
                temp_low = int(row[temp_low_index])
                temp_high = int(row[temp_high_index])
            except ValueError:
                print(f"Missing or invalid data for {row[date_index]}")
            else:
                dates.append(current_date)
                temp_lows.append(temp_low)
                temp_highs.append(temp_high)
    return dates, temp_lows, temp_highs

def check_index(path_adress):
    path = Path(path_adress)
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Khởi tạo các biến chỉ mục với giá trị mặc định
    date_index = tmin_index = tmax_index = None

    for index, column_header in enumerate(header_row):
        if column_header == 'DATE':
            date_index = index
        elif column_header == 'TMIN':
            tmin_index = index
        elif column_header == 'TMAX':
            tmax_index = index

        # Nếu đã tìm thấy tất cả các chỉ mục, thoát khỏi vòng lặp
        if date_index is not None and tmin_index is not None and tmax_index is not None:
            break

    return date_index, tmin_index, tmax_index


# Đọc dữ liệu cho Sitka và Death Valley
sitka_dates, sitka_temp_lows, sitka_temp_highs = read_weather_data(
    r'C:\Github Repository\Data-visualization\Chapter 16\weather_data\sitka_weather_2021_simple.csv')
death_valley_dates, death_valley_temp_lows, death_valley_temp_highs = read_weather_data(
    r'C:\Github Repository\Data-visualization\Chapter 16\weather_data\death_valley_2021_simple.csv')

# Vẽ biểu đồ cho cả hai địa điểm
plt.style.use('seaborn-v0_8')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Biểu đồ nhiệt độ Sitka
ax1.plot(sitka_dates, sitka_temp_lows, color='blue', alpha=0.6)
ax1.plot(sitka_dates, sitka_temp_highs, color='red', alpha=0.6)
ax1.fill_between(sitka_dates, sitka_temp_lows, sitka_temp_highs, facecolor='blue', alpha=0.1)
ax1.set_title('Daily temperatures - Sitka', fontsize=16)
ax1.set_ylabel('Temperature (F)', fontsize=12)

# Biểu đồ nhiệt độ Death Valley
ax2.plot(death_valley_dates, death_valley_temp_lows, color='blue', alpha=0.6)
ax2.plot(death_valley_dates, death_valley_temp_highs, color='red', alpha=0.6)
ax2.fill_between(death_valley_dates, death_valley_temp_lows, death_valley_temp_highs, facecolor='blue', alpha=0.1)
ax2.set_title('Daily temperatures - Death Valley', fontsize=16)
ax2.set_ylabel('Temperature (F)', fontsize=12)

# Cài đặt cùng giới hạn cho trục y (phạm vi nhiệt độ)
min_temp = min(min(sitka_temp_lows), min(death_valley_temp_lows))
max_temp = max(max(sitka_temp_highs), max(death_valley_temp_highs))
ax1.set_ylim(min_temp, max_temp)
ax2.set_ylim(min_temp, max_temp)

# Định dạng và hiển thị biểu đồ
plt.tight_layout()
plt.show()
