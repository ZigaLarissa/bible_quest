from pymongo import MongoClient

# database_url = 'mongodb+srv://lbizimungu:S9kmYKTmunyDNjNM@cluster0.gaeuej0.mongodb.net/'
database_url = 'mongodb+srv://lbizimungu:S9kmYKTmunyDNjNM@cluster0.gaeuej0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(database_url)
Database = client['quiz_app']

def get_database():
    return Database