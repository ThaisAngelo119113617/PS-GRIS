-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema PS_Gris2020
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema PS_Gris2020
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PS_Gris2020` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `PS_Gris2020` ;

-- -----------------------------------------------------
-- Table `PS_Gris2020`.`Candidato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PS_Gris2020`.`Candidato` (
  `idCandidato` INT NOT NULL,
  `Nome` VARCHAR(50) NULL,
  `DRE` INT NULL,
  `Curso` VARCHAR(100) NULL,
  `Email` VARCHAR(150) NULL,
  `Nascimento` DATE NULL,
  `Telegram` VARCHAR(45) NULL,
  `CPF` VARCHAR(50) NULL,
  PRIMARY KEY (`idCandidato`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PS_Gris2020`.`Ouvinte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PS_Gris2020`.`Ouvinte` (
  `idOuvinte` INT NOT NULL,
  `Nome` VARCHAR(45) NULL,
  `CPF` VARCHAR(50) NULL,
  `Email` VARCHAR(100) NULL,
  `Telegram` VARCHAR(45) NULL,
  `É da UFRJ?` TINYINT(1) NULL,
  PRIMARY KEY (`idOuvinte`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PS_Gris2020`.`Palestrante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PS_Gris2020`.`Palestrante` (
  `idPalestrante` INT NOT NULL,
  `Telegram` VARCHAR(45) NULL,
  `Curso/Formação` VARCHAR(100) NULL,
  `Palestra` VARCHAR(45) NULL,
  `Nome` VARCHAR(50) NULL,
  PRIMARY KEY (`idPalestrante`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PS_Gris2020`.`TAGS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PS_Gris2020`.`TAGS` (
  `idTAGS` INT NOT NULL,
  `Data` DATE NULL,
  `Assunto` VARCHAR(45) NULL,
  `idPalestrante` INT NOT NULL,
  PRIMARY KEY (`idTAGS`),
  INDEX `fk_TAGS_Palestrante1_idx` (`idPalestrante` ASC),
  CONSTRAINT `fk_TAGS_Palestrante1`
    FOREIGN KEY (`idPalestrante`)
    REFERENCES `PS_Gris2020`.`Palestrante` (`idPalestrante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PS_Gris2020`.`Avaliação`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PS_Gris2020`.`Avaliação` (
  `idAvaliação` INT NOT NULL,
  `Nota` DECIMAL(10,0) NULL,
  `Candidato_idCandidato` INT NOT NULL,
  `TAGS_idTAGS` INT NOT NULL,
  PRIMARY KEY (`idAvaliação`),
  INDEX `fk_Avaliação_Candidato_idx` (`Candidato_idCandidato` ASC),
  INDEX `fk_Avaliação_TAGS1_idx` (`TAGS_idTAGS` ASC),
  CONSTRAINT `fk_Avaliação_Candidato`
    FOREIGN KEY (`Candidato_idCandidato`)
    REFERENCES `PS_Gris2020`.`Candidato` (`idCandidato`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Avaliação_TAGS1`
    FOREIGN KEY (`TAGS_idTAGS`)
    REFERENCES `PS_Gris2020`.`TAGS` (`idTAGS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
