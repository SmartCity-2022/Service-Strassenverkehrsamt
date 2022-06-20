CREATE TABLE `vehicle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(45) NOT NULL,
  `model` varchar(45) NOT NULL,
  `firstRegistration` datetime DEFAULT NULL,
  `displacement` float NOT NULL,
  `fuelType` varchar(45) NOT NULL,
  `emissions` float NOT NULL,
  `hudeadline` datetime DEFAULT NULL,
  `licenseplate` varchar(10) NOT NULL,
  `owner` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `registerrequest` (
  `id` int NOT NULL AUTO_INCREMENT,
  `registration1` varchar(500) NOT NULL,
  `registration2` varchar(500) NOT NULL,
  `vehicle` int NOT NULL,
  `huCertificate` varchar(500) NOT NULL,
  `owner` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicle_idx` (`vehicle`),
  CONSTRAINT `vehicle` FOREIGN KEY (`vehicle`) REFERENCES `vehicle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `penalty` (
  `id` int NOT NULL AUTO_INCREMENT,
  `owner` varchar(100) NOT NULL,
  `received` datetime NOT NULL,
  `value` int NOT NULL,
  `reason` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `licenserequest` (
  `id` int NOT NULL AUTO_INCREMENT,
  `citizen` varchar(100) NOT NULL,
  `form` varchar(500) NOT NULL,
  `issued` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `license` (
  `id` int NOT NULL AUTO_INCREMENT,
  `owner` varchar(100) NOT NULL,
  `type` varchar(10) NOT NULL,
  `received` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` float NOT NULL,
  `description` varchar(100) NOT NULL,
  `issued` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `payed` datetime DEFAULT NULL,
  `receiver` varchar(100) NOT NULL,
  `deadline` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

