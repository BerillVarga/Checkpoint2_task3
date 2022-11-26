import psycopg2
conn = psycopg2.connect(
   host = "localhost",
   port = '5432',
   database = "dict2",
   user = "postgres",
   password = "****"
   )

def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()


# Initial information text
print('Hello and welcome to the dictionary, available commands:')
print('  add    - add a phone number\n  list   - list all phone numbers')
print('  delete - delete a contact\n  quit   - quit the program')


while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().lower()
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
