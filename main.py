import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_gdp_data(countries):
    url = f"https://api.worldbank.org/v2/country/{countries}/indicator/NY.GDP.MKTP.KD.ZG?format=json"
    
    response = requests.get(url)
    data = response.json()[1]

    df = pd.DataFrame(data)

    df = df[["country", "date", "value"]]
    df["country"] = df["country"].apply(lambda x: x["value"])
    df["date"] = df["date"].astype(int)
    df = df.dropna()

    return df

def plot_data(df):
    pivot_df = df.pivot(index="date", columns="country", values="value")
    pivot_df = pivot_df.sort_index()

    ax = pivot_df.plot(
        title="GDP Growth (%) Comparison",
        figsize=(10,5),
        linewidth=2
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Growth (%)")
    ax.grid(True)

    plt.tight_layout()
    plt.show()

def show_stats(df):
    print("\nSummary Stats:\n")

    summary = df.groupby("country")["value"].agg([
        "mean",
        "min",
        "max"
    ])

    print(summary)


if __name__ == "__main__":
    print("Enter countries (example: US;IL;DE): ")
    countries = input()

    df = get_gdp_data(countries)

    show_stats(df)   
    plot_data(df)