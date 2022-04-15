# Service-Strassenverkehrsamt
## What should the service do?
The service should provide the following functionalities to a citizen:

- Register a new car to the office
- Unregister a car, which was registered by the citizen trying to unregister
- Change registration from one, to another car. Simply, unregister then register to keep license plate
- Get informations about the registered cars of the citizen

## Functions explained quick and dirty

First of, the citizen will need an authorization token delivered by the HUB to use the named functions.

### Registration

To register a new car, the user will have to fill a form with various data of the car like brand, model and year of manufacture.

Data like brand and model will be fetched from an existing database and presented in a kind of combo box.

The user will also have to upload a file, which will be the "HU/AU"-certificate.

After this is done, the request will be send to a clerk.

### Unregistration

If a request is verified, the user will be able to unregister the car by simply press a button.

Maybe it will be a good idea, to add some kind of verification to this step.

### Change registration

As already told, we will simply make a request to delete an entry and create a new one.

Deleting the existing entry should be executed, when new one can be accepted.

### Information about cars

The user will see the following informations:

- Brand
- Model
- Year of manufacture
- Date of registration
- Annual tax rate

The tax rate will be calculated as following:

- For each started 100cm³ of engine displacement, there will be 2€ for a petrol engine and 9.50€ for diesel engines
- For each 25g/CO² there will be a tax of 2€. The first 110g/CO² are taxfree
