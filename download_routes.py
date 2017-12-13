from pyquery import PyQuery
import sys
import sqlite3

PAGE_SIZE = 50
global conn

def getProtection(sections):
    for section in sections:
        headers = section.cssselect("h2")
        for h in headers:
            if "Protection" == h.text_content().strip():
                return section.text_content().strip()[12:].strip() # remove all white space and also "Protection" header
    return None

def connect_db():
    global conn
    conn = sqlite3.connect('routes.db')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS routes''')
    c.execute('''CREATE TABLE routes (
             id INT NOT NULL,
             html VARCHAR NOT NULL,
             protection VARCHAR NOT NULL,
             url VARCHAR(200) NOT NULL,
             PRIMARY KEY (id))''')
    conn.commit()

def close_db():
    conn.close()

def insert_route(id, html, protection, url):
    c = conn.cursor()
    c.execute('''INSERT INTO routes
                VALUES (?, ?, ?, ?)''', [id, html, protection, url])
    conn.commit()

def main():
    connect_db()
    n_routes = int(sys.argv[1]) if len(sys.argv) > 1 else PAGE_SIZE
    pages = int(n_routes / PAGE_SIZE) + 1
    print("Querying data...")

    id = 0
    for i in range(1, pages+1):
        html = None
        try:
            html = PyQuery(url='https://www.mountainproject.com/route-finder?diffMaxaid=75260&diffMaxboulder=21400&diffMaxice=38500&diffMaxmixed=60000&diffMaxrock=6800&diffMinaid=70000&diffMinboulder=20000&diffMinice=30000&diffMinmixed=50000&diffMinrock=1000&is_trad_climb=1&pitches=0&selectedIds=0&stars=0&type=rock&page=' + str(i))
        except:
            continue
        route_urls = [a.attrib.get("href") for a in html(".hidden-xs-down")(".route-row")("a:first")]

        for url in route_urls:
            try:
                html = PyQuery(url)
            except:
                continue
            sections = html(".col-xs-12")("div.m-t-2")
            pro = getProtection(sections)
            if pro is not None:
                insert_route(id, str(html), pro, url)
                id = id + 1
                if id > n_routes:
                    break

    close_db()
    print("Inserted %d routes." % id - 1)

if __name__ == "__main__":
    main()
