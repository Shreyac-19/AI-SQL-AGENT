import matplotlib.pyplot as plt

def plot_data(df):
    fig, ax = plt.subplots()

    if "Name" in df.columns and "Salary" in df.columns:
        ax.bar(df["Name"], df["Salary"])
        ax.set_title("Salary by Employee")
        ax.set_xlabel("Employee Name")
        ax.set_ylabel("Salary")

    else:
        ax.text(0.5, 0.5, "Required columns not found", ha='center')

    return fig