from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Đường dẫn tuyệt đối với chuỗi thô
absolute_path_str = r'C:\Github Repository\Data-visualization\Chapter 16\weather_data\sitka_weather_2021_full.csv'

# Tạo đối tượng Path từ đường dẫn tuyệt đối
path = Path(absolute_path_str)

# Đọc tệp và tách dòng
with path.open(newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header_row = next(reader)

    # Extract dates, daily rainfall amount
    dates, rain_amounts = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            rain = float(row[5])  # Chuyển đổi thành float để xử lý các giá trị thập phân
        except ValueError:
            print(f"Missing or invalid data for {row[2]}")
        else:
            dates.append(current_date)
            rain_amounts.append(rain)

# Plot the daily rainfall amounts.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rain_amounts, color='blue', alpha=0.5)

# Format plot.
title = "Daily Rainfall Amounts, 2021\nSitka, Alaska"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Rain Amount (in mm)", fontsize=16)
ax.tick_params(labelsize=16)

# Format date labels
fig.autofmt_xdate()  # Draws the date labels diagonally to prevent them from overlapping

plt.show()
