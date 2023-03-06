import sqlite3

conn = sqlite3.connect("convert_table.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS sae_met_tabl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sae_size REAL NOT NULL,
    metric_size REAL NOT NULL)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS met_sae_tabl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metric_size REAL NOT NULL,
    sae_size REAL NOT NULL)"""
)

c.execute("INSERT INTO sae_met_tabl VALUES(1,'15/16','24')" )
c.execute("INSERT INTO met_sae_tabl VALUES(1,'24','15/16')" )

conn.commit()
conn.close()
