-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 11, 2012 at 04:24 AM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

drop database if exists `job-interviews`; 
create database `job-interviews`; 
use `job-interviews`; 

--
-- Database: `xp2`
--

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE IF NOT EXISTS `branch` (
  `Bran_ID` int(3) NOT NULL DEFAULT '0',
  `Bran_Loc` varchar(11) DEFAULT NULL,
  `Bran_Country` varchar(13) DEFAULT NULL,
  `Year_Bran_Started` int(4) DEFAULT NULL,
  PRIMARY KEY (`Bran_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`Bran_ID`, `Bran_Loc`, `Bran_Country`, `Year_Bran_Started`) VALUES
(12, 'Atlanta, GA', 'United States', 1972),
(218, 'Austin, TX', 'United States', 1997),
(104, 'Miami, FL', 'United States', 1986),
(313, 'Beijing', 'China', 2007),
(314, 'Beijing', 'China', 2007),
(14, 'Atlanta, GA', 'United States', 1973);

-- --------------------------------------------------------

--
-- Table structure for table `candidate`
--

CREATE TABLE IF NOT EXISTS `candidate` (
  `Cand_ID` int(4) NOT NULL DEFAULT '0',
  `Cand_Name` varchar(12) DEFAULT NULL,
  `Cand_ Phone` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`Cand_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `candidate`
--

INSERT INTO `candidate` (`Cand_ID`, `Cand_Name`, `Cand_ Phone`) VALUES
(3219, 'Miles, D.', '404-894- 1117'),
(3318, 'Phillips, H.', '706-549- 2828'),
(3492, 'Robert, T.', '404-808- 1212'),
(3281, 'Norton, B.', '404-202- 0101'),
(3251, 'Shi, S.', '412-236- 3708'),
(3293, 'Bai, N.', '86-10-42877142'),
(3462, 'Grant, H.', '404-212- 3636'),
(3212, 'Bryant, K.', '404-396-6313'),
(3313, 'James, L.', '404-936-3616');

-- --------------------------------------------------------

--
-- Table structure for table `interview`
--

CREATE TABLE IF NOT EXISTS `interview` (
  `Interview_ID` int(2) NOT NULL DEFAULT '0',
  `Cand_ID` int(4) DEFAULT NULL,
  `Bran_ID` int(3) DEFAULT NULL,
  `Interview_Date` date DEFAULT NULL,
  `Interview_Round` varchar(6) DEFAULT NULL,
  `Interview_Result` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`Interview_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `interview`
--

INSERT INTO `interview` (`Interview_ID`, `Cand_ID`, `Bran_ID`, `Interview_Date`, `Interview_Round`, `Interview_Result`) VALUES
(1, 3219, 12, '2011-01-15', 'First', 'Pass'),
(2, 3219, 12, '2011-01-20', 'Second', 'Pass'),
(3, 3219, 12, '2011-01-30', 'Third', 'Pass'),
(4, 3318, 218, '2011-02-25', 'First', 'Pass'),
(5, 3318, 218, '2011-02-28', 'Second', 'Fail'),
(6, 3492, 12, '2011-03-21', 'First', 'Pass'),
(7, 3281, 104, '2011-02-12', 'First', 'Fail'),
(8, 3251, 313, '2011-01-24', 'First', 'Fail'),
(9, 3251, 314, '2011-02-05', 'First', 'Pass'),
(10, 3293, 314, '2011-02-12', 'First', 'Fail'),
(11, 3462, 14, '2011-03-17', 'First', 'Pass'),
(12, 3212, 12, '2011-01-16', 'First', 'Pass'),
(13, 3212, 12, '2011-02-21', 'Second', 'Fail'),
(14, 3212, 313, '2011-03-23', 'First', 'Fail'),
(15, 3313, 14, '2011-01-17', 'First', 'Pass'),
(16, 3313, 14, '2011-03-01', 'Second', 'Pass');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
