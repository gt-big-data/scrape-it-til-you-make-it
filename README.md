# Scrape It 'Til You Make It
Data Scraping 101
<Link slides>
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
<Example>
## HTML Review

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

### Example
```
{
	"employee": {
	    "name": "Richard Smith",
	    "age": 23
    }
}
```

### .dumps
Convert python object to JSON string
```
json.dumps({'employee': {"name": 'Richard Smith', 'age': 23})
>>> '{"employee": {"name": "Richard Smith", "age": 23}}'
```

### .loads
Convert JSON to a Python object
```
json.loads('{"employee": {"name": "Richard Smith", "age": 23}}')
>>> {"employee": {'name': 'Richard Smith', 'age': 23}
```

## Beautiful Soup

<Where most of tutorial will live - Good luck>
### Instructions

#### 1. Installing 
Run this command in terminal to install the package
```
pip install bs4
```

#### 2. Importing
Add the following lines to the top of scrape.api
```
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```
The first line imports the Beautiful Soup framework. The second line create an html parsing object with the html file.

#### 3. Useful Methods
##### Title
```
soup.title
<title>Wikipedia</title>
```
##### Name
```
soup.title.name
u'title'
```
```
soup.title.string
#u'The Dormouse's story'
```
```
soup.title.parent.name
u'head'
```
```
soup.p
 <p class="title"><b>The Dormouse's story</b></p>
 ```
```
soup.p['class']
#u'title'
```
```
soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
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
```
for link in soup.find_all('a'):
    print(link.get('href'))
http://example.com/elsie
http://example.com/lacie
```

## Test it out!

```
python -m http.server 8000
```
