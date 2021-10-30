## RSS Reader
```
Pure command-line rss-reader
```

##Usage
```
usage: rss_reader.py [-h] [--version] [--verbose] [--limit LIMIT] [--json] [--date DATE] [--to_html] [--to_pdf]
                     [source]

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limits news topics if this parameter is provided
  --json         Print result as JSON in stdout
  --date DATE    Print news of provided date in YYYYMMDD format
  --to_html      Convert news to HTML-format
  --to_pdf       Convert news to PDF-format
 ```
## Installation
Install a virtual environment:
Windows 
```
pip install virtualenv
```
Ubuntu
 ```
sudo apt-get install python3-venv
```
Create the env:
Windows
```
python -m venv env
```
Linux
```
/usr/bin/python3 -m venv env
```

Activate environment:
Windows
```
env\Scripts\activate.bat
```
Ubuntu
```
source env/bin/activate
```
Install package:
```
pip install 'Full local path to folder with package'
```

##JSON format
```
[
    {
        "Title": title,
        "Description": description,
        "Source": source,
        "Link": link,
        "Date": date of news,
        "Media": [urls of media content]
    }
]
```
##News caching
```
News saves into json-format file as a dict.
{
    "link_of_rss": [
        {
        "Title": title,
        "Description": description,
        "Source": source,
        "Link": link,
        "Date": date of news,
        "Media": [urls of media content]
    },
        {
        "Title": title,
        "Description": description,
        "Source": source,
        "Link": link,
        "Date": date of news,
        "Media": [urls of media content]
    },
    ...
}
```
##Format converter
```
User can convert data into html-format file:
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<TITLE>
News</TITLE>
</HEAD>
<BODY>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Title</th>
      <td>title</td>
    </tr>
    <tr>
      <th>Description</th>
      <td>description</td>
    </tr>
    <tr>
      <th>Source</th>
      <td>source</td>
    </tr>
    <tr>
      <th>Link</th>
      <td>link</td>
    </tr>
    <tr>
      <th>Date</th>
      <td>date of news</td>
    </tr>
    <tr>
      <th>Media</th>
      <td>[list of media urls]</td>
    </tr>
  </tbody>
</table></BODY>
</HTML>
 User can convert news into pdf-format.
```
##License
Rss-reader is released under the MIT license. See LICENSE.txt for details.
