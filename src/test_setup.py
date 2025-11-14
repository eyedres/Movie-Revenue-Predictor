import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
import sklearn
import requests
from dotenv import load_dotenv
import os

print("Testing setup...\n")

# Load environment variables
load_dotenv()

# Test API key
api_key = os.getenv('TMDB_API_KEY')
if api_key:
    print(f"✓ API Key loaded: {api_key[:10]}...")
else:
    print("✗ API Key not found! Check your .env file")
    exit()

# Test API call
print("\nTesting TMDB API connection...")
url = f"https://api.themoviedb.org/3/movie/550?api_key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    movie = response.json()
    print(f"✓ API Connection Successful!")
    print(f"\nTest movie: {movie['title']}")
    print(f"Budget: ${movie['budget']:,}")
    print(f"Revenue: ${movie['revenue']:,}")
else:
    print(f"✗ API Error: {response.status_code}")

# Test libraries
print("\n✓ All libraries imported successfully!")
print(f"  - Pandas: {pd.__version__}")
print(f"  - NumPy: {np.__version__}")
print(f"  - Scikit-learn: {sklearn.__version__}")
print("\nSetup complete! You're ready to start collecting data.")