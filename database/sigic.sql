-- MySQL dump 10.13  Distrib 8.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: micromercado
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `contacto` varchar(20) DEFAULT NULL,
  `cedula` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (4,'Diego','Suarez','3222053551','1014659694'),(5,'Luis','Fuentes','3226459664','1015169534'),(6,'N/A','N/A','0','0');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallesventas`
--

DROP TABLE IF EXISTS `detallesventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detallesventas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_producto` int DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `valor_unitario` decimal(10,2) DEFAULT NULL,
  `valor_total` decimal(10,2) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `id_venta` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallesventas`
--

LOCK TABLES `detallesventas` WRITE;
/*!40000 ALTER TABLE `detallesventas` DISABLE KEYS */;
INSERT INTO `detallesventas` VALUES (1,3,4,2,5400.00,10800.00,'2025-06-18',2),(2,10,4,1,3432.00,3432.00,'2025-06-18',2),(3,8,4,2,4560.00,9120.00,'2025-06-18',2),(4,6,4,1,8400.00,8400.00,'2025-06-18',2),(5,9,4,1,2160.00,2160.00,'2025-06-18',2),(6,7,5,3,720.00,2160.00,'2025-06-18',3),(7,3,4,2,5400.00,10800.00,'2025-06-18',4),(8,9,4,2,2160.00,4320.00,'2025-06-18',4),(9,10,4,1,3432.00,3432.00,'2025-06-18',4),(10,7,4,1,720.00,720.00,'2025-06-18',4),(11,10,4,4,3432.00,13728.00,'2025-06-18',5),(12,7,4,2,720.00,1440.00,'2025-06-18',6),(13,8,4,2,4560.00,9120.00,'2025-06-18',7),(14,6,4,1,8400.00,8400.00,'2025-06-18',7),(15,10,4,1,3432.00,3432.00,'2025-06-18',7),(16,8,4,1,4560.00,4560.00,'2025-06-18',8),(17,10,4,6,3432.00,20592.00,'2025-06-18',8),(18,10,4,10,3432.00,34320.00,'2025-06-19',9),(19,10,4,5,3432.00,17160.00,'2025-06-19',10),(20,3,4,1,5400.00,5400.00,'2025-06-20',11),(21,2,6,4,1200.00,4800.00,'2025-06-21',12),(22,8,6,2,4560.00,9120.00,'2025-06-21',12),(23,10,6,3,3432.00,10296.00,'2025-06-21',12),(24,2,6,1,1200.00,1200.00,'2025-06-21',13),(25,16,6,1,960.00,960.00,'2025-06-21',14),(26,16,4,1,960.00,960.00,'2025-06-21',15),(27,18,6,22,2400.00,52800.00,'2025-06-21',16),(28,16,4,1,960.00,960.00,'2025-06-21',17),(29,16,4,1,960.00,960.00,'2025-06-21',18),(30,16,6,1,960.00,960.00,'2025-06-21',19);
/*!40000 ALTER TABLE `detallesventas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(100) DEFAULT NULL,
  `codigo` varchar(50) DEFAULT NULL,
  `precio_compra` decimal(10,2) DEFAULT NULL,
  `precio_venta` decimal(10,2) DEFAULT NULL,
  `descripcion` text,
  `presentacion` varchar(100) DEFAULT NULL,
  `ubicacion` varchar(100) DEFAULT NULL,
  `stock_minimo` int DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `id_proveedor` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_proveedor` (`id_proveedor`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (13,'queso tajado ','2-0001',5800.00,6960.00,'','paquete 250 gramos ','nevera 5 ',NULL,NULL,1,10,'',NULL),(14,'Yogurt Griego x500ml','2-0002',5000.00,6000.00,'','envase','Nevera 3',NULL,NULL,4,20,'yogurt_500ml.png','Lacteos'),(15,'Doritos 200 gramos','9-0001',2500.00,3000.00,'Doritos 200 gramos','bolsa','Pasillo 1',NULL,NULL,4,3,'Doritos_200gr.png','Confiteria'),(16,'Salsa Tomate fruco','15-0001',800.00,960.00,'Salsa Fruco de tomate','sobre','vitrina 2',NULL,NULL,3,19,'','Salsamentaria'),(17,'Cebolla Larga','1-001',4000.00,4800.00,'','Unidad','Nevera 3',NULL,NULL,1,200,'cebollaLarga.png','Frutas y verduras'),(18,'papas margarita pollo ','9-0002',2000.00,2400.00,'','bolsa','vitrina 2',NULL,NULL,3,3,'','Confiteria');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empresa` varchar(100) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `contacto` varchar(20) DEFAULT NULL,
  `telefono2` varchar(20) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (1,'Distribuidora La 14','Camilo Rojas','3109988776',NULL,NULL),(2,'Frutas del Valle','Marta Díaz','3155544332',NULL,NULL),(3,'Lestharkin','Camilo rodriguez','3222053551',NULL,NULL),(4,'Drivezone','luis fuentes','3229146551',NULL,NULL);
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(100) DEFAULT NULL,
  `contraseña` varchar(255) DEFAULT NULL,
  `rol` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'omar','prueba','administrador'),(2,'empleado1','emp123','empleado');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_venta` date DEFAULT NULL,
  `total_venta` decimal(10,2) DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  KEY `fk_ventas_cliente` (`id_cliente`),
  CONSTRAINT `fk_ventas_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (2,'2025-06-18',33912.00,1,4),(3,'2025-06-18',2160.00,1,5),(4,'2025-06-18',19272.00,1,4),(5,'2025-06-18',13728.00,1,4),(6,'2025-06-18',1440.00,1,4),(7,'2025-06-18',20952.00,1,4),(8,'2025-06-18',25152.00,1,4),(9,'2025-06-19',34320.00,1,4),(10,'2025-06-19',17160.00,1,4),(11,'2025-06-20',5400.00,1,4),(12,'2025-06-21',24216.00,1,6),(13,'2025-06-21',1200.00,1,6),(14,'2025-06-21',960.00,1,6),(15,'2025-06-21',960.00,1,4),(16,'2025-06-21',52800.00,1,6),(17,'2025-06-21',960.00,1,4),(18,'2025-06-21',960.00,1,4),(19,'2025-06-21',960.00,1,6);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-21 23:47:48
