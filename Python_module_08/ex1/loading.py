import importlib
import sys

try:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import requests
    DEPS_OK = True
except ModuleNotFoundError:
    print("""
Dependencies not installed\npoetry add or pip install -r requirements.txt""")
    sys.exit(1)


DEPENDENCIES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "requests": "Network access",
    "matplotlib": "Visualization"
}


def check_dependency(name: str) -> tuple[bool, str | None]:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", None)
        return (True, version)
    except ImportError:
        return (False, None)


def check_all_dependencies(dependencies: dict[str, str]) -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:\n")
    for name, purpose in dependencies.items():
        status, version = check_dependency(name)
        if status:
            print(f"[OK] {name} ({version or 'unknown'}) - {purpose} ready")
        else:
            print(f"[KO] {name} is missing. Install it with")
            print(f"    pip install {name}")
            print(f"    poetry add {name}")


def generate_matrix() -> np.ndarray:
    random_generator = np.random.default_rng(seed=42)
    data = random_generator.normal(loc=50, scale=10, size=1000)
    return np.round(data).astype(int)


def analyze_data(data: np.ndarray) -> pd.DataFrame:
    df = pd.DataFrame({
        "time": np.arange(len(data), dtype=np.int_),
        "signal": data,
    })
    return df


def create_visualization(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(
        df["time"], df["signal"], linewidth=1.5, label="signal", color="green")
    plt.axhline(y=50, color="black", linestyle="--", label="mean (loc=50)")
    plt.title("Matrix signal analysis", fontsize=40, color="Black")
    plt.xlabel("Time")
    plt.ylabel("Signal strength")
    plt.legend()
    plt.savefig("matrix_analysis.png")
    plt.close()


def http_request_bitcoin_price() -> None:
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        today_price = response.json()["bitcoin"]["usd"]
        print(f"Bitcoin's price today is {today_price} USDT")
    except (requests.RequestException, KeyError) as error:
        print(f"HTTP error: {error}")


def main() -> None:
    check_all_dependencies(DEPENDENCIES)
    if not DEPS_OK:
        print("\nInstall everything with:")
        print("    pip install -r requirements.txt")
        print("    poetry install")
        return
    print("\nAnalyzing Matrix data...")
    data = generate_matrix()
    print(f"Processing {len(data)} data points...")
    df = analyze_data(data)
    print("Generating visualization...")
    create_visualization(df)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    print("\nChecking requests: ")
    http_request_bitcoin_price()


if __name__ == "__main__":
    main()
