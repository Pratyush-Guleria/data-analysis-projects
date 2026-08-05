import pandas as pd

def load_data(path):

    try:
        df = pd.read_csv(path)
        print("✅ File found Successfully\n")
        return df
    
    except FileNotFoundError as e:
        print("❌ File Not Found")
        print(f"🔍 :{e}")
        raise