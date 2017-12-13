# trad-gear-guide
A website that gives quantitative information about what trad climbing protection is needed on different routes.

# download routes
To download routes, run the python script:
```
python download_routes.py <number_of_routes>
```
Make sure you have python3. You also might have to install packages:
```
pip3 install PyQuery
pip3 install sqlite3
```
Each time you run this script, the database is cleared (to avoid duplicate routes).
