from flask import Flask, request
from llm import index_dir, index_file, query, delete_index

app = Flask(__name__)

@app.route('/indexing', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
def indexing():
    if (request.method == 'GET'):
        return "Indexing is in progress"

    if (request.method == 'POST'):
        path = request.json['path']

        indexed_count = index_dir(path)

        return str(indexed_count) + ' new files were (re)indexed.'

    if (request.method == 'PATCH'):
        path = request.json['path']

        indexed_count = index_file(path)

        if (indexed_count == 0):
            return 'No update was needed for ' + path + '.'

        return path + ' got updated index.'

    if (request.method == 'DELETE'):
        file_path = request.json['path']
        # delete the file from the index store
        delete_index(file_path)

        return file_path + ' deleted from document store and index'

@app.route('/', methods = ['POST'])
def index():
    if (request.method == 'POST'):
      user_query = request.json['query']

      response = query(user_query)

      return response
