from bson import ObjectId
from app.schemas.user import UserCreate, UserList
from pymongo.database import Database
import hashlib

# User CRUD operations
def create_user(db: Database, user: UserCreate):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    del user_dict["password"]
    # Insert the user into the database
    result = db.users.insert_one(user_dict)

    # Retrieve the inserted user document
    created_user = db.users.find_one({"_id": result.inserted_id})

    # Convert the ObjectId to a string
    created_user["id"] = str(created_user["_id"])
    del created_user["_id"]

    return created_user


def get_user(db: Database, user_id: str):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["id"] = str(user["_id"])
        del user["_id"]
    return user


def get_user_by_email(db: Database, email: str):
    user = db.users.find_one({"email": email})
    if user:
        user["id"] = str(user["_id"])
        del user["_id"]
    return user


def get_users(db: Database, skip: int = 0, limit: int = 100):
    users = list(db.users.find().skip(skip).limit(limit))
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
    total = db.users.count_documents({})
    return UserList(users=users, total=total)


def delete_user(db: Database, user_id: str):
    user = db.users.delete_one({"_id": ObjectId(user_id)})
    if user.deleted_count:
        return {"id": user_id}


# Category CRUD operations
# def create_category(db: Database, category: CategoryCreate):
#     category_dict = category.dict()
#     result = db.categories.insert_one(category_dict)
#     return db.categories.find_one({"_id": result.inserted_id})

# def get_category(db: Database, category_id: str):
#     return db.categories.find_one({"_id": ObjectId(category_id)})

# def get_categories(db: Database, skip: int = 0, limit: int = 100):
#     return list(db.categories.find().skip(skip).limit(limit))

# def update_category(db: Database, category_id: str, category: CategoryUpdate):
#     result = db.categories.update_one(
#         {"_id": ObjectId(category_id)},
#         {"$set": category.dict(exclude_unset=True)}
#     )
#     if result.modified_count > 0:
#         return db.categories.find_one({"_id": ObjectId(category_id)})
#     return None

# def delete_category(db: Database, category_id: str):
#     result = db.categories.delete_one({"_id": ObjectId(category_id)})
#     return result.deleted_count > 0