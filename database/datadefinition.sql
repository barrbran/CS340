-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 05, 2021 at 03:39 AM
-- Server version: 10.4.17-MariaDB-log
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_barrbran`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `phoneNumber` varchar(255) NOT NULL,
  `salary` int(11) NOT NULL,
  `nurseID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `fname`, `lname`, `phoneNumber`, `salary`, `nurseID`) VALUES
(1, 'Susan', 'Zoom', '345-099-0493', 150000, 10),
(2, 'Troy', 'Albertson', '345-543-5544', 145000, 9),
(3, 'Buddy', 'Baker', '6723449875', 98765, 9),
(4, 'Jill', 'Biden', '555-555-5555', 5000000, 10);

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `phoneNumber` varchar(255) NOT NULL,
  `salary` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`id`, `fname`, `lname`, `phoneNumber`, `salary`) VALUES
(1, 'Judy', 'Boris', '444-567-9483', 90008),
(2, 'Ron', 'West', '433-343-3532', 50000),
(3, 'Sally', 'Rio', '1234565555', 40000);

-- --------------------------------------------------------

--
-- Table structure for table `nurse`
--

CREATE TABLE `nurse` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `phoneNumber` varchar(255) NOT NULL,
  `salary` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nurse`
--

INSERT INTO `nurse` (`id`, `fname`, `lname`, `phoneNumber`, `salary`) VALUES
(9, 'Gina', 'Peters', '333-454-3455', 55255),
(10, 'Phil', 'Melancon', '9876543210', 65437);

-- --------------------------------------------------------

--
-- Table structure for table `office`
--

CREATE TABLE `office` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phoneNumber` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `zip` int(11) NOT NULL,
  `managerID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `office`
--

INSERT INTO `office` (`id`, `name`, `phoneNumber`, `street`, `city`, `state`, `zip`, `managerID`) VALUES
(1, 'Main Clinic', '445-453-3422', '123 Main Street', 'Corvallis', 'OR', 97330, 1),
(2, 'The Biltmore', '343-444-2345', '444 Tree Drive', 'Corvallis', 'OR', 97331, 1),
(4, 'The Sick Place', '345-324-3452', '444 Nowhere Ave', 'Corvallis', 'OR', 97331, 1),
(5, 'Test Office', '123-456-5555', '34 1st St.', 'Seattle', 'WA', 53212, 2);

-- --------------------------------------------------------

--
-- Table structure for table `officedoctor`
--

CREATE TABLE `officedoctor` (
  `officeID` int(11) NOT NULL,
  `doctorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `officedoctor`
--

INSERT INTO `officedoctor` (`officeID`, `doctorID`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `phoneNumber` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `zip` int(11) NOT NULL,
  `dob` date NOT NULL,
  `weight` int(11) NOT NULL,
  `doctorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `fname`, `lname`, `phoneNumber`, `street`, `city`, `state`, `zip`, `dob`, `weight`, `doctorID`) VALUES
(1, 'Harris', 'Harrison', '455-455-4555', '78 Pine Avenue', 'Corvallis', 'OR', 97330, '2000-12-08', 140, 1),
(2, 'Horace', 'Buxley', '455-567-4433', '899 Illness Rd', 'Corvallis', 'OR', 97330, '2001-04-14', 344, 2),
(3, 'Horace', 'Buxley', '455-567-4433', '899 Illness Rd', 'Corvallis', 'OR', 97330, '2001-04-14', 344, 2),
(4, 'Bill', 'Williams', '5555555555', 'house st', 'seattle', 'washington', 99999, '1980-09-04', 170, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nurseID` (`nurseID`);

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nurse`
--
ALTER TABLE `nurse`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `office`
--
ALTER TABLE `office`
  ADD PRIMARY KEY (`id`),
  ADD KEY `office_fk_1` (`managerID`);

--
-- Indexes for table `officedoctor`
--
ALTER TABLE `officedoctor`
  ADD PRIMARY KEY (`officeID`,`doctorID`),
  ADD KEY `assignment_fk_1` (`doctorID`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patient_fk_1` (`doctorID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `manager`
--
ALTER TABLE `manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `nurse`
--
ALTER TABLE `nurse`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `office`
--
ALTER TABLE `office`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_fk_1` FOREIGN KEY (`nurseID`) REFERENCES `nurse` (`id`);

--
-- Constraints for table `office`
--
ALTER TABLE `office`
  ADD CONSTRAINT `office_fk_1` FOREIGN KEY (`managerID`) REFERENCES `manager` (`id`);

--
-- Constraints for table `officedoctor`
--
ALTER TABLE `officedoctor`
  ADD CONSTRAINT `assignment_fk_1` FOREIGN KEY (`doctorID`) REFERENCES `doctor` (`id`),
  ADD CONSTRAINT `assignment_fk_2` FOREIGN KEY (`officeID`) REFERENCES `office` (`id`);

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `patient_fk_1` FOREIGN KEY (`doctorID`) REFERENCES `doctor` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
