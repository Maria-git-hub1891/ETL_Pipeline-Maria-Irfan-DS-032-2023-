import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Assuming you already have the combined_df DataFrame
combined_df = pd.DataFrame({
    'City': ['Karachi', 'Lahore', 'Islamabad'],
    'Temperature (°C)': [30.9, 27.99, 25.47],
    'Humidity (%)': [48, 42, 51],
    'Weather Condition': ['Haze', 'Haze', 'Clear sky']
})

# Print the combined DataFrame
print(combined_df)

# MongoDB connection details

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mariairfan1891:cFeq6EPY9XNowNP8@cluster0.brirekv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Define the database and collection
db = client['city_weather']  # Replace with your actual database name
collection = db['weather_data']     # Replace with your desired collection name

# Convert the DataFrame to a list of dictionaries
data_to_insert = combined_df.to_dict(orient='records')

# Insert the data into MongoDB
try:
    result = collection.insert_many(data_to_insert)
    print(f"Inserted {len(result.inserted_ids)} documents into the collection.")
except Exception as e:
    print(f"An error occurred: {e}")

# Optionally, you can close the client connection when done
client.close()

