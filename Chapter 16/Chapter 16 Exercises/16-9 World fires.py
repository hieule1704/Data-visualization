from pathlib import Path
import csv
import plotly.express as px
from datetime import datetime


def read_fire_data(filename):
    date_index, latitude_index, longitude_index, bright_index = check_index(filename)
    dates, latitudes, longitudes, brights = [], [], [], []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
                latitude = float(row[latitude_index])
                longitude = float(row[longitude_index])
                bright = float(row[bright_index])
            except ValueError:
                print(f"Missing or invalid data for {row[date_index]}")
            else:
                dates.append(current_date)
                latitudes.append(latitude)
                longitudes.append(longitude)
                brights.append(bright)
    return dates, latitudes, longitudes, brights

def check_index(path_adress):
    path = Path(path_adress)
    lines = path.read_text().splitlines()

    # latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, confidence, version, bright_t31, frp, daynight

    reader = csv.reader(lines)
    header_row = next(reader)

    # Khởi tạo các biến chỉ mục với giá trị mặc định
    latitude_index = longitude_index = bright_index = date_index = None

    for index, column_header in enumerate(header_row):
        if column_header == 'latitude':
            latitude_index = index
        elif column_header == 'longitude':
            longitude_index = index
        elif column_header == 'brightness':
            bright_index = index
        elif column_header == 'acq_date':
            date_index = index

        # Nếu đã tìm thấy tất cả các chỉ mục, thoát khỏi vòng lặp
        if (latitude_index is not None and longitude_index is not None and
                bright_index is not None and date_index is not None):
            break

    return date_index, latitude_index, longitude_index, bright_index


# Đọc dữ liệu cho Sitka và Death Valley
dates, lats, lons, brights = read_fire_data(r'C:\Github Repository\Data-visualization\Chapter 16\eq_data\world_fires_1_day.csv')




# print(brights[:10])
# print(lons[:5])
# print(lats[:5])


title = "World Fires"
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
        color=brights,
        color_continuous_scale='Viridis',
        labels={'color':'Brightness'},
        projection='natural earth',
                     )
fig.show()