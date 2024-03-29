# Inventory

Inventory is a backend service for persisting real estate listings.

## Installation

This project uses Docker for easy setup and isolation. You can work on this project using either VSCode or PyCharm, but the instructions below are for VSCode.

### Prerequisites

1. VSCode
2. `Docker` and `Dev Containers` VSCode Extensions
3. Docker

### Running the Service

1. Open the project in VSCode.
2. Run the command `docker-compose up --build -d` in the terminal to build and start the Docker container.
3. Use the command `Attach to running container` to connect your IDE to the running Docker container.

### Installing Additional Extensions

You might want to install some more extensions in the IDE attached to the container like `Python`.
As long as you don't manually delete the docker images created from this project, you won't have to perform this step again.

### Stopping the Service

1. Run the command `docker-compose down` in the terminal

In the current setup, DynamoDB does not use any docker volume for persisting data, therefore when the container is deleted after bringing down the deployment, any data persisted so far gets lost.

### Initializing the DynamoDB Table

DynamoDB is initialized automatically from the `start.sh` script.

## API Endpoints

Document your API endpoints here.
After a succesful set up, you would be able to access the list of the available APIs
http://localhost:7200/docs#/

Also, for integrating with the LLM service, the Open API spec is published here 
http://localhost:7200/openapi.json

Currently only create and fetch operations are supported.

## Testing
Sonar Cube executes the tests and test the code coverage automatically whenever develop branch is invoked.

Additionally you can manually Run the tests from the `/code` path, by executing:
`pytest`

And produce the code coverage report:
1. `coverage run -m pytest`
2. `coverage report -m`

##  Model

Only a handfull of property attributes like number of bedrooms, bathrooms and location are included in the initial model.