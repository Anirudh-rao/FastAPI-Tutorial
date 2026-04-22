# FastAPI Advanced Topics

## PUT and DELETE Operations

1. PUT operation and Delete operations are used to update and Delete objects.

2. They take in parameters sent via query string as well as request body.


### Refrencing Existing Objects

1. No ORM, so app must map object to ID

2. Database ID - unique identifier.

## Handling Errors

1. User errors: Invalid and outdated URI , missing or incorrect input

2. Server Errors: Something else happended in the server side.

To Communicate FastAPI used HTTP status Codes.
Some advantages of using Status Codes are:

1. Enable API to Provide status in response

2. Specific codes defines in HTTP protocol

3. Range from `100-599`

### Common HTTP status Codes

1. **SUCCESS**(200-299):
   1. `200 OK`
    Default Success response.

   2. `201 Created`
    Specific to POST Operation.

   3. `202 Accepted`
    Noncommittal "Working on it".

   4. `204 No Content`
    Success! Nothing more to say.

   5. `301 Moved Permanently`
    URI changed Permanently.

   6. `400 Bad Request`
    Client Error.

   7. `404 Not Found`
   Server cannot find the requested resource.

   8. `500 Internal Server Error`
   Server has encountered a situation it does not know how to handle.
