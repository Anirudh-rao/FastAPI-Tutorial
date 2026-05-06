# Automed Testing In FastAPI

In this section we will be learning about how to write system tests  to validate fastAPI endpoints. Post which will conculude this section by building a CRUD API to manage object lifecycles over HTTP.

## Automated Testing:

* Autometed tests are divided in to two types:

|Unit Tests|System Tests|
|----------|------------|
|Focus:Isolated Code|Focus:Isolated System operations|
|Puspose: Validate Code Function|Purpose:Validate System function|
|Scope:Function or method|Scope: Endpoint|
|Environment: Isolated Python Env|Enviroment:Python env with app running|


## Building a JSON CRUD API.

There are four  stages in an object lifecycle:

1. Create : `POST OPERATION`
2. Read : `GET OPERATION`
3. Update: `PUT OPERATION`
4. Delete : `DELETE OPERATION`

