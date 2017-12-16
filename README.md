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


#Usage 
To calculate common n-grams use the following.

```
python3 -i common_grams.py
>>> find_most_common_trigrams(2, True) #(n-gram number, Whether or not to remove stop words)
```