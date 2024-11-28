from cs50 import SQL
def first():
    fixers = ('Adventure Time', 'Arrow', 'Avatar: The Last Airbender', 'Brooklyn Nine-Nine', 'Community', 'Family Guy', 'Friends', 'Game of Thrones', 'Gilmore Girls', "Grey's Anatomy", "How I Met Your Mother", "It's Always Sunny in Philadelphia", "Parks and Recreation", "Sherlock", "Squid Game", "The Bachelorette", "The Crown", "The Office", "The Queen's Gambit", "The Untamed")
    print(len(fixers))
    for i in range(len(fixers)):

        db = SQL("sqlite:///favorites.db")

        rows = db.execute("UPDATE shows SET title = ? WHERE title LIKE ?", fixers[i], fixers[i])
        print(rows)
def second():
    fixers = ('Billions', 'Brooklyn 99', 'Criminal Minds', 'Sherlock Holmes')
    for i in range(len(fixers)):

        db = SQL("sqlite:///favorites.db")

        rows = db.execute("UPDATE shows SET title = ? WHERE title LIKE ?", fixers[i], fixers[i])
        print(rows)


first()
# second()
