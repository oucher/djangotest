CREATE TABLE IF NOT EXISTS `mydb`.`user_info` (
  `userid` INT NOT NULL,
  `username` VARCHAR(45) NULL,
  `userpass` VARCHAR(200) NULL,
  PRIMARY KEY (`userid`))
ENGINE = InnoDB
