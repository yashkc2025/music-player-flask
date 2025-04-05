# 🎵 Music Streaming App

A full-featured music streaming application that allows users to upload, listen to music, create playlists, and share them publicly.

[![Demo Video](https://img.shields.io/badge/Demo-Video-red)](https://drive.google.com/file/d/1V7R4mLp9PoQrP3tFC06m2_YAZsOy3k2s/view?usp=sharing)

## 📋 Features

- **User Authentication**: Secure login and registration system
- **Music Upload & Playback**: Upload and stream your favorite tracks
- **Playlist Management**: Create, edit, and share playlists
- **Song Rating**: Upvote/downvote system for songs
- **User Dashboard**: Manage your uploaded songs and playlists
- **Admin Panel**: View app performance metrics and manage users

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-RESTful
- **Frontend**: Jinja2 templates
- **Database**: SQLite3
- **Audio Processing**: Mutagen
- **Deployment**: Render

## 📊 Database Schema

The application uses SQLite with 5 main tables:

### Albums Table
```sql
CREATE TABLE "albums" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "ALBUMNAME" TEXT,
    "ARTIST" TEXT,
    "GENRE" TEXT,
    "DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "USER" INTEGER
)
```

### Playlists Table
```sql
CREATE TABLE "playlists" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "PLAYLISTNAME" TEXT,
    "DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "SONGS" TEXT,
    "USER" INTEGER
)
```

### Songs Table
```sql
CREATE TABLE "songs" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NAME" TEXT,
    "ALBUMID" TEXT,
    "ALBUMNAME" TEXT,
    "ARTIST" TEXT,
    "UPVOTES" INTEGER NOT NULL DEFAULT 0,
    "DOWNVOTES" INTEGER NOT NULL DEFAULT 0,
    "DURATION" INTEGER NOT NULL DEFAULT 0,
    "SONGFILE" TEXT,
    "LYRICS" TEXT,
    "DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "USER" INTEGER
)
```

### Users Table
```sql
CREATE TABLE "users" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "EMAIL" TEXT,
    "PASSWORD" TEXT,
    "TYPE" INTEGER,
    "NAME" TEXT,
    "BLOCKED" INTEGER NOT NULL DEFAULT 0,
    "DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP
)
```

The database also includes the standard SQLite system table `sqlite_sequence` for managing autoincrement fields.

## 🔌 API Endpoints

The application provides 9 RESTful API endpoints supporting POST & GET requests for various operations.

## 🏗️ Project Structure

```
music-streaming-app/
├── app.py              # Main entry point
├── functions/          # Core functionality
├── api/
│   └── api.py          # RESTful API definitions
├── db/
│   ├── database.db     # SQLite database
│   └── ...             # Database utilities
└── templates/          # Jinja2 templates
```

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/music-streaming-app.git
   cd music-streaming-app
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database
   ```bash
   python init_db.py
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## 👥 User Types

- **Regular Users**: Upload songs, create playlists, rate songs
- **Admin**: Access to admin panel, user management, analytics

## 📊 Rating System

The song rating is calculated as:
```
Rating = (Number of Upvotes * 100) / Total Votes
```

## 🔒 Security Features

- Users can only edit songs they've uploaded
- Admin account for platform management
- User blocking/unblocking functionality

## 👨‍💻 Author

**Yash Kumar**  
Web Dev Enthusiast | Interested in Linux and Lower Level Programming  
[Email](mailto:22f3000472@ds.study.iitm.ac.in)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by Yash Kumar
