import pandas as pd
import matplotlib.pyplot as plt


def load_and_clean_data(file_path):
    """
    Load sales data and perform cleaning
    """

    sales = pd.read_csv(file_path)

    sales["unit_price"] = pd.to_numeric(
        sales["unit_price"],
        errors="coerce"
    )

    sales["store"] = (
        sales["store"]
        .str.strip()
        .str.title()
    )

    sales["revenue"] = (
        sales["quantity"]
        * sales["unit_price"]
    )

    return sales


def save_chart(title, filename):
    """
    Save charts to the charts folder
    """

    plt.title(title)

    plt.tight_layout()

    plt.savefig(
        f"data/charts/{filename}"
    )