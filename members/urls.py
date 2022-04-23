from django.urls import path
#from . import views
from members.views import index,bookDetails,authorDetails,createBook,createAuthor,removeBook,editBook

urlpatterns = [
    path('', index, name='books'),
    path('<int:bookId>/', bookDetails, name='book_list'),
    path('author/<int:authorId>',authorDetails,name="author"),
    path('create', createBook ,name="createBook"),
    path('createAuthor', createAuthor ,name="createAuthor"),
    path('deleteBook/<int:book_id>', removeBook ,name="removeBook"),
    path('editBook/<int:book_id>', editBook ,name="editBook"),
    #path('<int:num>/', views.memberWelcome),
]