import sqlite3
import random

def init_db():
    conn = sqlite3.connect('themes.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS lieux (id INTEGER PRIMARY KEY, nom TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS actions (id INTEGER PRIMARY KEY, nom TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS personnages (id INTEGER PRIMARY KEY, nom TEXT, nombre TEXT)')

    #adjectifs & adverbes
    c.execute('CREATE TABLE IF NOT EXISTS adjectifs_sujet (id INTEGER PRIMARY KEY, nom TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS adjectifs_lieu (id INTEGER PRIMARY KEY, nom TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS adverbes (id INTEGER PRIMARY KEY, nom TEXT)')

    lieux = ["forest", "city", "desert", "mountain", "castle",]
    actions = ["explores", "combats", "dances", "walks"]
    personnages = [("monkey", "singulier"), ("wizard", "singulier"), ("robots", "pluriel")]

    adjectifs_sujet = ["red", "mysterious", "fast"]
    adjectifs_lieu = ["enchanted", "dangerous", "huge"]
    adverbes = ["quickly", "silently", "joyfully"]

    for lieu in lieux:
        c.execute("INSERT OR IGNORE INTO lieux (nom) VALUES (?)", (lieu,))
    for action in actions:
        c.execute("INSERT OR IGNORE INTO actions (nom) VALUES (?)", (action,))
    for perso, nombre in personnages:
        c.execute("INSERT OR IGNORE INTO personnages (nom, nombre) VALUES (?, ?)", (perso, nombre))
    for adj in adjectifs_sujet:
        c.execute("INSERT OR IGNORE INTO adjectifs_sujet (nom) VALUES (?)", (adj,))
    for adj in adjectifs_lieu:
        c.execute("INSERT OR IGNORE INTO adjectifs_lieu (nom) VALUES (?)", (adj,))
    for adv in adverbes:
        c.execute("INSERT OR IGNORE INTO adverbes (nom) VALUES (?)", (adv,))
    
    conn.commit()
    conn.close()

def get_random_item(table):
    conn = sqlite3.connect('themes.db')
    c = conn.cursor()
    if table == "personnages":
        result = random.choice(c.execute(f"SELECT nom, nombre FROM {table}").fetchall())
        conn.close()
        return result  # Retourne un tuple (nom, nombre)
    else:
        item = random.choice(c.execute(f"SELECT nom FROM {table}").fetchall())[0]
        conn.close()
        return item

if __name__ == "__main__":
    init_db()
    print(get_random_item("lieux"))
    print(get_random_item("actions"))
    print(get_random_item("personnages"))