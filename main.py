import argparse
from src.cleaner import clean_data_set

def main():
    parser = argparse.ArgumentParser(description="Data Automation Toolkit");
    parser.add_argument("input",help="path to input CSV file")
    parser.add_argument("output",help="path to save cleaned data")
    parser.add_argument("--format",choices=["csv","json","excel"],default="csv",
                        help="Export format (default : CSV)")
    args = parser.parse_args()
    clean_data_set(args.input, args.output, args.format)

if __name__ == "__main__":
    main()
