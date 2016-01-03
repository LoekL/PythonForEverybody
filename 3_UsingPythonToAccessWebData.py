# [Python for Everybody] - Using Python to Access Web Data

print 'hello there!'

-- Week 1

== RegEx ==

'^'  --	Matches the beginning of a line
'$'	 -- Matches the end of the line
'.'  --	Matches any character
'\s' --	Matches whitespace
'\S' --	Matches any non-whitespace character
'*'  -- Repeats a character zero or more times
'*?' -- Repeats a character zero or more times (non-greedy)
'+'  --	Repeats a character one or more times
'+?' -- Repeats a character one or more times (non-greedy)
'[aeiou]'  -- Matches a single character in the listed set --> within lists special characters are NOT wildcards!
'[^XYZ]'   -- Matches a single character not in the listed set --> within lists special characters are NOT wildcards!
'[a-z0-9]' -- The set of characters can include a range
'('  -- Indicates where string extraction is to start
')'	 -- Indicates where string extraction is to end

"""
In computing, a regular expression, also referred to as "regex" or "regexp", provides a concise and
flexible means for matching strings of text, such as particular characters, words, or patterns of
character. A regular expression is written in a formal language that can be interpreted by a regular
expression processor.
"""

The Regular Expression Module

- Before you can use regular expressions in your program, you must import the library using 
"import re"
- You can use re.search() to see if a string matches a regular expression, similar to using 
the find() method for strings
- You can use re.findall() to extract portions of a string that match your regular expression 
similar to a combination of find() and slicing: var[5:10]

-- Finding 'From:' anywhere in the line, 2 methods:

[A]

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:') >= 0: # find returns the position of the string
		print line

[B]

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line): # re.search returns T/F
		print line

-- Finding 'From:' when it is only at the start of the line, 2 methods:

[A] - Change .line to .startswith
[B] - Change 'From:' to '^From:'

- We fine-tune what is matched by adding special characters to the string

Wild-Card Characters

- The dot character matches any character
- If you add the asterisk character, the character is "any number of times"

'^X.*:' # 'X-Content-Type-Message-Body: text/plain'

Fine-Tuning Your Match

- Depending on how 'clean' your data is and the purpose of your application, you may want to narrow
your match down a bit

'^X-\S+:'

'\S' = any non-blank character; so one or more non-whitespace character (regex above)

Would return: 'X-DSPAM-Result: Innocent'
But not: 'X-Plane is behind schedule: two weeks'

Matching and Extracting Data

- The re.search() returns a True/False depending on whether the string matches the regex
- If we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print y 
#=> ['2', '19', '42']

- When we use re.findall(), it returns a list of zero or more sub-strings that match the RegEx

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+')
print y
#=> ['2', '19', '42']
y = re.findall('[AEIOU]+')
print y
#=> []

Warning: Greedy Matching

- The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y
#=> ['From: Using the :']
y = re.findall('^F.+?:', x)
print y
#=> ['From:']

Fine-Tuning String Extraction

- You can refine the match for re.findall() and separately determine which portion of the match
is to be extracted by using paranthesis

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print y
#=> ['stephen.marquard@uct.ac.za']

- Parantheses are not part of the match - but they tell where to start and stop what string to extract

y = re.findall('^From (\S+@\S+)', x) # Only looks at lines that start with from
#=> ['stephen.marquard@uct.ac.za']

-- Previous methodologies

[A] - .find & slicing

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos - data.find('@')
print atpos
#=> 21
sppos = data.find(' ', atpos) # find me the first occurrence of a blank/whitespace after atpos
print sppos
#=> 31
host = data[atpos+1 : sppos]
print host
#=> 'uct.ac.za'

[B] - The Double Split Pattern

- Sometimes we split a line one way, and then grab one of the pieces of the line and split that line again

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1] 			#=> 'stephen.marquard@uct.ac.za'
pieces = email.split('@') 	#=> ['stephen.marquard', 'uct.ac.za']
print pieces[1] 			#=> 'uct.ac.za'

[C] - RegEx Version

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', line)
print y
#=> ['uct.ac.za']

- [^ ] = match non-blank character; inside the brackets '^' means NOT

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	# inside of the brackets '.' is not a wildcard!
		if len(stuff) != 1: continue
		num = float(stuff[0])
		numlist.append(num)

print 'Maximum:', max(numlist)

Escape Character

- If you want a special regular expression character to just behave normally (most of the time)
you prefix it it with a '\'' (backslash)

import re 
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print y
['$10.00'] 

- Regular expressions are a cryptic but powerful language for matching strings and extracting 
elements from those strings
- Regular expression have special characters that indicate intent

-- Week 2

== Networks and Sockets ==

[Networked Programs]

Transport Control Protocol (TCP)
- Built on top of IP (Internet Protocol)
- Assumes IP might lose some data
  + Stores and tetransmits data if it seems to be lost
- Handles 'flow control' using a transmit window
- Provides a nice reliable pipe

TCP Connections / Sockets

"In computer networking, an Internet socket or network socket is an endpoint of a bidirectional \
inter-process communication flow across an Internet Protocol-based computer network, such as \
the Internet." # the socket is the abstraction, it replaces the filehandler

TCP Port Numbers
- A port is an application-specific or process-specific software communications endpoint
- It allows multiple networked applications to coexist on the same server
- There is a list of well-known TCP port numbers

# Domain name == IP address
# Port == functions of server (e.g. login / incoming email / web server, etc.)

Common TCP Ports 
+ Telnet (23) - Login
+ SSH (22) - Secure Login
+ HTTP (80) # one we will use most in this class
+ HTTPS (443) - Secure
+ SMTP (25) - Mail
+ IMAP (143/220/993) - Mail Retrieval
+ POP (109/110) - Mail Retrieval
+ DNS (53) - Domain Name
+ FTP (21) - File Transfer

- Sometimes we see the port number in the URL if the web server is running a 'non-standard' port. # http://localhost:8085/sites.html

Sockets in Python
- Python has built-in support for TCP Sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this opens the 'portal' to the outside world; but nothing is connected yet
# socket.socket --> library.method_within_library "open me a socket"
# socket.AF_INET --> make an internet socket
# socket.SOCK_STREAM --> it's a stream socket (just giving and receiving data)
mysock.connect( ('www.py4inf.com', 80) ) # host / port; now we connect the socket to a host (www.py4inf.com) and port 80
# There has to be software running on the server which waits for you to show up, you can't connect to just anything

[From Sockets to Applications]

Application Protocol
- Since TCP (and Python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
- Application Protocols
  + Mail
  + World Wide Web

HTTP - Hypertext Transport Protocol

"The HyperText Transport Protocol is the set of rules to allow browsers to retrieve web documents from servers over the Internet"

- The dominant Application Layer Protocol on the Internet
- Invented for the Web - to Retrieve HTML, Images, Documents, etc.
- Extended to be data in addition to documents - RSS, Web Services (such as API), etc..
- Basic Concept - Make a Connection - Request a Document - Retrieve the Document - Close the Connection

What is a Protocol?

- A set of rules that all parties follow for so we can predict each others behavior
- And not to bump into each other
  + On two-way roads in USA, drive on the right-hand side of the read
  + On two-way roads in the UK, drive on the left-hand side of the road
- Who talks first? # E.g. if both are waiting for the other nothing happens..

URL - Uniform Resource Locator
- http://www.dr-chuck.com/page1.htm
  + http:// == protocol
  + www.dr-chuck.com == host
  + /page1.htm == document

Getting Data From The Server # the act of surfing the web

- Each time the user clicks on an anchor tag with an href= value to switch to a new page, 
the browser makes a connection to the web server and issues a "GET" request - to GET the content
of the page at the specified URL.
- The server returns the HTML document to the browser, which formats and displays the document to the user
- This is called the request/response cycle # browser: get --> retrieve --> display

Internet Standards
- The standards for all of the Internet protocols (inner workings) are developed by an organization
- Internet Egineering Task Force (IETF) # www.ietf.org
- Standards are called 'RFCs' # Request for Comments --> never is so set in stone that we can never imagine not changing them

Making an HTTP request
- Connect to the server like www.dr-chuck.com
  + a "hand shake"
- Request a document (or the default document)
  + GET http://www.dr-chuck.com/page1.htm
  + GET http://www.facebook.com

telnet # old command to log-in to other computers; can be used to hand-talk the protocal

In the command line (CL):
$ telnet www.dr-chuck.com 80 # opens a websocket and uses port 80 (webbrowsers)
$ GET http://www.dr-chuck.com/page1.htm HTTP/1.0 # feed this and enter twice

# Ultimately opening a browser involves many GET requests; HTML doc, CSS doc, images, etc.

[Lets Write a Web Browser]

An HTTP Request in Python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET http://www.py4inf.com/code/romea.txt HTTP/1.0\n\n') # since we initiate the connection, we talk first --> following the HTTP protocal (port 80)
# GET - the GET request
# Document URL - http://www.py4inf.com/code/romea.txt
# Protocal we want to use - HTTP/1.0
# Enter twice - \n\n (two newline characters)

while True:
	data = mysock.recv(512) # receive up to 512 characters at a time
	if (len(data) < 1): # there is a special mark that says "this is the end of the file", if there is no data ANYMORE -1 is returned, so the loop will break
		break
	print data # since it finished and returned -1, the loop is broken, and now it will continue to print it
mysock.close()

!! When .send is completed -1 is returned !!

Making HTTP Easier With urllib

- Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file.

- socket --> low-level library, make a phone call, you choose how to talk
- urllib --> application level library, that knows about GET and all other things (rules)
  + urllib makes URLs seem like files 

import urllib
fhand = urllib.urlopen('http://ww.py4inf.com/code/romea.txt')

for line in fhand:
	print line.strip()

- With urllib you do not get the headers/metadata; only the file itself

# TIP: don't name your files as libraries

Like a file...

import urllib
fhand = urllib.urlopen('http://ww.py4inf.com/code/romea.txt')

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print counts

-- Week 4

== Programs that Surf the Web ==

[Understanding HTML]

Reading Web Pages

import urllib
fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
	print line.strip()

#=> <h1>The First Page</h1>
#=> <p>
#=> If you like, you can switch to the <a
#=> href="http://www.dr-chuck.com
#=> /page2.htm">Second Page </a>.
#=> </p>

- The idea is that you grep all the URLs and feed those again into the fhand.
- This is the idea behind a crawler.

Parsing HTML (a.k.a. Web Scraping)

What is Web Scraping?
- When a program or script pretends to be a browser and retrieves web pages,
  looks at those web pages, extracts information, and then looks at more 
  web pages.
- Search engines scrape web pages - we call this "spidering the web" or
  "web crawling".

Why Scrape?
- Pull data - particularly social data - who links to who?
- Get your own data back out of some system that has no "export capability".
- Monitor a site for new information.
- Spider the web to make a database for a search engine.

Parsing HTML with BeautifulSoup

The Easy Way - Beautiful Soup
- You could do string searches the hard way
- Or use the free software called BeautifulSoup from www.crummy.com

Place the BeautifulSoup.py file in the same folder as your Python code...

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read() # read method --> read it all in one line, with newlines intact, etc.
soup = BeautifulSoup(html) # returns a soup object, which is a parsed form of the html document (no you can ask questions to it)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
# For instance: key: href, value: www.example.com
# <a> could have more attributes than href, e.g. size etc. Those would be new keys.

tags = soup('a') # return all a anchors: <a> 

for tag in tags:
	print tag.get('href', None) # Each tag is a library (attributes/values).
	# href is a key. Give all the values of key href. If no href present return None.

Summary

- The TCP/IP gives us pipes/sockets between applications
- We designed application protocols to make use of these pipes
- HyperText Transport Protocol (HTTP) is a simple yet powerful protocol
- Python has good support for sockets, HTTP, and HTML parsing

-- Week 5

== Web Services and XML == 

[Web Services Overview]

Data on the Web
- With the HTTP Request/Response well understood and well supported,
  there was a natural move towards exchanging data between programs using 
  these protocols
- We needed to come up with an agreed way to represent data going between
  applications and across networks
- There are two commonly used formats: XML and JSON

Sending Data across the Net
- "Wire Protocol" - What we send on the 'wire' # either JSON or XML
  + Serialize: taking internal structure and creating the wire format
  + Deserialize: taking wire format and creating the internal structure

[eXtensible Markup Language - XML]

- Primary purpose is to help information systems share structured data
- It started as a simplified subset of the Standard Generalized Markup
  Language (SGML), and is designed to be relatively human-legible

- Simple element: a tag that includes something
- Complex element: tag that includes other tags

XML Basics

<person> 				# Start Tag
 <name>Chuck</name>	
 <phone type="intl">    # type="intl" == Attribute
  +1 734 303 4456		# Text Content
 </phone> 				# End Tag
 <email hide="yes" />   # Self-Closing Tag / hide="yes" == Attribute
</person>	            # End Tag

- Tags indicate the beginning and ending of elements.
- Attributes are key/value pairs on the opening tag of XML.
- White Space: Line ends do not matter. White space is generally discarded on text elements.
  We indent only to be readable.

<a>
 <b>X</b>
 <c>
  <d>Y</d>
  <e>Z</e>
 </c>
</a>

/a/b = X
/a/c/d = Y
/a/c/e = Z

[XML Schema]

- Description of the legal format of an XML document
- Expressed in terms of constraints on the structure and content of documents
- Often used to specify a 'contract' between systems.
  + "My system will only accept XML that conforms to this particular schema."
- If a particular piece of XML meets the specification of the Schema - it is said to 'validate'.

XML Document

<person>
 <lastname>Severance</lastname>
 <age>17</age>
 <dateborn>2001-04-17</dateborn>
</person>

XML Schema Contract

<xs:complexType name="person">
 <xs:sequence>
  <xs:element name="lastname" type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="dateborn" type="xs:date"/>
 </xs:sequence>
</xs:complexType>

- Send both Document & Contract to Validator, and check if it validates 
  (if the XML adheres to the contract).

Many XML Schema Languages
- Document Type Definition (DTD)
  + http://en.wikipedia.org/wiki/Document_Type_Definition
- Standard Generalized Markup Language (ISO 8879:1986 SGML)
  + http://en.wikipedia.org/wiki/SGML
- XML Schema from W3C - (XSD) # World Wide Web Consortium = W3C
  + http://en.wikipedia.org/wiki/SML_Schema(W3C)

XSD XML Schema (W3C spec)
- We will focus on the W3C Version
- It is often called "W3C Schema" because "Schema" is considered generic
- More commonly it is called XSD because the file names end in .xsd

XSD Structure
- xs:element
- xs:sequence
- xs:complexType

<xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1" /> # maxOccurs = "unbounded"
<xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10" />

<full_name>Tove Refsnes</full_name>
<child_name>Hege</child_name>
<child_name>Stale</child_name>
<child_name>Borge</child_name>

--> Hence this checks out fine. 

Attribute: type
- string  	# Loek
- date   	# 2015-09-10
- dateTime 	# 2002-05-30T09:30:10Z --> Z == timezone, e.g.: GMT, UTC etc. / YYYY-mm-ddTHH-MM-SS
- decimal	# 99
- integer	# 12.34, also have 'positiveInteger'

<xs:element name="Country">
 <xs:simpleType>
  <xs:restriction base="xs:string">
   <xs:enumeration value="FR" />
   <xs:enumeration value="DE" />
   <xs:enumeration value="ES" />
   <xs:enumeration value="UK" />
   <xs:enumeration value="US" />
  </xs:restriction>
 </xs:simpleType>
</xs:element> 
 
Attribute: use="required" # also optional

[Parsing XML in Python]

import xml.etree.ElementTree as ET

data = '''
<person>
 <name>Chuck</name>
 <phone type="intl">
 +1 734 303 4456
 </phone>
 <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) # act of parsing/deserialisation using the .fromstring method
print 'Name:', tree.find('name').text # find the name tag, find the text (.text)
print 'Attr:', tree.find('email').get('hide') # find the email tag, .get the value for the hide key
#=> Name: Chuck
#=> Attr: yes

import xml.etree.ElementTree as ET
input = '''
<stuff>
 <users>
  <user x="2">
   <id>001</id>
   <name>Chuck</name>
  </user>
  <user x="7">
   <id>009</id>
   <name>Brent</name>
  </user>
 </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # this is the path!
print 'User count:', len(lst)
for item in lst:
	print 'Name', item.find('name').text  #=> Chuck
	print 'Id', item.find('id').text      #=> 001
	print 'Attribute', item.get('x')      #=> 7

Example of an item:

<user x="2">
  <id>001</id>
  <name>Chuck</name>
</user>

-- Week 4

== JSON and the REST Architecture ==

[JSON - Javascript Object Notation]

- JSON can have two structures:
  + a list: called an array --> []
  + a dictionary: called an object --> {}
- JSON represents data as nested 'lists' and 'dictionaries'

Example: JSON object

import json
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email": {
    "hide" : "yes"
  }
}'''

info = json.loads(data) # returns a native dictionary
print 'Name: ', info["name"]
print 'Hide: ', info["email"]["hide"]

# In terminal vi --> view command

Example: JSON array

import json 
input = '''
[
{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
},
{ "id" : "009",
  "x" : "7",
  "name": "Chuck"
}
]'''

info = json.loads(input)
print 'User count: ', len(info)
for item in info:
  print 'Name ', item['name']
  print 'Id', item['id']
  print 'Attribute', item['x']

#=> Name Chuck
#=> Id 2
#=> Attribute 2
#=> Name Chuck
#=> Id 7
#=> Attribute 7

[Service Oriented Approach]

- Most non-trivial web applications use Services
- They use services from other applications 
  + Credit Card Charge
  + Hotel Reservation systems
- Services publish the "rules" applications must follow to make use of the service (API)

Multiple systems
- Initially - two systems cooperate and split the problem
- As the data/service becomes useful, multiple applications want to use the information/application

[Accessing APIs in Python]

Application Program Interface

- The API itself is largely abstract in that it specifies an interface and controls the behavior 
  of the objects specified in that interface. The software that provides the functionality described
  by an API is said to be an implementation of the API. An API is typically defined in terms of the
  programming language used to build an application.

Web Service Technologies

- SOAP: Simple Object Access Protocol (software)
  + Remote programs/code which we use over the network
  + Note: Dr. Chuck does not like SOAP because it is overly complex
- REST: Representational State Transfer (resource focused)
  + Remote resources which we create, read, update and delete remotely

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True: 
  address = raw_input('Enter location: ')
  if len(address) < 1 : break

  url = serviceurl + urllib.urlencode({'sensor' : 'false',
    'address' : address}) # encode this addres value that the user put in in a way that is legal for a url
  print 'Retrieving', url
  uh = urllib.urlopen(url)
  data = uh.read()
  print 'Retrieved', len(data), 'characters'

  try: js = json.loads(str(data))
  except: js = None
  if 'status' not in js or js['status'] != 'OK': # check array -not in- and  object -js['status']
    print '=== Failure to Retrieve ==='
    print data
    continue

  print json.dumps(js, indent = 4) # dumps --> dump in a string, "print it pretty"

  lat = js["results"][0]["geometry"]["location"]["lat"]
  lng = js["results"][0]["geometry"]["location"]["lng"]
  location = js['results'][0]['formatted_address']
  print location


The JSON Object that is returned in the example:

{
  "status" : "OK",
  "results" : [
  {
    "geometry" : {
      "location_type": "APPROXIMATE",
      "location" : {
        "lat" : 42.2808256,
        "lng" : -83.7430378
      }
    },
    "address_components" : [
      {
      "long_name": "Ann Arbor",
      "types" : [
        "locality", 
        "political"
        ],
      "short_name" : "Ann Arbor"
      }
    ],
    "formatted_address" : "Ann Arbor, MI, USA",
    "types": [
      "locality",
      "political"
      ]
    }
  ]
}

[API Security and Rate Limiting]

- The compute resources to run these APIs are not 'free'
- The data provided by these APIs is usually valuable
- The data providers might limit the number of requests per day,
  demand an API 'key', or even charge for usage
- They might change the rules as things progress..

Using the Twitter API

hidden.py

def oauth():
  return {
  "consumer_key" : "h7lu....Ng",
  "consumer_secret" : "dNKenAC3New...mmn7Q",
  "token_key" : "10185562-ein2...P4GEQQOSGI",
  "token_secret" "H0ycCFemmwyf1...qoIpBO"
  }

--

twurl.py 

import urllib
import oauth
import hidden

def augment(url, parameters): # parameters = dictionary
  secrets = hidden.oauth()
  consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
  token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
  oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token = token, http_method = 'GET', http_url = url, parameters = parameters)
  oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
  return oauth_request.to_url()

-- twitter.py

import urllib
from twurl import augment

print '* Calling Twitter... *'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name' : 'drchuck', 'count': 2} ) # show me the user's timeline, for user (screen_name) drchuck and show me the first 2
print url
connection = urllib.urlopen(url)
data = connection.read() # gets the body 
print data # will be JSON data
headers = connection.info().dict # gets a dictionary with only the headers
print headers

# python -mjson.tool < json_ugly_file

-- twitter2.py

import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True: 
  print ''
  acct = raw_input('Enter Twitter Account:')
  if (len(acct) < 1) : break
  url = twurl.augment(TWITTER_URL, {'screen_name' : acct, 'count' : '5'})
  print 'Retrieving', url
  connection = urllib.urlopen(url)
  data = connection.read() # this is the JSON data
  headers = connection.info().dict # headers are the result of the connection via urllib, not JSON! It's like the JSON's metadata
  print 'Remaining' headers['x-rate-limit-remaining']
  js = json.loads(data)
  print json.dumps(js, indent = 4) # pretty printing
  for u in js['users'] : 
    print u['screen_name']
    s = u['status']['text']
    print ' ',s[:50]

Summary
- Service Oriented Architecture - allows an application to be broken into parts and distributed across a network. 
- An Application Program Interface (API) is a contract for interaction.
- Web Services provide an infrastructure for applications cooperating (an API) over a network - SOAP and REST are two
  styles of web services. 
- XML and JSON are serialization formats.