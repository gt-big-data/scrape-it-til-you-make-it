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
<!-- This is the root tag. It encapsulates alll html content.   -->
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

### .dumps

### .loads

## Beautiful Soup

<Where most of tutorial will live - Good luck>


## Test it out!

```
python -m http.server 8000
```
