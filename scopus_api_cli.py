#!/usr/bin/env python2

import click
from scopus_api import *

@click.group()
def cli():
    pass

@click.command('document', help='Retrieve a document')
@click.argument('DOCUMENT_EID')
def document(eid):
    get_document_by_eid(eid)

@click.command('documents', help='Retrieve a set of documents')
@click.argument('AUTHOR_ID')
@click.option('--start-offset', default=0, help='Starting offset')
def documents(author_id, offset):
    get_documents_by_author_id(author_id, offset)

@click.command('author-profile', help='Retrieve an author profile')
@click.argument('AUTHOR_ID')
def author_profile(author_id):
    get_author_profile_by_author_id(author_id)

@click.command('authors-by-affiliation', help='Retrieve a list of authors by affiliation')
@click.argument('AFFILIATION_ID')
def authors_by_affiliation(affiliation_id):
    get_authors_by_affiliation_id(affiliation_id)

@click.command('authors-by-name', help='Retrieve a list of authors by name')
@click.argument('SURNAME')
@click.argument('NAME')
def authors_by_name(surname, name):
    get_authors_by_name(surname, name)

cli.add_command(document)
cli.add_command(documents)
cli.add_command(author_profile)
cli.add_command(authors_by_affiliation)
cli.add_command(authors_by_name)

if __name__ == '__main__':
    cli()