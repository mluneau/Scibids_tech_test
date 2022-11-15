import sqlite3


class DatabaseError(Exception):
    pass


def add_headers_sqlite(d, cursor):
    headers = [description[0] for description in cursor.description]
    _data = {headers[index]: value for index, value in enumerate(d)}
    return _data


def get_documents():
    documents = []
    with sqlite3.connect("document.db") as conn:
        try:
            cursor = conn.execute('SELECT * FROM document')
            data = cursor.fetchall()
        except sqlite3.Error as err:
            raise DatabaseError(err.args[0])

        for d in data:
            documents.append(add_headers_sqlite(d, cursor))

    return documents


def get_tags(document_id):
    tags = []
    with sqlite3.connect("document.db") as conn:
        try:
            query = '''
            Select tag.name from document
            left join document_tag on document.id = document_tag.document_id
            join tag on tag.id = document_tag.tag_id
            where document.id = ? ;
            '''
            cursor = conn.execute(query, [document_id])
            data2 = cursor.fetchall()
        except sqlite3.Error as err:
            raise DatabaseError(err.args[0])
        
        for d in data2:
            tags += d

    return tags


