-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Car_Sales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Car_Sales` (
  `year` YEAR(4) NOT NULL,
  `make` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `trim` VARCHAR(45) NULL,
  `body` VARCHAR(45) NULL,
  `transmission` VARCHAR(45) NULL,
  `vin` VARCHAR(45) NOT NULL,
  `state` CHAR(2) NULL,
  `condition` INT NULL,
  `odometer` INT NULL,
  `color` VARCHAR(45) NULL,
  `interior` VARCHAR(45) NULL,
  `seller` VARCHAR(45) NULL,
  `mmr` BIGINT(250) NULL,
  `sellingprice` VARCHAR(45) NULL,
  `saledate` VARCHAR(150) NULL,
  PRIMARY KEY (`vin`))
ENGINE = InnoDB;

USE `mydb`;

DELIMITER $$
USE `mydb`$$
CREATE DEFINER = CURRENT_USER TRIGGER `mydb`.`Car_Sales_BEFORE_INSERT` BEFORE INSERT ON `Car_Sales` FOR EACH ROW
BEGIN

END
$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
