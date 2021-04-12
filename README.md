A location-based API with GET and POST call methods to post a message and retrieve posts in a defined range in km.

** Call api.py to start the service

Examples:

GET http://localhost:5000?latitude=-21.2069354&longitude=-47.796838&distance=0.8

POST http://localhost:5000/
{"latitude":43.4303489,"longitude":-80.6163987,"nick":"NEW_POST_USER","post":"NEW_POST_MESSAGE"}
