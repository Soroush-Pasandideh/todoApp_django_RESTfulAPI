# todo_backend_django
 this is an implementation of the back-end of a ToDo web app using Django and Django REST Framework and RESTful API.
 
 It connects to sqlLite database to store data.

 endpoints are represented in the API root (localhost:8000/todo/ if you’re using 8000 port).
 
 For security reasons, each endpoint only represents data related to the logged-in user (unless you logged in as an admin user) using permissions.

 this back-end uses JWT (jason web token) for user authentication.

 Users endpoint is represented in auth root (localhost:8000/auth/). If you log in as an admin user, you can access the list of users through this endpoint.

 Admin pannel is available to control data.
