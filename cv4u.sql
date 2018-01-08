-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2018 at 11:41 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cv4u`
--

-- --------------------------------------------------------

--
-- Table structure for table `cvinfo`
--

CREATE TABLE `cvinfo` (
  `ID` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `datecol` varchar(255) NOT NULL,
  `personals` varchar(255) DEFAULT NULL,
  `academich` varchar(255) DEFAULT NULL,
  `skills` varchar(255) DEFAULT NULL,
  `carrerhistory` varchar(255) DEFAULT NULL,
  `refe` varchar(255) DEFAULT NULL,
  `image` varchar(255) NOT NULL,
  `socialinks` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cvinfo`
--

INSERT INTO `cvinfo` (`ID`, `username`, `datecol`, `personals`, `academich`, `skills`, `carrerhistory`, `refe`, `image`, `socialinks`) VALUES
(1, 'sagi', '2017-12-11', 'Lorem ipsum', 'Lorem ipsum', 'Lorem ipsum', 'Lorem ipsum', 'Lorem ipsum', '', ''),
(2, 'sagi', '0000-00-00', 'Personal Summary of cv applicative', 'Your education information', 'Web Development', 'Carrer history ..', 'Reference...', '', ''),
(3, 'check', '0000-00-00', 'Personal Summary of cv applicative', 'Your education information', 'Web Development', 'Carrer history ..', 'Reference...', '', ''),
(4, 'check', '1994', 'Personal Summary of cv applicative', 'Your education information', 'Web Development', 'Carrer history ..', 'Reference...', '', ''),
(5, 'check', '2017-12-11', 'Personal Summary of cv applicative', 'Your education information', 'Web Development', 'Carrer history ..', 'Reference...', '', ''),
(6, 'check', '2017-12-11', 'Personal Summary of cv applicative', 'Your education information', 'Web Development', 'Carrer history ..', 'Reference...', 'david.jpeg', ''),
(7, 'check', '2017-12-11', 'Personal Summary of cv applicative', 'Your education information', 'Web Development', 'Carrer history ..', 'Reference...', 'david.jpeg', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `passwordval` varchar(255) DEFAULT NULL,
  `typeid` int(11) DEFAULT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `username`, `passwordval`, `typeid`, `email`) VALUES
(8, 'elior', '7712', 0, 'sagi232123@gmail.com'),
(9, 'david', '1234', 1, 'feew@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cvinfo`
--
ALTER TABLE `cvinfo`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cvinfo`
--
ALTER TABLE `cvinfo`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
