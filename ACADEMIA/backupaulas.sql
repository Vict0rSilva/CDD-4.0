-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: academiaturmad
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `matricula` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `cpf` char(11) DEFAULT NULL,
  `end` varchar(256) DEFAULT NULL,
  `tel` char(11) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (1,'joao','71295501762','rua joao das dores','81993220873','joaozinho123@gmail.com'),(2,'lunara','85696696325','rua lunara das dores','8196552148','lunal@gmail.com'),(3,'poli','85696632325','rua do cavalo','8196552448','polidogera@gmail.com'),(4,'marcelino','85696632325','rua do mama','8185447125','martelo@gmail.com'),(5,'bila','85696396325','rua da bila','8296552148','bila123@gmail.com'),(6,'bila',NULL,NULL,'00000000000',NULL),(7,'bila',NULL,NULL,'00000000000',NULL),(8,'bila',NULL,NULL,'00000000000',NULL),(9,'bila',NULL,NULL,'00000000000',NULL);
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `func`
--

DROP TABLE IF EXISTS `func`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `func` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `cpf` char(11) NOT NULL,
  `departamento` int NOT NULL,
  `salario` decimal(8,2) DEFAULT NULL,
  `quantidade_filhos` int NOT NULL,
  PRIMARY KEY (`id_funcionario`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `func`
--

LOCK TABLES `func` WRITE;
/*!40000 ALTER TABLE `func` DISABLE KEYS */;
INSERT INTO `func` VALUES (2,'maria santos','01397207547',1,4485.00,0),(3,'jose','00397740291',4,3900.00,0),(4,'luanna','75869993601',5,3600.00,0),(5,'danilo','52536652141',6,3600.00,0),(6,'poli','69696969696',1,5400.00,0),(7,'isa','01010102014',1,4400.00,0),(8,'marcelo','01397207576',8,10000.00,0),(9,'hawk','14263301258',8,12000.00,0),(10,'isabele','03692201038',8,52000.00,0);
/*!40000 ALTER TABLE `func` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modalidades`
--

DROP TABLE IF EXISTS `modalidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modalidades` (
  `id_mod` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  PRIMARY KEY (`id_mod`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modalidades`
--

LOCK TABLES `modalidades` WRITE;
/*!40000 ALTER TABLE `modalidades` DISABLE KEYS */;
INSERT INTO `modalidades` VALUES (1,'judo'),(2,'capoeira'),(3,'box'),(4,'kikibox'),(5,'ginastica');
/*!40000 ALTER TABLE `modalidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `cpf` char(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cref` char(6) NOT NULL,
  `tel` char(11) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` VALUES ('9033990122','aulara','523206','89030330434','aur32l@gmail.com'),('90339909809','jojde','323222','89030000000','adaaad@gmail.com'),('90339909832','aula','523202','89030330044','aurl@gmail.com'),('90339909869','jojdea','323202','89030330000','adfaad@gmail.com'),('90399909809','joje','323232','89000000000','adad@gmail.com');
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-16 17:48:50
