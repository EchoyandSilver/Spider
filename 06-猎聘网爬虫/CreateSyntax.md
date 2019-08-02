### Mysql ###
* create syntax:

	```
	CREATE TABLE `joblist` (
	  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `title` varchar(255) DEFAULT NULL,
	  `release_time` varchar(255) DEFAULT NULL,
	  `area` varchar(255) DEFAULT NULL,
	  `company` varchar(255) DEFAULT NULL,
	  `edu` varchar(255) DEFAULT NULL,
	  `worktime` varchar(255) DEFAULT NULL,
	  `descContent` varchar(1000) DEFAULT NULL,
	  `salary` varchar(255) DEFAULT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB AUTO_INCREMENT=661 DEFAULT CHARSET=utf8;
	```
