import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "chat.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=10000")
    return conn


def init_db():
    conn = get_connection()
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                created_by INTEGER,
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                username TEXT NOT NULL,
                content TEXT NOT NULL,
                emoji_rendered TEXT,
                created_at TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%S','now','localtime')),
                FOREIGN KEY (room_id) REFERENCES rooms(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            """
        )
        conn.commit()
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

def create_user(username, password):
    conn = get_connection()
    try:
        existing = conn.execute(
            "SELECT id FROM users WHERE username = ?", (username,)
        ).fetchone()
        if existing:
            return None
        password_hash = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash),
        )
        conn.commit()
        return conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
    finally:
        conn.close()


def verify_user(username, password):
    conn = get_connection()
    try:
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            return user
        return None
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def get_or_create_room(name, user_id):
    name = name.strip()
    if not name:
        return None
    conn = get_connection()
    try:
        room = conn.execute(
            "SELECT * FROM rooms WHERE name = ?", (name,)
        ).fetchone()
        if room:
            return room
        conn.execute(
            "INSERT INTO rooms (name, created_by) VALUES (?, ?)",
            (name, user_id),
        )
        conn.commit()
        return conn.execute(
            "SELECT * FROM rooms WHERE name = ?", (name,)
        ).fetchone()
    finally:
        conn.close()


def list_rooms():
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT r.id, r.name,
                   (SELECT COUNT(*) FROM messages m
                     WHERE m.room_id = r.id) AS message_count
            FROM rooms r
            ORDER BY r.name
            """
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------

def save_message(room_id, user_id, username, content, emoji_rendered):
    conn = get_connection()
    try:
        conn.execute(
            """
            INSERT INTO messages
                (room_id, user_id, username, content, emoji_rendered)
            VALUES (?, ?, ?, ?, ?)
            """,
            (room_id, user_id, username, content, emoji_rendered),
        )
        conn.commit()
        return conn.execute(
            "SELECT * FROM messages WHERE id = last_insert_rowid()"
        ).fetchone()
    finally:
        conn.close()


def get_message_history(room_id, limit=100):
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT id, username, content, emoji_rendered, created_at
            FROM messages
            WHERE room_id = ?
            ORDER BY id
            LIMIT ?
            """,
            (room_id, limit),
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


def format_message_for_client(row):
    """Normalize a DB message row into the JSON shape sent over the socket."""
    return {
        "id": row["id"],
        "username": row["username"],
        "content": row["content"],
        "emoji_rendered": row["emoji_rendered"],
        "created_at": row["created_at"],
    }