### Mysql ###
* create syntax:

	```
	CREATE TABLE `zufang` (
	  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `title` varchar(255) DEFAULT NULL,
	  `city` varchar(255) DEFAULT NULL,
	  `region` varchar(255) DEFAULT NULL,
	  `price` varchar(255) DEFAULT NULL,
	  `house_type` varchar(255) DEFAULT NULL,
	  `orientation` varchar(255) DEFAULT NULL,
	  `full_area` varchar(255) DEFAULT NULL,
	  `base_info` varchar(255) DEFAULT NULL,
	  `peitao` varchar(255) DEFAULT NULL,
	  `house_information` text,
	  `house_pushtime` varchar(255) DEFAULT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
	```
