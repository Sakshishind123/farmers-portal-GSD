-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: geeklogin
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(320) NOT NULL,
  `Role` varchar(20) DEFAULT NULL,
  `fid` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`email`),
  UNIQUE KEY `unique_fid` (`fid`),
  UNIQUE KEY `unique_fid2` (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES ('abcd','1','abc@gmail.com','Farmer',9),('ak','22','ak@gmail.com','Buyer',6),('gayatri ghone','11111','gayatri@gmail.com','Farmer',4),('hemant','123456','hemant@gmail.com','Farmer',8),('isha','111','isha@123gmail.com','Buyer',2),('mrudula','12345','mrudula@gmail.com','Farmer',7),('rutuja','222','rutuja@gmail.com','Buyer',5),('sakshi jadhav','12345','sakshi.22210493@gamil.com','Farmer',12),('sakshi shinde','12345','sakshi.22210493@viit.ac.in','Farmer',1),('sakshi shinde','11111','shinde@gmail.com','Farmer',10),('sakshi shinde','12345','shindesakshi98764@gmail.com','Farmer',11),('shreya','111','shreya@gmail.com','Farmer',3);
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `ch_id` int NOT NULL AUTO_INCREMENT,
  `bill_id` varchar(255) DEFAULT NULL,
  `sno` int NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`ch_id`),
  KEY `cart_ibfk_1` (`sno`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`sno`) REFERENCES `products` (`sno`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (41,'9377',38,'banana',32,12),(42,'9377',39,'apple',87,12),(43,'9377',39,'apple',87,33),(44,'9377',40,'apple',87,2),(45,'9377',40,'apple',87,1),(46,'9377',40,'apple',87,1),(47,'9377',40,'apple',87,1),(48,'9377',40,'apple',87,1),(49,'9377',40,'apple',87,1),(50,'9377',40,'apple',87,1),(51,'9377',40,'apple',87,1),(52,'9377',40,'apple',87,1),(53,'9377',40,'apple',87,1),(54,'6978',40,'apple',87,1),(55,'7494',40,'apple',87,1),(56,'3037',40,'apple',87,1),(57,'3523',40,'apple',87,5),(58,'3523',40,'apple',87,5),(59,'8940',42,'banana',20,2),(60,'8940',42,'banana',20,1),(61,'3970',40,'apple',87,1),(64,'3970',40,'apple',87,3),(67,'6575',41,'apple',87,5),(68,'6575',41,'apple',87,23),(69,'6575',41,'apple',87,3),(71,'6575',40,'apple',87,5),(73,'6575',41,'apple',87,12),(74,'6575',41,'apple',87,1),(76,'6575',40,'apple',87,1),(77,'6575',40,'apple',87,1),(78,'6575',40,'apple',87,1),(81,'6575',40,'apple',87,1),(83,'6575',40,'apple',87,1),(84,'6575',42,'banana',20,1),(85,'6575',40,'apple',87,1),(86,'6575',40,'apple',87,1),(87,'6575',40,'apple',87,1),(88,'8877',40,'apple',87,1),(89,'8877',40,'apple',87,1),(90,'8877',41,'apple',87,1),(91,'8877',40,'apple',87,2),(92,'8877',44,'stawbery',50,2),(93,'8246',44,'stawbery',50,1),(94,'8246',44,'stawbery',50,1),(100,'BILL-7625',47,'strawberry',12,3),(101,'BILL-7625',46,'apple',24,4),(102,'BILL-7625',47,'strawberry',12,1),(103,'BILL-7625',46,'apple',24,2),(104,'BILL-7625',45,'banana',20,1),(105,'BILL-7625',46,'apple',24,2),(106,'BILL-7625',47,'strawberry',12,2),(107,'BILL-7625',47,'strawberry',12,1),(108,'BILL-7625',47,'strawberry',12,1),(109,'BILL-7625',46,'apple',24,1),(110,'BILL-7625',47,'strawberry',12,5),(111,'4550',47,'strawberry',12,1),(116,'3156',45,'banana',20,2),(117,'3156',45,'banana',20,3),(118,'8147',45,'banana',20,8),(119,'8147',48,'strawberry',12,8),(120,'8147',45,'banana',20,2),(121,'8147',48,'strawberry',12,3);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `earning`
--

DROP TABLE IF EXISTS `earning`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `earning` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `fid` int NOT NULL,
  `amount_earned` float NOT NULL,
  `order_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  KEY `fid` (`fid`),
  CONSTRAINT `earning_ibfk_1` FOREIGN KEY (`fid`) REFERENCES `accounts` (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `earning`
--

LOCK TABLES `earning` WRITE;
/*!40000 ALTER TABLE `earning` DISABLE KEYS */;
INSERT INTO `earning` VALUES (1,1,100.5,'2024-12-13 09:48:38'),(2,1,36,'2024-12-13 09:22:37'),(3,1,40,'2024-12-13 09:25:43'),(4,1,12,'2024-12-13 09:25:43'),(5,1,96,'2024-12-13 12:04:45'),(6,1,20,'2025-03-06 16:09:57'),(7,1,12,'2025-03-06 16:09:57'),(8,1,36,'2025-03-06 16:52:57'),(9,1,48,'2025-03-06 16:52:57'),(10,1,72,'2025-03-25 06:53:20'),(11,1,24,'2025-03-25 06:53:20'),(12,1,12,'2025-03-26 04:11:18'),(13,1,24,'2025-03-26 04:11:18'),(14,1,36,'2025-03-27 06:16:04');
/*!40000 ALTER TABLE `earning` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmer`
--

DROP TABLE IF EXISTS `farmer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `farmerid` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `farmerid` (`farmerid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer`
--

LOCK TABLES `farmer` WRITE;
/*!40000 ALTER TABLE `farmer` DISABLE KEYS */;
/*!40000 ALTER TABLE `farmer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `fid` int NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `quantity` int NOT NULL,
  `category` varchar(50) NOT NULL,
  `date_created` datetime DEFAULT CURRENT_TIMESTAMP,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (38,1,'banana',32,0,'Fruit','2024-09-05 06:06:13',NULL),(39,1,'apple',87,0,'Fruit','2024-09-05 06:06:24',NULL),(40,1,'apple',87,0,'Fruit','2024-09-05 06:16:11',NULL),(41,10,'apple',87,0,'Fruit','2024-11-26 07:13:44',NULL),(42,10,'banana',20,0,'Fruit','2024-11-26 07:14:00',NULL),(43,1,'banana',20,0,'Fruit','2024-12-13 06:34:24',NULL),(44,1,'stawbery',50,0,'Fruit','2024-12-13 06:34:41',NULL),(45,1,'banana',20,0,'Fruit','2024-12-13 07:22:37',NULL),(46,1,'apple',24,18,'Fruit','2024-12-13 07:22:50',NULL),(47,1,'strawberry',12,0,'Fruit','2024-12-13 07:23:07',NULL),(48,1,'strawberry',12,7,'Fruit','2024-12-13 10:26:35',NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-27 16:11:22
