== Using Databases with Python ==

-- Week 1: Objected Oriented Python

[What is an Object?]

- A program is made up of many cooperating objects
- Instead of being the 'whole program', each object is a little 'island' within
  the program and cooperatively working with other objects.
- A program is made up of one or more objects working together - objects make use
  of each others capabilities

Object
- An Object is a bit of self-contained Code and Data
- A key aspect of the Object approach is to break the problem into smaller
  understandable parts (divide and conquer)
- Objects have boundaries that allow us to ignore unneeded detail
- We have been using objects all along: String Objects, Integer Objects,
  Dictionary Objects, List Objects..

Objects hide detail - they allow us to ignore the detail of 'the rest of the program'.

[Terminology]

- Class: a template 										--> dog
- Method or Message: a defined capability of a class 		--> .bark()
- Field or attribute: a bit of data in a class 				--> length
- Object or Instance: A particular instance of a class 		--> Lassie

[Simple Python Objects]

# Class is a reserved word
# This is the template for making PartyAnimal objects

class PartyAnimal:

	x = 0 # Each PartyAnimal object has a bit of data

	def party(self): # Each PartyAnimal object has a bit of code | self is/are the variable(s) passed to the class
		self.x = self.x + 1
		print 'So far', self.x

an = PartyAnimal() # Create a PartyAnimal object
an.party() # Tell the object to run the party() code
an.party() # PartyAnimal.party(an)
an.party()

- 'self' is a formal argument that refers to the object itself
- self.x is saying 'x within self'
- self is 'global within this object'

A Nerdy Way to Find Capabilities
- The dir() command lists capabilities
- Ignore the oneswith underscores, these are used by Python itself
- The rest are real operations that the object can perform
- It is like type() - it tells us something *about* a variable

We can use dir() to find the 'capabilities' of our newly created  class.

[Object Life Cycle]

- Objects are created, used and discarded
- We have special blocks of code (methods) that get called
  + At the moment of creation (constructor)
  + At the moment of destruction (destructor)
- Constructors are used a lot
- Destructors are seldom used

Constructor
- The primary purpose of the constructor is to set up some instance variables
  to have the proper initial values when the object is created

# The constructor and destructor are optional
# The constructor is typically used to set up variables
# The destructor is seldom used

class PartyAnimal:

	x = 0

	def __init__(self):
		print "I am constructed"

	def party(self):
		self.x = self.x + 1
		print "So far", self.x

	def __del__(self):
		print "I am destructed", self.x

an = PartyAnimal #=> I am constructed
an.party() #=> So far 1
an.party() #=> So far 2
an.party() #=> So far 3
# Program now ends (script ends), so: 'I am destructed' is printed

- In object-oriented programming, a constructor in a class is a special 
  block of statements called when an object is created

Many Instances
- We can create lots of objects, the class is the template for the object
- We can store each distinct object in its own variable
- We call this having multiple instances of the same class 
- Each instance has its own copy of the instance variables

class PartyAnimal:

	x = 0
	name = ''

	def __init__(self, nam):
		self.name = nam
		print self.name,'constructed'

	def party(self):
		self.x = self.x + 1
		print self.name, 'party count', self.x

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()

# There are now two independent instances (they have their own values for x and name)

- Constructors can have additional parameters
- These can be used to setup instance variables for the particular 
  instance of the class - i.e. for the particular object

[Inheritance]

- When we make a new class - we can reuse an existing class and inherit all the capabilities
  of an existing class and then add our own little bit to make our new class
- Another form of store and reuse
- Write once and reuse many times
- The new child class has all the capabilities of the old parent class - and then some more

'Subclasses' are more specialized versions of a class, which inherit attributes and behaviors from 
their parent classes, and can introduce their own.

class FootballFan(PartyAnimal):

	points = 0

	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print self.name, 'points', self.points

# FootballFan is a class which extends PartyAnimal
# It has all of the capabilities of PartyAnimal and more

Summary
- Object Oriented programming is a very structured approach to code reuse
- We can group data and functionality together and create many independent instances of a class

-- Week 2: Basic Structured Query Language

[Database Introduction]

SQLite Browser # http://sqlitebrowser.org

Relational Databases
- Relational databases model data by storing rows and columns in tables.
  The power of the relational database lies in its ability to efficiently
  retrieve data from those tables and in particular where there are multiple
  tables and the relationship between those tables involved in the query.

Terminology
 - Database: contains many tables
 - Relation (or table): contains tuples and attributes
 - Tuple (or row): a set of fileds that generally represents an object # like aperson or a music track
 - Attribute (also column or field): one of possibly many elements of data corresponding to the object represented by the row

 A relation is defined as a set of tuples that have the same attributes.
 A tuple usually represents an object and information about that object.
 Objects are typically physical objects or concepts. A relation is usually
 described as a table, which is organized into rows and columns. All the data
 referenced by an attribute are in the same domain and conform to the same 
 constraints (which is described in the schema).

SQL
- Structured Query Language is the language we use to issue commands to the database
  + Create a table
  + Retrieve some data
  + Insert data
  + Delete data
- SQL is the abstraction/API between the end-user and the database

[Using Databases]

Two Roles in Large Projects
+ Application Developer: builds the logic for the application, the look and feel of the 
  application, monitors the application for problems
+ Database Administrator: monitors and adjusts the database as the program runs in production
+ Often both people participate in the building of the 'Data Model'

Database Administrator (DBA)
- A database administrator (DBA) is a person responsible for the design, implementation, maintenance,
  and repair of an organizations database. The role includes the development and design of database
  strategies, monitoring and improving database performance and capacity, and planning for future expansion
  requirements. They may also plan, coordinate, and implement security measures to safeguard the database. 

Database Model # contract of what we are going to store and retrieve in our database
- A database model or database schema is the structure or format of a database, described in a formal language 
  supported by the database management system. In other words, a 'database model' is the application of a data
  model when used in conjunction with a database management system. 

Common Database Systems
- Three Major Database Management Systems in wide use
  + Oracle: large, commercial, enterprise-scale, very very tweakable
  + MySQL: simpler but very fast and scalable, commercial (bought by Oracle) open source
  + SQLServer: very nice, from Microsoft (also Access)
- Many other smaller projects, free and open source
  + HSQL, SQLite, Postgress

[Singe Table CRUD] # Create Read Update Delete

SQLite Browser
- SQLite is a very popular database, it is free and fast and small
- SQLite Browser allows us to directly manipulate SQLite files # http://sqlitebrowser.org/
- SQLite is embedded in Python and a number of other languages

Start Simple - A Single Table # first 'create new database'

CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
) # This is the contract/schema

- Go to 'browse data', click on 'New Record' to insert new rows
- Right corner click on 'SQL Log' to see what SQL was submitted

SQL Insert 
- The INSERT statement inserts a row into a table 
- " INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu') " # corresponding columns/values

SQL Delete
- Deletes a row in a table based on a selection criteria
- " DELETE FROM Users WHERE email = 'ted@umich.edu' "

SQL Update
- Allows the updating of a field with a where clause
- " UPDATE Users SET name = 'Charles' WHERE email = 'csev@umich.edu' "

Retrieving Records: Select
- The select statement retrieves a group of records. You can either retrieve all 
  the records or a subset of the records with a WHERE clause
- " SELECT * FROM Users "
- " SELECT * FROM Users WHERE email = 'csev@umich.edu' "

Sorting with ORDER BY
- You can add an ORDER BY clause to SELECT statements to get
  the results sorted in ascending or descending order
- " SELECT * FROM Users ORDER BY email "

- The hex() function interprets its argument as a BLOB 
  and returns a string which is the upper-case hexadecimal 
  rendering of the content of that blob.
- BLOB: Binary Large Object

[Email Database Demo]

import sqlite3

# we are going to use a database, and store the file in emaildb.sqlite
conn = sqlite3.connect('emaildb.sqlite') # it is making a connection to a sqlite db file
cur = conn.cursor() # create a thing through which you can send commands

cur.execute(''' 
	DROP TABLE IF EXISTS Counts''') # triple quotes are for strings > 1 line

cur.execute('''
	CREATE TABLE COUNTS (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()
	email = pieces[1]
	# The '?' is a placeholder to be filled in, its value is in the tuple next to the string
	# We only need one item in the tuple but without the comma it thinks it is an expression
	# The first '?' in the string is replaced by the first item in the tuple, etc.
	cur.execute('SELECT count FROM Counts WHERE email = ?', (email, )) # the cursor now returns a row set (or potentiall no rows)
	try: # Use a try/except in case the SELECT returns NULL / 0 rows
		# fetchone brings us back one row into memory as a list 
		count = cur.fetchone()[0] # item 0 is the count, since we only selected one column (count)
		cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, )) # set the COLUMN count to the count VALUE + 1 (column/value called the same)
	except: # if the try fails (no e-mail address matches that's already in there), we insert a new row with this e-mail address 
		cur.execute('''INSERT INTO Counts (email, count)
			VALUES (?, 1)''', (email, ))
	conn.commit() # If you have been doing things in memory, write it back to disk; you need to do this else nothing will be committed to the db

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
	print str(row[0]), row[1] # only two values in each row, remember it is returned as a list (and first element is count, hence we convert to a string)

cur.close()

-- Week 3: Data Models and Relational SQL

[Designing a Data Model]

Database Design 
- Database design is an art form of its own with particular skills and experience
- Our goal is to avoid the really bad mistakes and design clean and easily understood databases
- Others may performance tune things later
- Database design starts with a picture

Building a Data Model 
- Drawing a picture of the data objects for our application and then figuring out how to 
  represent the objects and their relationships
- Basic rule: do not put the same string data in twice - use a relationship instead (give it an ID int instead)
- When there is one thing in the 'real world' there should be one copy of that thing in the database

For each "piece of info"...

- Is the column an object or an attribute of another object?
- Once we define objects, we need to define the relationships between objects.

[Representing a Data Model in Tables]

- Primary Key: the key for which there is one key for every row # track
- Foreign Key: one of the colums we add to be the starting point of an arrow to another table # album
- Logical Key: that unique thing that we use when we look up this row from the outside world # track title // we might use it in a WHERE / ORDER BY clause

+ Every table has a primary key 
+ Tables that point to other tables have Foreign Keys

SQLite
- 'Not': NOT NULL
- 'PK': Primary Key 
- 'AI': Auto-Increment (1, 2, 3, ... etc.)
- 'U': Unique

'''CREATE TABLE 'Artists' (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'name' TEXT 
	);'''

You create tables 'leaves-in', from leaves to main-table (tree).

'''CREATE TABLE Genre (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	'name' TEXT
	);'''

'''CREATE TABLE Album (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	'artist_id' INTEGER,
	'title' TEXT
	);'''

'''CREATE TABLE Track (
	'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	'title' TEXT,
	'album_id' INTEGER,
	'genre_id' INTEGER,
	len INTEGER, rating INTEGER, count INTEGER
	);'''

[Inserting Relational Data]

# not specifying id field --> AUTOINCREMENT
'INSERT INTO Artists (name) VALUES ('Led Zeppelin')' #1 
'INSERT INTO Artists (name) VALUES ('AC/DC')' #2

'INSERT INTO Genre (name) VALUES ('Rock')'
'INSERT INTO Genre (name) VALUES ('Metal')'

'INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2)' # 2 == AC/DC
'INSERT INTO Album (title, artist_id) VALUES ('IV', 1)' # 1 == Led Zeppelin

'INSERT INTO Track (title, rating, len, count, album,_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1)'
'INSERT INTO Track (title, rating, len, count, album,_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1)'
'INSERT INTO Track (title, rating, len, count, album,_id, genre_id) VALUES ('About to Rock', 5, 313, 0, 1, 2)'
'INSERT INTO Track (title, rating, len, count, album,_id, genre_id) VALUES ('Who Made Who', 5, 207, 0, 1, 2)'

# Replication is fine as long as they are numbers!
# Reduce the number that needs to me scanned: a number (4 chars), and a string (could be 128 chars)

[Reconstructing Data with JOIN]

Relational Power 
- By removing the replicated data and replacing it with references to a single copy of each bit of data 
  we build a 'web' of information that relational database can read through very quickly - even for 
  very large amounts of data 
- Often when you want some data it comes from a number of tables linked by these foreign keys

The JOIN Operation 
- The JOIN operation links across several tables as part of a select operation 
- You must tell the JOIN how to use the keys that make the connection between 
  the tables using an ON clause

'SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id'
'SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id'
'SELECT Track.title, Genre.name FROM Track JOIN Genre' # omitting the ON clause results in 'all combinations': 4 tracks * 2 genres = 8 rows
# Joining two talbes without an ON clause gives all possible combinations of rows
# The ON clause is picking the ones that match (or removing the ones that don't match)

It can get complex... 

'''
SELECT
  Track.title,
  Artist.name,
  Genre.name
FROM Track 
JOIN Genre 
JOIN Album
JOIN Artist 
ON  Track.genre_id = Genre.id
AND Track.album_id = Album.id 
AND Album.artist_id = Artist_id  
'''

# The output contains string replication, but that is fine in the output
# It isn't stored in the database that way, we reconstruct it with JOINs

[Multi-table Tracks Demo]

import xml.etree.ElementTree as ET 
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some tables | UNIQUE : can't store two identical values in there
cur.execute('''
	CREATE TABLE IF NOT EXISTS Artist (
		'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		'name' TEXT UNIQUE 
		)''')

cur.execute('''
	CREATE TABLE IF NOT EXISTS Album (
		'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		'artist_id' INTEGER,
		'title' TEXT UNIQUE
		)''')

cur.execute('''
	CREATE TABLE IF NOT EXISTS Track (
		'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		'title' TEXT UNIQUE,
		'album_id' INTEGER,
		'len INTEGER, rating INTEGER, count INTEGER
		)''')

fname = raw_input('Enter file name: ')
if( len(fname) < 1) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def lookup(d, key):
	found = False
	for child in d:
		if found : return child.text
		if child.tag == 'key' and child.text == key :
			found = True # in the NEXT loop iteration it will return the found text
		return None

# Next time round the loop, because the variable found is now true, 
# we can simply take the new child.text which will be the contents 
# of the <string>. We return with this value. Another one bites the dust.

are we looking at text we want, such as 'Name'? In which case we have found <key>Name</key>. Hoorah! We found it. We now know the next tag will be a string containing the actual track name.

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict') # 3-deep dictionary, at the third level are tracks
print 'Dict count:', len(all)

for entry in all:
	if (lookup(entry, 'Track ID') is None) : continue

	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	count = lookup(entry, 'Play Count')
	rating = lookup(entry, 'Rating')
	length = lookup(entry, 'Total Time')

	if name is None or artist is None or album is None : continue

	print name, artist, album, count, rating, length 

	cur.execute('''INSERT OR IGNORE INTO Artist (name) # we use UNIQUE above, we cannot use the same name twice
		VALUES( ? )''', (artist, ))                    # INSERT OR IGNORE --> if fails: IGNORE (when it is already there)
	cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,)) # one-item tuple, you need to still put the ','
	artist_id = cur.fetchone()[0] # only fetch one row (fetchone) --> should already be the case since we used UNIQUE

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
		VALUES (?, ?)''', (album, artist_id))
	cur.execute('SELECT id FROM album WHERE title = ?', (album, ))

	cur.execute('''INSERT OR REPLACE INTO Track # if the title doesn't exist --> insert rows
		(title, album_id, len, rating, count)   # if the title does exist --> update it
		VALUES(?, ?, ?, ?, ?)''',
		(name, album_id, length, rating, count))

    conn.commit()

-- Week 4: Many-to-Many Relationships in SQL

cur.executescript() : allows for many SQL statements to be executed separated by semi-colons (;).

[Many-to-Many Relationships]

- Sometimes we need to model a relationship that is many-to-many # to two many-to-1 
- We need to add a 'connection' table with two foreign keys 
- There is usually no separate primary key # i.e. a primary key to identify the foreign key - foreign key mapping
  + If you add the two numbers together, you basically get the PK (composite key)

'''
CREATE TABLE User (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT,
	email TEXT
	)

CREATE TABLE Course (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT
	)

CREATE TABLE Member (
	user_id INTEGER,
	course_id INTEGER, 
	role INTEGER,
	PRIMARY KEY (user_id, course_id)
	)
'''

Insert Users and Courses

'''
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
'''

How Its Connected

'''
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course 
ON Member.user_id = User.id AND Member.course_id = Course.id 
ORDER BY Course.title, Member.role DESC, User.name
'''

[Many-to-Many Roster Demo] 

Junction/Many-to-Many Table
- Contains at least two foreign keys (mapping the relationship)
- Can contain more data (that is unique to the specific relationship) # 'role' in the given student/courses example
- There is no Primary Key but a Composite Key, which is the two Foreign Keys combined

---

import json
import sqlite3

conn  = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup, executescript() allows you to execute multiple SQL statements in one string
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
);

CREATE TABLE Course (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE
);

CREATE TABLE Member (
	user_id INTEGER,
	course_id INTEGER,
	PRIMARY KEY (user_id, couse_id) -- Composite Key
);
''')

fname = raw_input('Enter file name: ')
if(len(fname) < 1) : fname = 'roster_data.json'

# [
#   ['Charley', 'si110', 1],
#   ['Mea', 'si110', 0],

str_data = open(fname).read() # read everything into one big string
json_data = json.loads(str_data)

for entry in json_data: 

	name = entry[0];
	title = entry[1];

	print name, title 

	# INSERT OR IGNORE --> if this insert fails, do nothing
	# Remember the UNIQUE restriction on name (l596)
	# If the name is already in the table,
	# the INSERT will fail and thus be IGNOREd (so every unique name will get an id)

	cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
	cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
	user_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title, ))
	cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
	course_id = cur.fetchone()[0]

	# INSERT OR REPLACE(/UPDATE): avoids duplicates, makes sure Composite Key remains unique

	cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id) VALUES (?, ?)', (user_id, course_id)) 

	conn.commit()

-- Week 5: Databases and Visualization

[Geocoding]
# http://www.pythonlearn.com/code/geodata.zip

Many Data Mining Technologies
- https://hadoop.apache.org/
- https://spark.apache.org/
- https://aws.amazon.com/redshift/
- https://community.pentaho.com/

"Personal Data Mining"
- Our goal is to make you better programmers - not to make you data 
mining experts!

GeoData 
- Make a Google Map from user entered data
- Uses the Google Geodata API
- Caches data in a database to avoid rate limiting and allow restarting
- Visualized in a browser using the Google Maps API 

[Page Rank and Web Searching]

Page Rank
- Write a simple web page crawler
- Compute a simple version of Googles Page Rank algorithm
- Visualize the resulting network

Search Engine Architecture
- Web Crawling
- Index Building
- Searching

Web Crawler
- A Web crawler is a computer program that browses the World Wide Web in a 
  methodical, automated manner. Web crawlers are mainly used to create a copy
  of all the visited pages for later processing by a search engine that will 
  index the downloaded pages to provide fast searches.
  + Retrieve a page
  + Look through the page for links
  + Add the links to a list of 'to be retrieved' sites 
  + Repeat...

Web Crawling Policy
- a 'selection policy' that states which pages to download
- a 're-visit policy' that states when to check for changes to the pages
- a 'politeness policy' that states how to avoid overloading Web sites 
- a 'parallelization policy' that states how to coordinate distributed Web crawlers

robots.txt
- A way for web sites to communicate with web crawlers
- An informal and voluntary standard
- Sometimes folks make a 'Spider Trap' to catch 'bad' spiders

Search Indexing
- Search engine indexing collects, parses, and stores data to facilitate
  fast and accurate information retrieval. The purpose of storing an index is 
  to optimize speed and performance in finding relevant documents for a search 
  query. Without an index, the search engine would scan every document in the 
  corpus, which would require considerable time and computing power.

[Gmane - Mailing Lists]
# http://www.pythonlearn.com/code/gmane.zip

- Crawl the archive of a mailing list
- Do some analysis / cleanup
- Visualize the data as word cloud and lines

Warning: This Dataset is > 1 GB
- Do not just point this application at gmane.org and let it run all night
- There is no rate limits - these are cool folks
- Do not ruin it for the rest of us 
- We will have a non-rate-limited copy of this available

[GeoCoding API Demo]

== geoload.py ==

import urllib
import sqlite3
import json
import time

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')

fh = open('where.data')
count = 0

for line in fh:
	if count > 200 : break
	address = line.strip()
	print ''
	# The first time this won't work (when you don't have the address yet)
	# buffer is a way to force it to what we want to be (in case it is Unicode)
	cur.execute('SELECT geodata FROM Locations WHERE address = ?', (buffer(address), )) # (buffer(address), ) = 1-value tuple

	try:
		data = cur.fechtone()[0]
		print "Found in database ", address
		continue
	except:
		pass

	# If we do not have the address already, we continue here
	print 'Resolving', address
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved', len(data), 'characters', data[:20].replace('\n',' ') # last part replaces newlines with white spaces so that all is printed on one row
	count = count + 1
	try:
		js = json.load(str(data))
		# print js # we print in case of errors
	except:
		continue

	if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
		print '=== Failure to Retrieve ==='
		print data
		break

	cur.execute('''INSERT INTO Locations (address, geodata) VALUES 
		           (?,?)''', (buffer(address), buffer(data)))

	conn.commit()
	time.sleep(1) # wait one second; so we're not moving too fast

print 'Run geodump.py to read the data from the database so you can visualize it on a map.'

# Use 'cntrl + c' to force quit a program/script

== geodump.py ==

import sqlite3
import json
import codecs

conn.sqlite3connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations') 
fhand = codecs.open('where.js', 'w', 'utf-8') # write to a JSON file called where.js
fhand.write('myData = [\n')
count = 0
for row in cur : # loops through all the rows that are opened in the cursor
	data = str(row[1]) # 0 = address, 1 = geodata
	try:
		js = json.loads(str(data))
	except:
		continue

	if not('status' in js and js['status'] == 'OK') : continue

	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	if lat == 0 or lng == 0 : continue
	where = js['results'][0]['formatted_address']
	where = where.replace("'","")
	
	try:
		print where, lat, lng 

		count = count + 1
		if count > 1 : fhand.write(',\n') # add a newline (enter once)
		output = "["+str(lat)+","+str(lng)+",'"+where+"']"
		fhand.write(output)
	except:
		continue

fhand.write("\n];\n")
cur.close() 
fhand.close()
print count, "records written to where.js"

--

Run in terminal: 'open where.html'