import mysql.connector

# Database connection
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="CansinErdi",
        password="Cansin14.",  # Add your MySQL password here
        database="film_collection"
    )

# Add a film
def add_film(title, director, genre, release_year, rating):
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO films (title, director, genre, release_year, rating) VALUES (%s, %s, %s, %s, %s)"
    values = (title, director, genre, release_year, rating)
    cursor.execute(query, values)
    db.commit()
    print(f"Film '{title}' added.")
    db.close()

# Delete a film
def delete_film(film_id):
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM films WHERE id = %s"
    cursor.execute(query, (film_id,))
    db.commit()
    print(f"Film with ID {film_id} deleted.")
    db.close()

# Update film information
def update_film(film_id, title, director, genre, release_year, rating):
    db = connect()
    cursor = db.cursor()
    query = """
        UPDATE films
        SET title = %s, director = %s, genre = %s, release_year = %s, rating = %s
        WHERE id = %s
    """
    values = (title, director, genre, release_year, rating, film_id)
    cursor.execute(query, values)
    db.commit()
    print(f"Film with ID {film_id} updated.")
    db.close()

# Search for films related to George Lucas (director or producer)
def search_george_lucas():
    db = connect()
    cursor = db.cursor()
    query = """
        SELECT * FROM films
        WHERE director LIKE %s OR title LIKE %s
    """
    cursor.execute(query, ('%George Lucas%', '%George Lucas%'))
    results = cursor.fetchall()
    if results:
        print("George Lucas-related films:")
        for film in results:
            print(film)
    else:
        print("No George Lucas-related films found.")
    db.close()

# Test: Add George Lucas films and search
if __name__ == "__main__":
    # Adding example George Lucas-related films
    add_film("Star Wars: A New Hope", "George Lucas", "Science Fiction", 1977, 8.6)
    add_film("Star Wars: The Empire Strikes Back", "George Lucas (Producer)", "Science Fiction", 1980, 8.7)
    add_film("Indiana Jones: Raiders of the Lost Ark", "George Lucas (Producer)", "Adventure", 1981, 8.4)

    # Search for George Lucas films
    search_george_lucas()

def sort_films_by_rating():
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM films ORDER BY rating DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    for film in results:
        print(film)
    db.close()
