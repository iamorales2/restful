from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

books = [
  {"id": 1, "title": "Pride and Prejudice", "author": "Jane Austen"},
  {"id": 2, "title": "Moby-Dick", "author": "Herman Melville"},
  {"id": 3, "title": "War and Peace", "author": "Leo Tolstoy"},
  {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
  {"id": 5, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
  {"id": 6, "title": "The Odyssey", "author": "Homer"},
  {"id": 7, "title": "Jane Eyre", "author": "Charlotte Brontë"},
  {"id": 8, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
  {"id": 9, "title": "Wuthering Heights", "author": "Emily Brontë"},
  {"id": 10, "title": "Les Misérables", "author": "Victor Hugo"}
]


# Book Resource
class BookResource(Resource):
    def get(self, book_id=None):
        if book_id:
            book = next((b for b in books if b["id"] == book_id), None)
            return book if book else {"message": "Book not found"}, 404
        return books

    def post(self):
        data = request.get_json()
        new_book = {
            "id": len(books) + 1,
            "title": data["title"],
            "author": data["author"],
        }
        books.append(new_book)
        return new_book, 201

    def put(self, book_id):
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            return {"message": "Book not found"}, 404

        data = request.get_json()
        book.update(data)
        return book

    def delete(self, book_id):
        global books
        books = [b for b in books if b["id"] != book_id]
        return {"message": "Book deleted"}, 200

# API Routes
api.add_resource(BookResource, "/books", "/books/<int:book_id>")

if __name__ == "__main__":
    app.run(debug=True)
