import sqlite3

def init_db():
    conn = sqlite3.connect("issues.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS issues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        priority TEXT
    )
    """)

    # insert dummy data
    cursor.execute("DELETE FROM issues")

    cursor.executemany("""
    INSERT INTO issues (title, category, priority)
    VALUES (?, ?, ?)
    """, [
        ("App crashes on login", "bug", "high"),
        ("Add dark mode", "feature", "medium"),
        ("How to reset password", "question", "low"),
        ("Payment failed error", "bug", "high"),
        ("Improve UI design", "feature", "low")
    ])

    conn.commit()
    conn.close()


def run_query(sql):
    conn = sqlite3.connect("issues.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results

    except Exception as e:
        return {"error": str(e)}

    finally:
        conn.close()