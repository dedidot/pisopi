# Documentation

**Github**: `https://github.com/dedidot/pisopi.git`

**Get All data:**
GET: `http://localhost:5000/api/v1/`
Success Response: 

    {
        "data": [
            {
                "amount": 25.3,
                "id": 42,
                "name": "Macee",
                "price": 23,
                "refundable": true,
                "tax": 2.3000000000000003,
                "tax_code": 1,
                "type": "Food"
            },
            {
                "amount": 163,
                "id": 43,
                "name": "Malacca",
                "price": 150,
                "refundable": false,
                "tax": 13,
                "tax_code": 2,
                "type": "Tobacco"
            }
        ],
        "message": "Success",
        "status": true
    }

**Add new**
Post: `http://localhost:5000/api/v1/add`
Post Params:

    {
    	"name": "Malacca",
    	"tax_code": 2,
    	"price": 150
    }

Validation:

    {
        "data": {},
        "message": "Tax code not found",
        "status": false
    }

Success Response:

    {
        "data": {
            "amount": 165,
            "id": 44,
            "name": "Malacca",
            "price": 150,
            "refundable": true,
            "tax": 15,
            "tax_code": 1,
            "type": "Food"
        },
        "message": "",
        "status": true
    }

Dummy Db:

    FLUSH PRIVILEGES ;
    
    CREATE DATABASE github;
    use github;
    
    CREATE TABLE `data` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(100) DEFAULT NULL,
      `tax_code` int(11) DEFAULT NULL,
      `price` int(11) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
    
    INSERT INTO `data` (`id`, `name`, `tax_code`, `price`)
    VALUES
    	(40,'Mac mac',2,8000),
    	(41,'Macee',3,8000),
    	(42,'Macee',1,23);


