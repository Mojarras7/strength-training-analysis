import pandas as pd
import glob
import os
import numpy as np

def process_csv(d_raw, d_processed):
    """
    
    """

    csvFiles = glob.glob(os.path.join(d_raw, "*.csv"))

    if not csvFiles:
        print("No CSV files found in the specified directory")
        return

if __name__ == "__main__":


    process_csv()