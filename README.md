# Bible Games Flashcard App

This project is a mobile application for Bible-themed flashcard games. It consists of a FastAPI backend and a React Native frontend.

## Project Structure

```
bible-games-flashcard-app/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── screens/
│   │   ├── services/
│   │   ├── utils/
│   │   └── App.js
│   ├── package.json
│   └── README.md
│
└── README.md (this file)
```

## Backend

The backend is built with FastAPI and uses PostgreSQL as the database.

### Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your PostgreSQL database and update the connection string in `app/main.py`

6. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`. API documentation can be accessed at `http://localhost:8000/docs`.

## Frontend

The frontend is built with React Native.

### Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npx react-native start
   ```

4. Run the app:
   - For iOS: `npx react-native run-ios`
   - For Android: `npx react-native run-android`

Make sure you have Xcode (for iOS) or Android Studio (for Android) set up on your machine.

## Development Workflow

1. Start by implementing the backend API endpoints.
2. Test the API endpoints using the FastAPI interactive documentation.
3. Move on to the frontend development, integrating with the API as you build out the UI.
4. Test the full application flow regularly.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
