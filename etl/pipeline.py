import yaml
import pandas as pd

def load_config(path="../config/config.yaml"):
    """Load the YAML configuration file."""
    with open(path, "r") as f:
        return yaml.safe_load(f)

def extract(source_file):
    df = pd.read_csv(source_file)
    return df

def transform(df, config):
    if config["transform"].get("drop_na"):
        df = df.dropna()
    columns = config["transform"].get("columns_to_keep", [])
    if columns:
        df = df[columns]
    return df

def load(df, destination_file):
    df.to_csv(destination_file, index=False)

def main():
    config = load_config()
    source = config["etl"]["source_file"]
    dest = config["etl"]["destination_file"]

    df = extract(source)
    df = transform(df, config)
    load(df, dest)
    print("ETL completed.")

if __name__ == "__main__":
    main()
