# Nicholas Reitano's Assessment for SIL International

# BibTeX Parser (Task 2)
## Installation

##### Unzip folder and navigate to the root folder named, 2.BibTexParser.

##### Create a virtual environment in the root directory to house the dependencies required for this program.

````bash
$ python -m venv venv
````

##### Activate the virtual environment that was just created (may be different syntax for Windows vs. Linux-based Operating Systems)

Windows:
````bash
$ venv\Scripts\activate.bat

````
Linux-based (including MacOS): 
````bash
$ source venv/bin/activate
```` 

##### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required python packages.

```bash
$ pip install -r requirements.txt
```

## Important!
### Unzip the large BibTeX file located in the "gotolog_source.zip" folder and place the .bib file in the root directory.

## Usage

```bash
$ python myBibTexParser.py -inFile=<name of your .bib file> -outFile=<name of your .csv file>
```
#### Example Usage: 
```bash
$ python myBibTexParser.py -inFile=gotolog_source.bib -outFile=out.csv
```

## Usage Notes
For large files, such as the gotolog_source.bib file, please allow up to 2 minutes for this program to execute. 

## Build Philosophy

#### Choosing a BibTeX Parser for Python
I experimented using a few different BibTeX parsers for python. I found a [StackOverflow Article](https://stackoverflow.com/questions/30768745/is-there-a-reliable-python-library-for-taking-a-bibtex-entry-and-outputting-it-i) highlighting a few different parsers. 

First, I tried, Bibtexparser which worked well for small files, but larger files took too long to run. 

Next, I tried pybtex which was a bit finicky to get working; however, it runs the large file in under 2 minutes which is why I ended up using this module. 

Finally, I experimented with biblib which worked okay; however, this had a longer runtime than pybtex. Also, since it is not a pip module, it would have required additional installation steps. 

#### Encoding Unique Characters
I ran into an interesting case where I needed to specify the encoding to use UTF-32 instead of the default UTF-8. This was due to the vast number of unique characters used in the many different and unique languages in the gotolog_source.bib file. 
 
