create database linkedin;
use linkedin;
CREATE TABLE `field`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `field` varchar(255) COLLATE utf8_bin NOT NULL,
    `count` int(32),
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1;