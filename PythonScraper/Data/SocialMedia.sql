-- MySQL dump 10.13  Distrib 5.6.19, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: SocialMedia
-- ------------------------------------------------------
-- Server version	5.6.19-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Document`
--

DROP TABLE IF EXISTS `Document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Document` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sparseWords` longtext,
  `text` longtext,
  `topics` longtext,
  `url` varchar(255) DEFAULT NULL,
  `timeDicovered` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Following`
--

DROP TABLE IF EXISTS `Following`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Following` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fromUser_id` int(11) NOT NULL,
  `toUser_id` int(11) NOT NULL,
  `timeCreated` datetime DEFAULT NULL,
  `timeDiscovered` datetime NOT NULL,
  `timeLastDiscovered` datetime NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Following_toUser_id` (`toUser_id`),
  KEY `Following_fromUser_id` (`fromUser_id`),
  KEY `Following_fromUser_id_toUser_id` (`fromUser_id`,`toUser_id`),
  CONSTRAINT `Following_ibfk_1` FOREIGN KEY (`fromUser_id`) REFERENCES `User` (`id`),
  CONSTRAINT `Following_ibfk_2` FOREIGN KEY (`toUser_id`) REFERENCES `User` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Liking`
--

DROP TABLE IF EXISTS `Liking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Liking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `document_id` int(11) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Liking_document_id` (`document_id`),
  KEY `Liking_user_id` (`user_id`),
  KEY `Liking_user_id_document_id` (`user_id`,`document_id`),
  CONSTRAINT `Liking_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`),
  CONSTRAINT `Liking_ibfk_2` FOREIGN KEY (`document_id`) REFERENCES `Document` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Posting`
--

DROP TABLE IF EXISTS `Posting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Posting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `document_id` int(11) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Posting_document_id` (`document_id`),
  KEY `Posting_user_id` (`user_id`),
  KEY `Posting_user_id_document_id` (`user_id`,`document_id`),
  CONSTRAINT `Posting_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`),
  CONSTRAINT `Posting_ibfk_2` FOREIGN KEY (`document_id`) REFERENCES `Document` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(255) NOT NULL,
  `timeCreated` datetime DEFAULT NULL,
  `timeDicovered` datetime NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-23  8:23:44
