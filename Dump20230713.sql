-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: booklent
-- ------------------------------------------------------
-- Server version	5.7.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(45) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rec_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `first_msg` varchar(45) NOT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (2,'i would like to buy your book on rent',35,19,16,'rent','first'),(5,'hi',35,19,16,'rent',''),(6,'ok',19,19,16,'rent',''),(7,'',35,19,16,'rent',''),(8,'',35,19,16,'rent',''),(9,'',35,19,16,'rent',''),(10,'',35,19,16,'rent',''),(11,'i would like to exchange my book with u',35,35,4,'rent','first'),(12,'ok',35,35,4,'rent','');
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exchange`
--

DROP TABLE IF EXISTS `exchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exchange` (
  `exc_id` int(11) NOT NULL AUTO_INCREMENT,
  `usr_bk_nm` varchar(45) NOT NULL,
  `book_of_exch` varchar(45) NOT NULL,
  `owner` varchar(45) NOT NULL,
  `exch_date` date NOT NULL,
  `usr_nm` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`exc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exchange`
--

LOCK TABLES `exchange` WRITE;
/*!40000 ALTER TABLE `exchange` DISABLE KEYS */;
INSERT INTO `exchange` VALUES (1,'test','god of war','a','2023-06-23','t','approved');
/*!40000 ALTER TABLE `exchange` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorite`
--

DROP TABLE IF EXISTS `favorite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorite` (
  `fav_id` int(11) NOT NULL AUTO_INCREMENT,
  `bk_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  PRIMARY KEY (`fav_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorite`
--

LOCK TABLES `favorite` WRITE;
/*!40000 ALTER TABLE `favorite` DISABLE KEYS */;
INSERT INTO `favorite` VALUES (1,16,35),(2,4,35);
/*!40000 ALTER TABLE `favorite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `genre_id` int(11) NOT NULL AUTO_INCREMENT,
  `genre_name` varchar(20) NOT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Adventure'),(2,'Fan Fiction'),(3,'The Wattys'),(4,'Contemporary Lit'),(5,'Diverse Lit'),(6,'Fantasy'),(7,'Historical Fiction'),(8,'Horror'),(9,'Humor'),(10,'Mystery'),(11,'Science'),(12,'Novels'),(13,'Romance'),(14,'Non-Fiction'),(15,'Biography'),(16,'Autobiography'),(17,'Business'),(18,'Poetry'),(19,'Travel'),(20,'Drama'),(21,'Fiction'),(22,'Children\'s'),(23,'crime/thriller');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre_selected`
--

DROP TABLE IF EXISTS `genre_selected`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre_selected` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre_selected`
--

LOCK TABLES `genre_selected` WRITE;
/*!40000 ALTER TABLE `genre_selected` DISABLE KEYS */;
INSERT INTO `genre_selected` VALUES (7,1,1),(8,1,2),(9,1,3),(10,1,1),(11,1,2),(12,1,3),(13,1,1),(14,1,2),(15,1,3),(16,35,14),(17,35,13),(18,35,8),(19,56,1),(20,56,8),(21,56,9),(22,57,1),(23,57,2),(24,57,3),(25,58,1),(26,58,2),(27,58,3);
/*!40000 ALTER TABLE `genre_selected` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loc`
--

DROP TABLE IF EXISTS `loc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loc` (
  `loc_id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` varchar(45) NOT NULL,
  `longitude` varchar(45) NOT NULL,
  PRIMARY KEY (`loc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loc`
--

LOCK TABLES `loc` WRITE;
/*!40000 ALTER TABLE `loc` DISABLE KEYS */;
INSERT INTO `loc` VALUES (1,'11.2587531','75.78041'),(2,'11.2587531','75.78041');
/*!40000 ALTER TABLE `loc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `loc_id` int(11) NOT NULL AUTO_INCREMENT,
  `town` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `pincode` int(6) NOT NULL,
  PRIMARY KEY (`loc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (3,'Calicut','Calicut',673636),(4,'Hgsyj','Bfsjs',864589),(5,'Kondotty','Kondotty',638536),(6,'Bgsjsban','Bzgusns',826728),(7,'Bgsjsban','Bzgusns',826728),(8,'Bgsjsban','Bzgusns',826728),(9,'Calicut','Calicut',836681),(10,'Pkd','Pkd',763728);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  `u_id` int(11) NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'admin','admin','admin',0),(2,'Gayu','Jhsusj','user',17),(4,'Athii','Hi','user',19),(5,'Athii','Hi','user',20),(6,'Athii','Hi','user',21),(8,'Kili','1234','user',23),(10,'Jishh','Jk','user',25),(13,'Bzgjsbsv','Vgjsbs','user',28),(14,'Bzgjsbsv','Vgjsbs','user',29),(15,'Bzgjsbsv','Vgjsbs','user',30),(16,'Bzgjsbsv','Vgjsbs','user',31),(17,'Bzgjsbsv','Vgjsbs','user',32),(18,'Bzgjsbsv','Vgjsbs','user',33),(19,'Jishna','Asdfg','user',34),(20,'ab','ab','user',35),(21,'Jk','Akk','user',36),(22,'u','u','user',37),(23,'Bsgjsn','Njskjs','user',38),(24,'jishna','asdfg','user',39),(25,'jishna','asdfg','user',40),(26,'athira','athii','user',41),(27,'aadiv','achu','user',42),(28,'aadiv','achu','user',43),(29,'Shibila','Shiii','user',44),(30,'Kili','Bshakn','user',45),(31,'jishna','jkk','user',46),(32,'vyvy','yutrsf','user',47),(33,'hdhhs','koo','user',48),(34,'gjfjt','fh','user',49),(35,'sfjfh','vhfh','user',50),(36,'jishna','aaa','user',51),(37,'jk','kkj','user',52),(38,'maa','maa','user',53),(39,'ggg','ssyyhvkkkjsyin','user',54),(40,'a','a','user',55),(41,'Babin','123456','user',56),(42,'babin','123456','user',57),(43,'rojith','1234','user',58),(44,'babin','12345','user',59),(45,'babin','1234','user',60),(46,'babin','12345','user',61),(47,'rohith','12345','user',62),(48,'rr','12345','user',63);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `noti_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(45) NOT NULL,
  `book` varchar(30) NOT NULL,
  PRIMARY KEY (`noti_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (1,'New book Published','16');
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `reg_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int(2) NOT NULL,
  `interest` varchar(30) NOT NULL,
  `phone_no` varchar(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`reg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (17,'Gayu','Female',0,'','6462882678','Sb fun nd','Jhsusj'),(19,'Athii','Female ',0,'','8623468642','Hfgdgjhfdghh','Hi'),(20,'Athii','Female ',0,'','8623468642','Hfgdgjhfdghh','Hi'),(21,'Athii','Female ',0,'','8623468642','Hfgdgjhfdghh','Hi'),(23,'Kili','Female',0,'','8547826788','Kili@gmail.com','1234'),(25,'Jishh','Female',0,'','8528536836','Jishna@gmail.com','Jk'),(28,'Bzgjsbsv','Bzgsjns',0,'','Bzgjana','Bgsjbs','Vgjsbs'),(29,'Bzgjsbsv','Bzgsjns',0,'','Bzgjana','Bgsjbs','Vgjsbs'),(30,'Bzgjsbsv','Bzgsjns',0,'','Bzgjana','Bgsjbs','Vgjsbs'),(31,'Bzgjsbsv','Bzgsjns',0,'','Bzgjana','Bgsjbs','Vgjsbs'),(32,'Bzgjsbsv','Bzgsjns',0,'','Bzgjana','Bgsjbs','Vgjsbs'),(33,'Bzgjsbsv','Bzgsjns',0,'','Bzgjana','Bgsjbs','Vgjsbs'),(34,'Jishna','Female',0,'','9725628853','Jish@gmail.com','Asdfg'),(35,'Kili','male',34,'dgsfg','9663836575','Ndhdksnb','Fine'),(36,'Jk','Male',0,'','9625827552','Nhajnsk','Akk'),(39,'jishna','female ',22,'poems ','6523678621','jushnatp@gmail.com','asdfg'),(40,'jishna','female ',22,'poems ','6523678621','jushnatp@gmail.com','asdfg'),(41,'athira','female ',22,'story ','3578732146','athira@gmail.com','athii'),(42,'aadiv','male',5,'story','8225527926','aadi@gmail.com','achu'),(43,'aadiv','male',5,'story','8225527926','aadi@gmail.com','achu'),(44,'Shibila','Female ',26,'Story','7755738557','Shibila@gmail.com','Shiii'),(45,'Kili','Bsgsb',14,'Nshajj','8661881572','Nshgsjab','Bshakn'),(46,'jishna','female',23,'poem','7362772572','jishna@gmail.com','jkk'),(47,'vyvy','vuvuc',7,'bhctd','7464768687','huftsrg','yutrsf'),(48,'hdhhs','bggj',23,'jhhh','8652728222','bbahaj','koo'),(49,'gjfjt','dhfh',56,'cbch','3646485836','cbcjgkkf','fh'),(50,'sfjfh','dghy',34,'bjvhf','3585236746','vncgdgo','vhfh'),(51,'jishna','f',4,'bcg','7426863367','gdjbn','aaa'),(52,'jk','male ',65,'vjchf','7532578436','jkchh','kkj'),(53,'maa','f',23,'bjvydt','3567357887','ma@gmail.com','maa'),(54,'ggg','m',12,'gghhhj','1234567890','dhhddkkju','ssyyhvkkkjsyin'),(55,'a','m',12,'gghhhj','1234567890','dhhddkkju','ssyyhvkkkjsyin'),(56,'Babin','male',22,'reading','9746524044','babindaskk@gmail.com','123456'),(57,'babin','male',23,'readinng','9789898988','bb@gmail.com','123456'),(58,'rojith','male',22,'reading','9876543212','bbb@gmail.com','1234'),(61,'babin','male',23,'sports','9876543212','bb@gmail.com','12345'),(62,'rohith','male',23,'spo','9876543212','bb@gmail.com','12345'),(63,'rr','male',24,'dk','9876543212','bb@gmail.com','12345');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rent`
--

DROP TABLE IF EXISTS `rent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rent` (
  `rnt_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `return_date` date NOT NULL,
  `amount` varchar(45) NOT NULL,
  `own_id` int(11) NOT NULL,
  `boorower_name` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `u_id` int(11) NOT NULL,
  PRIMARY KEY (`rnt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rent`
--

LOCK TABLES `rent` WRITE;
/*!40000 ALTER TABLE `rent` DISABLE KEYS */;
INSERT INTO `rent` VALUES (1,'god of war','2023-06-21','2023-06-28','300',35,'a','approved',55);
/*!40000 ALTER TABLE `rent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transcation`
--

DROP TABLE IF EXISTS `transcation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transcation` (
  `tran_id` int(11) NOT NULL AUTO_INCREMENT,
  `book` varchar(200) NOT NULL,
  `usr_nm` varchar(100) NOT NULL,
  PRIMARY KEY (`tran_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transcation`
--

LOCK TABLES `transcation` WRITE;
/*!40000 ALTER TABLE `transcation` DISABLE KEYS */;
INSERT INTO `transcation` VALUES (2,'god of war','t'),(3,'god of war','a');
/*!40000 ALTER TABLE `transcation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_post`
--

DROP TABLE IF EXISTS `user_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_post` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(50) NOT NULL,
  `Author_name` varchar(30) NOT NULL,
  `bio` text NOT NULL,
  `gen_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `image` varchar(500) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_post`
--

LOCK TABLES `user_post` WRITE;
/*!40000 ALTER TABLE `user_post` DISABLE KEYS */;
INSERT INTO `user_post` VALUES (1,'Fydhdhfu','Gdjfigi','Chgygxuduydu \n\n',13,0,'Available',''),(2,'Fydhdhfu','Gdjfigi','Chgygxuduydu \n\n',12,0,'Available',''),(3,'Akshysjb','Jsuaibs','Nshuaknsyducnqo nduuskwn .jsuusnsvgs. Sjyshksusklwb.bshyshwjwuhw,jgsuakbshs ',4,35,'Available',''),(4,'Chchfufu','Xhcuxuf','Bjhfsdkh gfuygyy z try rc cf uh difference y xiyydf',14,35,'Available',''),(5,'Murder on the Orient Express ','Agatha Christie','It is an interesting detective fiction. ',10,35,'Available',''),(6,'The Silence of the Lambs','Thomas Harris','very interesting crime/thriller story. ',23,35,'Available',''),(7,'Gone Girl','Gillian Flynn','Vycyfxtfx yfxtfib fduhb.',10,35,'Available',''),(8,'Gighxgx FC','Vicy day','Vuftshpk',15,45,'not Available',''),(9,'It gysrz guy g','Dry Dx I\'ll lb','Her as hb a try togk.',13,45,'not Available',''),(10,'Hjftstig','HzrZUCI','CGZR As IHO',14,45,'Available',''),(11,'test','HzrZUCI','CGZR As IHO',14,45,'Available',''),(12,'hsbgshssn','bshhajaa','bhahkaagsss',10,19,'Available',''),(13,'jshgsbgd','kbvvb','nhhgfgh',20,19,'Available',''),(14,'aasaas','adeefs','ascrasfrax',22,23,'Available',''),(15,'dd','dd','dd',3,35,'Available','TextEditingController#dba82(TextEditingValue(text: ┤dr.jpeg├, selection: TextSelection.invalid, composing: TextRange(start: -1, end: -1)))'),(16,'god of war','babin','njkk',8,19,'Available','TextEditingController#168db(TextEditingValue(text: ┤588b7baf1b0000260004cd54.jpeg├, selection: TextSelection.invalid, composing: TextRange(start: -1, end: -1)))');
/*!40000 ALTER TABLE `user_post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-13 14:13:52
