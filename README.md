# cache-reader


### Description
 
 ```sh

 - This project is about using caching data in a redis database for requests
 - It demostrates how to perfrom CRUD operations in a MongoDB database 
 - The Backend is written is Flask
 - Process of retreiving data from mongodb database everytime can be made comparitvely faster if we can cache the epeated requests 

 ```

 ### How to run the project 

 ```sh
 * git clone https://github.com/DiptoChakrabarty/cache-reader.git
 * cd cache-reader
 * source venv bin activate
 * pip3 install -r requirements.txt
 * python3 app.py 

 ```

 ### Enpoints Present

 ```sh

  - /show  GET

   Shows all data present in the DataBase 

   - /show/<product name> GET

   Shows information about that  product only 

    - /add    POST

    Add a product to the database

    {
        "name": <produc_name>,
        "price": <product_price>
        
    }

 ```