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