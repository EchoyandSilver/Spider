### Mysql ###
* create syntax:

	```
	CREATE TABLE `article` (
	  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
	  `title` varchar(255) DEFAULT '',
	  `author` varchar(255) DEFAULT '',
	  `pub_time` datetime DEFAULT NULL,
	  `content` text,
	  `origin` varchar(255) DEFAULT '',
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB AUTO_INCREMENT=1169 DEFAULT CHARSET=utf8;
	```
