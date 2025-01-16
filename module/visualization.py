# import matplotlib.pyplot as plt
#
# def visualize_data(data):
#     """Visualize high-risk threats."""
#     if data.empty:
#         print("No data to visualize.")
#         return
#
#     data["category"].value_counts().plot(kind="bar", color="red")
#     plt.title("High-Risk Threat Categories")
#     plt.xlabel("Category")
#     plt.ylabel("Count")
#     plt.show()
import matplotlib.pyplot as plt

def visualize_data(data):
    """Visualize high-risk threats with enhanced styling."""
    if data.empty:
        print("No data to visualize.")
        return

    # Count the occurrences of each category
    category_counts = data["category"].value_counts()

    # Create the plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors)

    # Add labels on top of each bar
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(int(bar.get_height())),
            ha='center',
            fontsize=10
        )

    # Customize the plot
    plt.title("High-Risk Threat Categories", fontsize=16, fontweight='bold')
    plt.xlabel("Threat Categories", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()
