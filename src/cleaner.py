import pandas as pd ;
import numpy as np;

def clean_data_set(input_file:str,output_file:str, output_format:str = "csv"):
    df = pd.read_csv(input_file)
    
    df = df.dropna(thresh=len(df)*0.5,axis=1)
    
    df = df.ffill()
    
    for col in df.select_dtypes(include=np.number):
        df[col] = df[col].fillna(df[col].median())
    
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].fillna(df[col].mode()[0])
        
    string_cols = ["name", "host_name", "neighbourhood", "room_type"]
    df[string_cols] = df[string_cols].astype("string")
    df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")
    
    df["room_type"] = df["room_type"].str.strip().str.lower()
    df["room_type"] = df["room_type"].replace({
    "p" : "Private room",
    "pr": "Private room",
    "e" : "Entire home/apt"
    })
    
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=['host_id'])
    df = df.drop(columns=["id","minimum_nights"], errors="ignore")
    
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.rename(columns={"name": "fullname"})
    
    if output_format == "csv":
        df.to_csv(output_file,index=False)
    elif output_format == "json":
        df.to_json(output_file,orient="records",lines=True)
    elif output_format in ["xls","xlsx","excel"]:
        df.to_excel(output_file,index=False)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")
    
    print(f"✅ Cleaned dataset saved to {output_file}")
    
    
    
    