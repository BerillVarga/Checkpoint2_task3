import psycopg2
conn = psycopg2.connect(
   host = "localhost",
   port = '5432',
   database = "dict2",
   user = "postgres",
   password = '***'
   )


# Reads the database and returns all entries
def read_dict(connection):
    cur = connection.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

# Adds a new entry to the db
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

# A function that doesn't do anything :)
def insert_word(connection, word, translation):
    print(f"The word '{word}' with the translation '{translation}' is now inserted")

# Deletes an etry from the db
def delete_word(connection, ID):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

# Saves the changes
def save_dict(connection):
    cur = connection.cursor()
    cur.execute("COMMIT;")
    cur.close()


# Initial information text
print('Hello and welcome to the dictionary, available commands:')
print('  add    - add a word\n  list   - list dict content')
print('  insert - insert new word')
print('  delete - delete a word\n  quit   - quit the program')


while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().lower()
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(conn, word, translation)
    elif cmd == 'insert':
        word = input("  Word: ")
        translation = input("  Translation: ")
        insert_word(conn, word, translation)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
