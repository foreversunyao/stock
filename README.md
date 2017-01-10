# stock
This is for collecting of USA stock information every day.
Before run this, you need create two tables in mysql databases.

CREATE DATABASE `db_stock` /*!40100 DEFAULT CHARACTER SET utf8 */

Create Table: CREATE TABLE `tb_americanstockcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(512) DEFAULT NULL,
  `name` varchar(1024) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8

Create Table: CREATE TABLE `tb_stockinfo_day` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stat_date` date DEFAULT NULL,
  `stock_code` varchar(64) DEFAULT NULL,
  `open` decimal(10,6) DEFAULT NULL,
  `high` decimal(10,6) DEFAULT NULL,
  `low` decimal(10,6) DEFAULT NULL,
  `close` decimal(10,6) DEFAULT NULL,
  `volume` bigint(32) DEFAULT NULL,
  `adjclose` decimal(10,6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
