Scopus Search API Client
========================

Connect to the Scopus Search APIs (http://searchapidocs.scopus.com/)

The scopus\_author\_profiles file contains methods that wrap API calls to retrieve:
- single author profiles
- multiple author profiles associated to a given affiliation
- all documents associated to an author profile

Please insert a valid API key in scopus_api.py in order to use this library.

Check scopus_author_profiles.py for a few examples of how to use the library to retrieve information programmatically.

## Using the command line interface

Install required libraries:

```
pip install -r requirements.txt
```

Run CLI help for available commands:

```
./scopus_api_cli.py --help
```