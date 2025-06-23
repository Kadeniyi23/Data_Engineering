-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Brazilian_Supermarket_Sales
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Brazilian_Supermarket_Sales
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Brazilian_Supermarket_Sales` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;


USE `Brazilian_Supermarket_Sales` ;


-- CUSTOMER TABLE
CREATE TABLE IF NOT EXISTS `CUSTOMER`(
  `customer_id` VARCHAR(50) NOT NULL,
  `state` CHAR(2),
  `zip_code` VARCHAR(100),
  `city` VARCHAR(50),
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB;

-- PRODUCT TABLE
CREATE TABLE IF NOT EXISTS `PRODUCT`(
  `product_id` VARCHAR(50) NOT NULL,
  `product_category_name` VARCHAR(255) NOT NULL,
  `product_weight_g` INT,
  `product_length_cm` INT,
  `product_height_cm` INT,
  `product_width_cm` INT,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB;

-- ORDER TABLE
 n


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
