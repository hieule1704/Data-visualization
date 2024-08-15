import plotly.express as px
from random_walk import RandomWalk

def create_walk_plot():
    """Create and display a random walk plot."""
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Xác định phạm vi dữ liệu
    x_range = max(rw.x_values) - min(rw.x_values)
    y_range = max(rw.y_values) - min(rw.y_values)

    # Tính toán khoảng cách nhãn hợp lý
    # Sử dụng giá trị tối ưu cho tick spacing (đơn vị)
    x_dtick = max(1, int(x_range / 10))  # Chia phạm vi thành khoảng 10 nhãn
    y_dtick = max(1, int(y_range / 10))  # Chia phạm vi thành khoảng 10 nhãn

    # Visualize the results.
    title = "Random Walk Visualization"
    labels = {'x': 'X Coordinate', 'y': 'Y Coordinate'}
    fig = px.scatter(x=rw.x_values, y=rw.y_values, title=title, labels=labels)

    # Further customize chart.
    fig.update_layout(
        xaxis=dict(
            dtick=x_dtick  # Áp dụng khoảng cách nhãn cho trục x
        ),
        yaxis=dict(
            dtick=y_dtick  # Áp dụng khoảng cách nhãn cho trục y
        )
    )

    fig.show()

def main():
    """Main function to handle user input and generate walks."""
    while True:
        create_walk_plot()

        keep_running = input("Make another walk? (y/n): ").strip().lower()
        if keep_running != 'y':
            break

if __name__ == "__main__":
    main()
