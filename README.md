# Scrape It 'Til You Make It: Data Scraping 101

For supplementary information explaining the premise of data scraping, go [here](https://docs.google.com/presentation/d/1GiMOLlGX-JwUoZPmiYU9fEpFDB5QRR0kyxV892f2ha4/edit?usp=sharing)!

In this tutorial, we will be scraping data from a website to populate our own webpage!

## Repo Structure

```
/* The example webpage */
example/
  animation.gif
  index.html

/* This is the webpage that will visualize the data you pull */
ui/
  index.html

/* This is where your data will live. */
data/
  data.json

/* This is where you will implement the code for this tutorial. Good luck! :) */
scrape.py
```

## HTML Review
This is a quick review of HTML or Hypertext Markup Language. HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.

### HTML Tags

#### Doctype
```html
<!-- This tag is mostly for compliance. It tells the web browser that the website is being rendered in HTML 5.  -->
<!DOCTYPE html>
<!-- We could have done the following below. This is the DOCTYPE for HTML 4.1 Strict.  -->
<!-- <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"> -->
```

#### HTML
```html
<!-- This is the root tag. It encapsulates all html content.   -->
<html>
...
<!-- Tags in HTML have an associated "/" tag that ends the tag's enclosure. -->
</html>
```

#### Body
```html
<!-- All the rendered content is found in the body tag. -->
<body>
  ...
</body>
```

#### Headings
```html
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
...
<h6>This is heading 6</h6>
```
##### Paragraphs
```html
<p> Most longer text passages are written here</p>
```

### Media Content: Images, GIFs, and Videos
```html
<!-- You can render images, GIFs, and MP4 videos using this tag. -->
<img src="animation.gif">
```

## JSON
JSON or JavaScript Object Notation is an open-standard file format that uses human-readable text to transmit data objects consisting of attribute–value pairs and array data types.

It's basically a string formatted Python dictionary.

### JSON Example
```
{
	"employee": {
	    "name": "Richard Smith",
	    "age": 23
    }
}
```

There is a python package also called `json` that we can use to parse the object.

### .dumps
Converts python object to JSON string
```
json.dumps({'employee': {"name": 'Richard Smith', 'age': 23})
>>> '{"employee": {"name": "Richard Smith", "age": 23}}'
```

### .loads
Converts JSON to a Python object
```
json.loads('{"employee": {"name": "Richard Smith", "age": 23}}')
>>> {"employee": {'name': 'Richard Smith', 'age': 23}
```


## Beautiful Soup
Beautiful Soup is a Python library for pulling data out of HTML and XML files.

### Startup Instructions

#### 1. Installing
Run this command in terminal to install the package
```
pip install bs4
```

#### 2. Importing
Add the following lines to the top of scrape.api
```
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("wonderland.html"), 'html.parser')

```
The first line imports the Beautiful Soup framework. The second line create an html parsing object with the html file.

#### 3. Useful Methods
Beautiful Soup converts HTML tags to objects.

##### Tag
Gets the tag with the name as the variable
```
soup.title
<title>Wikipedia</title>

# or

soup.p
<p class="title"><b>The Dormouse's story</b></p>
```

##### Name
Gets the name of the tag specified
```
soup.title.name
# u'title'
```
##### String
Gets the string contained within the tag specified
```
soup.title.string
u'The Dormouse's story'
```
##### Parent
Returns the parent of the tag specified
```
soup.title.parent
u'head'
```
##### Class
Gets the class of the tag specified
```
soup.p['class']
#u'title'
```

##### All text
This function returns all the text inside the html page
```
soup.get_text()
```

##### Find all
This function returns takes in a tag parameter and returns all instances of that tag in the html
```
soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
 ```

##### Loping through
This is an example of looping through all a tags and prints the link contained inside its href attribute
```
for link in soup.find_all('a'):
    print(link.get('href'))

http://example.com/elsie
http://example.com/lacie
```

## Application
Now for the fun bit! We have given you the tools to succeed, it is time to apply it. :)

### Task
Extract all amusement parks, films, and albums involving Wonderland from the wikipedia page.


Once you have written this data to a file using the correct format (given below), we can now visualize it using a webpage we created which reads the JSON in `data/data.json`.

```json
[
  {
    "name": "Thing 1",
    "type": "amusement park",
    "img":  "http://wiki.org/.../image_1.png"
  },
  {
    "name": "Thing 2",
    "type": "film",
    "img":  "http://wiki.org/.../image_2.png"
  },

  ...

  {
    "name": "Thing X",
    "type": "album",
    "img":  "http://wiki.org/.../image_X.png"
  }
]
```

## Test it out!
```
python -m http.server 8000
```
