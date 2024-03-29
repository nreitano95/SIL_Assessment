# Nicholas Reitano's Assessment for SIL International

# API Endpoint (Optional Task 2b)

## API Endpoint Location (once server is running)
````html
http://localhost:8545/post-data
````

## Overview
This is a REST API endpoint that receives a JSON POST request containing an author, a title, or both.<br>
<br>
The API then returns all related entries from the [gotolog dataset](https://cdstar.shh.mpg.de/bitstreams/EAEA0-9478-C22F-4AAF-0/glottolog_source.bib.zip) in JSON format.<br> 
<br>
This API endpoint is served via a Python Flask microframework.<br>
<br> 
The .CSV file used for this was generated using a modified version of the "myBibTexParser.py" program from part 2.<br><br>
The modified version of the BibTeX parser included an additional column for the author which then outputted a .CSV file with all of the entries from the .bib file.<br> 
<br>
The .CSV file for this API endpoint has 5 columns: ID, Title, Subject Language, Year, Author.

## Requirements
##### Must be running Python 3.2 or newer.

## Installation

##### In the unzipped and extracted folder, navigate to the root folder named, "endpoint-flask-project" located in the "2b.APIEndpoint" folder (**2b.APIEndpoint/endpoint-flask-project**).

### Important!
##### Unzip the large .CSV file located in the "dataForPart2B.zip" folder and place the .CSV file in the root directory ("endpoint-flask-project"). 

##### Create a virtual environment in the root directory to house the dependencies required for this program.

````bash
python -m venv venv
````

##### Activate the virtual environment that was just created (may be different syntax for Windows vs. Linux-based Operating Systems)

Windows:
````bash
venv\Scripts\activate.bat

````
Linux-based (including MacOS): 
````bash
source venv/bin/activate
````

##### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required python packages.

```bash
pip install -r requirements.txt
```
## Usage and Example POST requests

#### Bash Usage Instructions
###### Starts Flask Server 
```bash
python app.py
```

#### JSON POST Request Format

###### JSON can contain either author, title, or both.

````json
{
 "author": "Kretzenbacher", 
  "title": "Rekapitulation"
}
````

## Example POST Requests
###### Can be entered in another bash shell once the server is running.

##### Author Only
````bash 
curl -X POST -H "Content-type: application/json" -d "{\"author\" : \"Kretzenbacher\"}" "localhost:8545/post-data"
````

###### Output
````json
{"id":411697,"title":"National variation of address in pluricentric languages: The examples of Swedish and German","subject_lang":"Swedish [swe] (computerized assignment from \"swedish\")","year":"2013","author":"[Person('Norrby, Catrin'), Person('Kretzenbacher, Heinz L.')]"}
{"id":446154,"title":"Book review","subject_lang":"Null","year":"2014","author":"[Person('Kretzenbacher, Heinz L.')]"}
{"id":442225,"title":"Florian Coulmas (ed.). 2007. Language Regimes in Transformation. Future Prospects for German and Japanese in Science, Economy, and Politics (Contributions to the Sociology of Language 93). Berlin, New York: Mouton de Gruyter. xi, 216 p","subject_lang":"Japanese [jpn] (computerized assignment from \"not among and not eastern and japanese\")","year":"2010","author":"[Person('Kretzenbacher, Heinz L.')]"}
{"id":414796,"title":"Rekapitulation. Analyse Einer Textsorte Der Wissenschaftlichen Fachsprache","subject_lang":"Null","year":"1991","author":"[Person('Kretzenbacher, Heinz Leonhard')]"}
{"id":401984,"title":"Mind your metaphors! Historical and theoretical notes toward a constructivist theory of metaphor in scientific communication","subject_lang":"Null","year":"1997","author":"[Person('Kretzenbacher, Heinz L.')]"}
````

##### Title Only
````bash 
curl -X POST -H "Content-type: application/json" -d "{\"title\" : \"Rekapitulation\" }" "localhost:8545/post-data"
````

###### Output
````json
{"id":414796,"title":"Rekapitulation. Analyse Einer Textsorte Der Wissenschaftlichen Fachsprache","subject_lang":"Null","year":"1991","author":"[Person('Kretzenbacher, Heinz Leonhard')]"}
````

##### Author and Title
````bash 
curl -X POST -H "Content-type: application/json" -d "{\"title\" : \"Rekapitulation\", \"author\" : \"Kretzenbacher\"}" "localhost:8545/post-data"
````
###### Output
````json
{"id":411697,"title":"National variation of address in pluricentric languages: The examples of Swedish and German","subject_lang":"Swedish [swe] (computerized assignment from \"swedish\")","year":"2013","author":"[Person('Norrby, Catrin'), Person('Kretzenbacher, Heinz L.')]"}
{"id":446154,"title":"Book review","subject_lang":"Null","year":"2014","author":"[Person('Kretzenbacher, Heinz L.')]"}
{"id":442225,"title":"Florian Coulmas (ed.). 2007. Language Regimes in Transformation. Future Prospects for German and Japanese in Science, Economy, and Politics (Contributions to the Sociology of Language 93). Berlin, New York: Mouton de Gruyter. xi, 216 p","subject_lang":"Japanese [jpn] (computerized assignment from \"not among and not eastern and japanese\")","year":"2010","author":"[Person('Kretzenbacher, Heinz L.')]"}
{"id":414796,"title":"Rekapitulation. Analyse Einer Textsorte Der Wissenschaftlichen Fachsprache","subject_lang":"Null","year":"1991","author":"[Person('Kretzenbacher, Heinz Leonhard')]"}
{"id":401984,"title":"Mind your metaphors! Historical and theoretical notes toward a constructivist theory of metaphor in scientific communication","subject_lang":"Null","year":"1997","author":"[Person('Kretzenbacher, Heinz L.')]"}
````

#### No Results Example
````bash 
curl -X POST -H "Content-type: application/json" -d "{\"title\" : \"kljadsflkjadsklahdjuthqajkerfldskjfhajkrhtajkdfakldjfad\", \"author\" : \"qwertyqu\"}" "localhost:8545/post-data"
````

###### Output
````json
**** No entries related to requested title or author. ****
````

#### Invalid Input
````bash 
curl -X POST -H "Content-type: application/json" -d "{\"ddadfd\" : \"Cognitive Socio\"}" "localhost:8545/post-data"
````
###### Output
````json
**** Incorrect JSON format used. Please see correct usage. ****
````


 
