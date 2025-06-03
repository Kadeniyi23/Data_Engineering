-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Sales_Data_US
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Sales_Data_US
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Sales_Data_US` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;


USE `Sales_Data_US` ;


-- CUSTOMER TABLE
CREATE TABLE IF NOT EXISTS `CUSTOMER`(
  `customer_id` VARCHAR(50) NOT NULL,
  `customer_first_name` VARCHAR(255) NOT NULL,
  `customer_last_name` VARCHAR(255) NOT NULL,
  `segment` VARCHAR(100),
  `country` VARCHAR(100),
  `city` VARCHAR(100),
  `state` VARCHAR(100),
  `region` VARCHAR(100),
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB;

-- PRODUCT TABLE
CREATE TABLE IF NOT EXISTS `PRODUCT`(
  `product_id` VARCHAR(50) NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `sub_category` VARCHAR(100),
  `category` VARCHAR(100),
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB;

-- ORDER TABLE
CREATE TABLE IF NOT EXISTS `ORDER`(
  `order_id` VARCHAR(50) NOT NULL,
  `order_date` DATE,
  `ship_date` DATE,
  `ship_mode` VARCHAR(100),
  `customer_id` VARCHAR(50),
  `product_id` VARCHAR(50),
  PRIMARY KEY (`order_id`, `product_id`),
  FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
    ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
