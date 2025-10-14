# actions/database.py

import psycopg2
from . import config

def get_connection():
    """Get database connection."""
    return psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        port=config.DB_PORT,
        sslmode='require'
    )

def save_master_sheet_id(sheet_id):
    """Save master sheet ID to database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bot_config SET master_sheet_id = %s WHERE id = 1;
            INSERT INTO bot_config (id, master_sheet_id) 
            SELECT 1, %s WHERE NOT EXISTS (SELECT 1 FROM bot_config WHERE id = 1);
        """, (sheet_id, sheet_id))
        conn.commit()
    finally:
        conn.close()

def save_active_sheet_id(sheet_id):
    """Save active sheet ID to database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bot_config SET active_sheet_id = %s WHERE id = 1;
            INSERT INTO bot_config (id, active_sheet_id) 
            SELECT 1, %s WHERE NOT EXISTS (SELECT 1 FROM bot_config WHERE id = 1);
        """, (sheet_id, sheet_id))
        conn.commit()
    finally:
        conn.close()

def get_master_sheet_id():
    """Get master sheet ID from database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT master_sheet_id FROM bot_config LIMIT 1")
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        conn.close()

def get_active_sheet_id():
    """Get active sheet ID from database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT active_sheet_id FROM bot_config LIMIT 1")
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        conn.close()