from contextlib import contextmanager
import sqlite3


class Database:

    def connect_to_db(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                membership_type TEXT,
                sessions TEXT
            )
        """)

    def get_all(self):
        self.cur.execute("SELECT * FROM members")
        rows = self.cur.fetchall()
        return [self._row_to_dict(row) for row in rows]

    def get(self, id):
        self.cur.execute("SELECT * FROM members WHERE id = ?", (id,))
        row = self.cur.fetchone()
        return self._row_to_dict(row) if row else None

    def create(self, item):
        self.cur.execute("SELECT MAX(id) FROM members")
        result = self.cur.fetchone()
        new_id = (result[0] or 0) + 1

        data = item.model_dump()
        data["sessions"] = str(data["sessions"])  # convert list to string

        self.cur.execute("""
            INSERT INTO members VALUES (:id, :name, :age, :membership_type, :sessions)
        """, {"id": new_id, **data})

        self.conn.commit()
        return new_id

    def update(self, id, item):
        data = item.model_dump()
        data["sessions"] = str(data["sessions"])  # convert list to string

        self.cur.execute("""
            UPDATE members
            SET name = :name,
                age = :age,
                membership_type = :membership_type,
                sessions = :sessions
            WHERE id = :id
        """, {"id": id, **data})

        self.conn.commit()
        return self.get(id)

    def delete(self, id):
        self.cur.execute("DELETE FROM members WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def _row_to_dict(self, row):
        return {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "membership_type": row[3],
            "sessions": row[4]
        }


@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()
    db.create_table()
    try:
        yield db
    finally:
        db.close()