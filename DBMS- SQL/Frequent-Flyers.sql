
drop database if exists `frequentflyer`; 
create database `frequentflyer`; 
use `frequentflyer`; 

CREATE TABLE IF NOT EXISTS `flight` (
  `Flight_no` varchar(6) NOT NULL DEFAULT '',
  `Flight_operator` varchar(12) DEFAULT NULL,
  `Flight_Origin` varchar(3) DEFAULT NULL,
  `Flight_Destination` varchar(3) DEFAULT NULL,
  `Miles_per_flight` int(4) DEFAULT NULL,
  PRIMARY KEY (`Flight_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `flight` (`Flight_no`, `Flight_operator`, `Flight_Origin`, `Flight_Destination`, `Miles_per_flight`) VALUES
('US1511', 'US Airways', 'PHX', 'LAX', 370),
('UA6466', 'United', 'LAX', 'SLC', 590),
('CO6357', 'Continental', 'SFO', 'LAX', 337),
('UA1143', 'United', 'PHX', 'PDX', 1008),
('UA6109', 'United', 'PDX', 'SFO', 550),
('CO2923', 'Continental', 'LAX', 'SFO', 554),
('US3221', 'US Airways', 'PHX', 'PDX', 1010),
('UA6456', 'United', 'HOU', 'LAX', 489),
('UA5466', 'United', 'HOU', 'PDX', 658),
('UA1122', 'United', 'SLC', 'HOU', 412);


CREATE TABLE IF NOT EXISTS `flyer` (
  `Frequent_Flyer_ID` int(7) NOT NULL DEFAULT '0',
  `Flyer_Name` varchar(10) DEFAULT NULL,
  `Address` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Frequent_Flyer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `flyer` (`Frequent_Flyer_ID`, `Flyer_Name`, `Address`) VALUES
(3133124, 'Bryant, K.', 'Los Angeles, CA'),
(3509802, 'James, L.', ' Cleveland, OH'),
(3200199, 'Wade, D.', 'Miami, FL'),
(4500891, 'Howard, D.', 'Orlando, FL'),
(2020014, 'Riley, R.', 'Phoenix, AZ'),
(3921239, 'Rose, D.', 'Chicago, IL '),
(4910920, 'Yao, M.', 'Shanghai, China');


CREATE TABLE IF NOT EXISTS `trip` (
  `Trip_reservation_no` int(2) NOT NULL DEFAULT '0',
  `Frequent_Flyer_ID` int(7) DEFAULT NULL,
  `Flight_no` varchar(6) DEFAULT NULL,
  `Flight_date` date DEFAULT NULL,
  `Flight_seating` varchar(5) DEFAULT NULL,
  `Flight_fare` int(4) DEFAULT NULL,
  PRIMARY KEY (`Trip_reservation_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `trip` (`Trip_reservation_no`, `Frequent_Flyer_ID`, `Flight_no`, `Flight_date`, `Flight_seating`, `Flight_fare`) VALUES
(1, 3133124, 'US1511', '2010-02-10', 'Coach', 195),
(2, 3133124, 'UA6466', '2010-02-08', 'Coach', 325),
(3, 3133124, 'CO6357', '2010-01-08', 'First', 300),
(4, 3133124, 'US1511', '2009-12-21', 'Coach', 290),
(5, 3509802, 'US1511', '2010-01-14', 'Coach', 189),
(6, 3509802, 'UA1143', '2009-12-21', 'First', 1096),
(7, 3509802, 'UA6109', '2009-12-21', 'First', 642),
(8, 3200199, 'CO2923', '2010-02-09', 'Coach', 276),
(9, 3200199, 'UA6466', '2010-01-10', 'Coach', 312),
(10, 4500891, 'CO6357', '2010-01-15', 'First', 305),
(11, 2020014, 'UA6109', '2010-01-14', 'Coach', 480),
(12, 2020014, 'US3221', '2010-01-05', 'Coach', 320),
(13, 3921239, 'US1511', '2012-03-02', 'First', 490),
(14, 3921239, 'CO6357', '2011-12-31', 'Coach', 667),
(15, 3921239, 'UA6456', '2010-03-21', 'First', 765),
(16, 4910920, 'US3221', '2012-11-03', 'Coach', 202),
(17, 4910920, 'UA5466', '2011-12-24', 'Coach', 457),
(18, 4910920, 'UA1122', '2011-04-05', 'First', 1003),
(19, 4910920, 'CO2923', '2010-05-23', 'First', 234);


