-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 05 oct. 2023 à 13:56
-- Version du serveur : 8.0.20
-- Version de PHP : 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `e_commande`
--

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE `categories` (
  `id` int NOT NULL,
  `nom_categorie` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `categories`
--

INSERT INTO `categories` (`id`, `nom_categorie`) VALUES
(19, 'Boissons'),
(20, 'Menu Viande BBQ'),
(21, 'Menu Mix Grill'),
(22, 'Menu Burgers'),
(23, 'Menu Brochettes'),
(24, 'Accompagnement'),
(25, 'Menu Saisonnier'),
(26, 'olive');

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

CREATE TABLE `commande` (
  `id_commande` int NOT NULL,
  `nom_client` varchar(255) NOT NULL,
  `contenu_commande` text,
  `date_commande` varchar(25) DEFAULT NULL,
  `matricule_employe` varchar(50) DEFAULT NULL,
  `recu_commande` varchar(255) DEFAULT NULL,
  `total_commande` double DEFAULT NULL,
  `statuts` bit(1) DEFAULT NULL,
  `numero_table` int DEFAULT NULL,
  `montant_recu` double DEFAULT NULL,
  `monnaie` double DEFAULT NULL,
  `cuisine` tinyint(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `commande`
--

INSERT INTO `commande` (`id_commande`, `nom_client`, `contenu_commande`, `date_commande`, `matricule_employe`, `recu_commande`, `total_commande`, `statuts`, `numero_table`, `montant_recu`, `monnaie`, `cuisine`) VALUES
(2, 'jean', '5xCoca Cola', '2023-07-22 11:50:55', '', 'facture_jean.pdf', 5000, b'1', 2, NULL, NULL, NULL),
(3, 'emma', '2xCoca Cola', '2023-07-21 13:17:01', '', 'facture_emma.pdf', 2000, b'1', 5, NULL, NULL, NULL),
(4, 'kouadio', '2xCoca Cola, 2xFanta', '2023-07-21 13:19:52', '', 'facture_kouadio.pdf', 5000, b'1', 2, NULL, NULL, NULL),
(5, 'jean', '2xCoca Cola, 2xOrangina', '2023-07-26 10:11:40', 'FAYE7974', 'facture_jean.pdf', 6000, b'1', 5, NULL, NULL, NULL),
(6, 'Manuel', '5xCoca Cola, 5xFanta', '2023-08-26 10:20:02', 'TANOH1548', 'facture_Manuel.pdf', 12500, b'1', 2, NULL, NULL, NULL),
(7, 'jean', '2xCoca Cola', '2023-08-26 10:41:19', 'FAYE7974', 'facture_jean.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(8, 'tanoh eliezer', '2xCoca Cola, 2xFanta, 2xOrangina', '2023-08-26 10:46:22', 'FAYE7974', 'facture_tanoh eliezer.pdf', 9000, b'1', 2, NULL, NULL, NULL),
(9, 'ursula', '2xCoca Cola', '2023-08-26 11:01:47', 'FAYE7974', 'facture_ursula.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(10, 'jean', '2xCoca Cola, 2xFanta', '2023-08-26 11:05:27', 'FAYE7974', 'facture_jean.pdf', 5000, b'1', 3, NULL, NULL, NULL),
(11, 'jean', '2xCoca Cola, 2xFanta', '2023-08-26 11:25:44', 'FAYE7974', 'facture_jean.pdf', 5000, b'1', 2, NULL, NULL, NULL),
(12, 'emma', '', '2023-08-26 11:28:44', 'FAYE7974', 'facture_emma.pdf', 0, b'1', 2, NULL, NULL, NULL),
(13, 'tanoh eliezer', '0xFanta', '2023-08-26 11:44:07', 'FAYE7974', 'facture_tanoh eliezer.pdf', 0, b'1', 2, NULL, NULL, NULL),
(14, 'tanoh eliezer', '1xFanta', '2023-09-01 11:05:07', 'FAYE7974', 'facture_tanoh eliezer.pdf', 1500, b'1', 2, NULL, NULL, NULL),
(15, 'alexhitchens', '1xFanta', '2023-09-01 11:06:37', 'FAYE7974', 'facture_alexhitchens.pdf', 1500, b'1', 8, NULL, NULL, NULL),
(16, 'alex', '2xCoca Cola, 2xFanta', '2023-09-05 08:57:23', 'FAYE7974', 'facture_alex.pdf', 5000, b'1', 2, NULL, NULL, NULL),
(17, 'ursula', '2xCoca Cola, 2xFanta', '2023-09-05 09:00:23', 'FAYE7974', 'facture_ursula.pdf', 5000, b'1', 5, NULL, NULL, NULL),
(18, 'tanoh eliezer', '0xFanta', '2023-09-05 09:05:32', 'FAYE7974', 'facture_tanoh eliezer.pdf', 0, b'1', 4, NULL, NULL, NULL),
(19, 'spiderman', '5xCoca Cola, 5xFanta', '2023-09-05 10:13:38', 'FAYE7974', 'facture_spiderman.pdf', 12500, b'1', 2, NULL, NULL, NULL),
(20, 'ursula', '1xCoca Cola, 1xFanta', '2023-09-07 10:21:03', 'FAYE7974', 'facture_ursula.pdf', 2500, b'1', 2, NULL, NULL, NULL),
(21, 'speed', '0xFanta', '2023-09-07 10:49:54', 'FAYE7974', 'facture_speed.pdf', 0, b'1', 2, NULL, NULL, NULL),
(22, 'jean', '2xCoca Cola', '2023-09-07 11:19:27', 'FAYE7974', 'facture_jean.pdf', 2000, b'1', 1, NULL, NULL, NULL),
(23, 'tanoh eliezer', '2xCoca Cola', '2023-09-07 11:26:34', 'FAYE7974', 'facture_tanoh eliezer.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(24, 'tanoh eliezer', '2xCoca Cola', '2023-09-07 11:39:32', 'FAYE7974', 'facture_tanoh eliezer.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(25, 'tanoh eliezer', '2xCoca Cola', '2023-09-07 11:45:26', 'FAYE7974', 'facture_tanoh eliezer.pdf', 2000, b'1', 1, NULL, NULL, NULL),
(26, 'emma', '2xCoca Cola', '2023-09-07 13:06:29', 'TANOH1548', 'facture_emma.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(27, 'tanoh eliezer', '2xCoca Cola', '2023-09-07 13:07:56', 'TANOH1548', 'facture_tanoh eliezer.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(28, 'tanoh eliezer', '2xCoca Cola', '2023-09-07 13:12:17', 'TANOH1548', 'facture_tanoh eliezer.pdf', 2000, b'1', 2, NULL, NULL, NULL),
(29, 'rr', '2xpoulet', '2023-09-09 08:23:21', 'FAYE7974', 'facture_rr.pdf', 14000, b'1', 2, NULL, NULL, NULL),
(30, 'rr2', '2xpoulet, 2xpoisson', '2023-09-09 08:26:18', 'FAYE7974', 'facture_rr2.pdf', 25200, b'1', 1, NULL, NULL, NULL),
(31, 'rr3', '2xSteak', '2023-09-09 10:26:20', 'TANOH1548', 'facture_rr3.pdf', 30000, b'1', 1, NULL, NULL, NULL),
(32, 'rr4', '1xSteak, 1xPizza Calebreze', '2023-09-09 10:27:25', 'TANOH1548', 'facture_rr4.pdf', 21000, b'1', 1, NULL, NULL, NULL),
(33, 'tanoh eliezer', '2xSteak', '2023-09-10 08:39:38', 'FAYE7974', 'facture_tanoh eliezer.pdf', 30000, b'1', 2, NULL, NULL, NULL),
(34, 'tanoh eliezer', '2xSteak', '2023-09-10 08:42:20', 'FAYE7974', 'facture_tanoh eliezer.pdf', 30000, b'1', 2, NULL, NULL, NULL),
(35, 'emilie', '2xPizza royale', '2023-09-11 12:08:31', 'FAYE7974', 'facture_emilie.pdf', 12000, b'1', 2, NULL, NULL, NULL),
(36, 'emilie', '2xPizza royale', '2023-09-14 09:23:41', 'FAYE7974', 'facture_emilie.pdf', 12000, b'1', 2, NULL, NULL, NULL),
(37, 'Tanoh Eliezer Bonny', '2xPizza royale', '2023-09-14 10:29:13', 'FAYE7974', 'facture_Tanoh Eliezer Bonny.pdf', 12000, b'1', 1, NULL, NULL, NULL),
(38, 'jean', '1xPizza royale', '2023-09-15 09:22:15', 'FAYE7974', 'facture_jean.pdf', 6000, b'1', 1, NULL, NULL, NULL),
(39, 'rr5', '1xPizza royale', '2023-09-15 09:23:50', 'FAYE7974', 'facture_rr5.pdf', 6000, b'1', 2, NULL, NULL, NULL),
(40, '', '2xgarba', '2023-09-15 10:13:54', 'FAYE7974', 'facture_.pdf', 8000, b'1', 1, NULL, NULL, NULL),
(41, 'olive', '2xEau minerale, 2xSteak Filet De Boeuf', '2023-09-21 10:08:08', 'FAYE7974', 'facture_olive.pdf', 20000, b'1', 1, NULL, NULL, NULL),
(42, 'emilie', '1xEau minerale, 1xCoca-Cola, 1xBurger Grand Canyos', '2023-09-21 11:23:12', 'FAYE7974', 'facture_emilie.pdf', 10000, b'1', 2, NULL, NULL, NULL),
(43, 'akon', '1xEau minerale, 1xCoca-Cola, 1xRibs O Ribs', '2023-09-21 11:26:59', 'FAYE7974', 'facture_akon.pdf', 11000, b'1', 1, NULL, NULL, NULL),
(44, 'olive', '1xCoca-Cola, 1xSteak Filet De Boeuf', '2023-09-21 14:43:41', 'FAYE7974', 'facture_olive.pdf', 10000, b'1', 1, NULL, NULL, NULL),
(45, 'emilie', '1xEau minerale, 1xSteak Filet De Boeuf', '2023-09-21 14:47:51', 'FAYE7974', 'facture_emilie.pdf', 10000, b'1', 2, NULL, NULL, NULL),
(46, 'olive', '2xEau minerale, 2xPoulet Texan Demi', '2023-09-21 15:19:19', 'FAYE7974', 'facture_olive.pdf', 10000, b'1', 1, 10000, 0, NULL),
(47, 'olive', '2xEau minerale, 2xPoulet Texan Demi', '2023-09-21 15:23:37', 'FAYE7974', 'facture_olive.pdf', 10000, b'1', 3, 10000, 0, NULL),
(48, 'olive', '2xEau minerale, 2xPoulet Texan Demi', '2023-09-21 15:29:58', 'FAYE7974', 'facture_olive.pdf', 10000, b'1', 1, 10000, 0, NULL),
(49, 'emilie', '1xEau minerale, 1xSteak Filet De Boeuf', '2023-09-21 15:31:41', 'FAYE7974', 'facture_emilie.pdf', 10000, b'1', 1, 30000, -20000, NULL),
(50, 'olive', '2xEau minerale, 2xPoulet Texan Demi', '2023-09-21 15:36:40', 'FAYE7974', 'facture_olive.pdf', 10000, b'1', 1, 20000, -10000, NULL),
(51, 'emilie', '2xEau minerale, 2xCoca-Cola', '2023-09-21 15:38:45', 'FAYE7974', 'facture_emilie.pdf', 4000, b'1', 2, 20000, -16000, NULL),
(52, 'olive', '1xEau minerale, 1xCoca-Cola, 1xPoulet Texan Demi', '2023-09-21 15:42:56', 'FAYE7974', 'facture_olive.pdf', 6000, b'1', 3, 10000, 4000, NULL),
(53, 'olive', '1xEau minerale, 1xCoca-Cola, 1xPoulet Texan Demi', '2023-09-21 15:45:30', 'FAYE7974', 'facture_olive.pdf', 6000, b'1', 1, 1, -5999, NULL),
(54, 'Tanoh Eliezer Bonny', '2xEau minerale, 2xCoca-Cola, 2xPoulet Texan Demi', '2023-09-21 16:01:38', 'FAYE7974', 'facture_Tanoh Eliezer Bonny.pdf', 12000, b'1', 2, 10000, -2000, NULL),
(55, 'akon lonely', '2xEau minerale, 2xPoulet Texan Demi', '2023-09-21 16:11:05', 'FAYE7974', 'facture_akon lonely.pdf', 10000, b'1', 3, 10000, 0, NULL),
(56, 'emilie', '1xCoca-Cola, 1xPoulet Texan Demi', '2023-09-21 16:15:52', 'FAYE7974', 'facture_emilie.pdf', 5000, b'1', 2, 10000, 5000, NULL),
(57, 'olive', '1xCoca-Cola', '2023-09-21 16:17:24', 'FAYE7974', 'facture_olive.pdf', 1000, b'1', 1, 10000, 9000, NULL),
(58, 'tanoh eliezer', '1xEau minerale', '2023-09-22 12:35:37', 'FAYE7974', 'facture_tanoh eliezer.pdf', 1000, b'1', 1, 10000, 9000, 1),
(59, 'jean', '2xEau minerale', '2023-09-22 13:17:40', 'FAYE7974', 'facture_jean.pdf', 2000, b'1', 1, 12000, 10000, 1),
(60, 'jean', '2xEau minerale', '2023-09-22 13:37:41', 'FAYE7974', 'facture_jean.pdf', 2000, b'1', 1, 4000, 2000, 1),
(61, 'olive', '2xEau minerale, 1xEau minerale, 2xCoca-Cola, 1xCoca-Cola', '2023-09-23 16:59:27', 'FAYE7974', 'facture_olive_7281.pdf', 6000, b'1', 1, 5000, -1000, 1),
(62, 'olive', '2xEau minerale, 1xEau minerale, 2xCoca-Cola, 1xCoca-Cola', '2023-09-23 17:24:17', 'FAYE7974', 'facture_olive_3370.pdf', 6000, b'1', 2, 5000, -1000, 1),
(63, 'emilie', '2xEau minerale, 2xCoca-Cola, 1xEau minerale, 1xCoca-Cola', '2023-09-23 17:27:30', 'FAYE7974', 'facture_emilie_8793.pdf', 6000, b'1', 3, 5000, -1000, 1),
(64, 'olive', '2xEau minerale, 2xCoca-Cola, 1xEau minerale, 1xCoca-Cola', '2023-09-23 17:31:01', 'FAYE7974', 'facture_olive_5192.pdf', 6000, b'1', 1, 5000, -1000, 1),
(65, 'olive', '2xEau minerale, 1xCoca-Cola', '2023-09-23 17:36:26', 'FAYE7974', 'facture_olive_1065.pdf', 3000, b'1', 2, 5000, 2000, 1),
(66, 'olive', '1xCoca-Cola, 2xFanta-Cocktail', '2023-09-23 17:44:49', 'FAYE7974', 'facture_olive_6396.pdf', 3000, b'1', 3, 5000, 2000, 1),
(67, 'akon', '1xCocktail, 1xRibs O Ribs', '2023-09-23 18:07:35', 'FAYE7974', 'facture_akon_1838.pdf', 11500, b'1', 1, 20000, 8500, 1),
(68, 'olive', '1xFanta-Cocktail, 1xCotes De Porc', '2023-09-23 18:09:24', 'FAYE7974', 'facture_olive_1765.pdf', 8000, b'1', 4, 50000, 42000, 1),
(69, 'jean', '2xEau minerale, 3xFanta-Cocktail, 4xPoulet Texan Demi, 3xBurger Grand Canyos', '2023-09-24 16:22:41', 'FAYE7974', 'facture_jean_6837.pdf', 45000, b'1', 1, 100000, 55000, 1),
(70, 'olive', '2xEau minerale, 1xCocktail, 2xPoulet Texan Entier, 1xRibs O Ribs', '2023-09-27 17:12:08', 'TCHOMAN3180', 'facture_olive_8983.pdf', 27500, b'1', 2, 50000, 22500, 1),
(71, 'olive', '1xEau minerale, 2xCoca-Cola, 1xPoulet Texan Demi', '2023-09-27 19:16:43', 'TCHOMAN3180', 'facture_olive_3902.pdf', 7000, b'1', 1, 50000, 43000, 1),
(72, 'emilie', '2xCoca-Cola, 1xFanta-Cocktail, 1xPoulet Texan Demi', '2023-09-27 19:18:58', 'TCHOMAN3180', 'facture_emilie_4810.pdf', 7000, b'1', 2, 15000, 8000, 1),
(73, 'emilie', '2xCoca-Cola, 1xCocktail, 1xPoulet Texan Demi', '2023-09-27 20:31:08', 'TCHOMAN3180', 'facture_emilie_4570.pdf', 8500, b'1', 3, 50000, 41500, 1),
(74, 'emilie', '2xCoca-Cola, 1xCocktail, 2xPoulet Texan Demi, 1xPoulet Texan Entier', '2023-09-27 20:36:40', 'TCHOMAN3180', 'facture_emilie_1596.pdf', 19500, b'1', 4, 50000, 30500, 1),
(75, 'jean', '1xEau minerale, 2xCocktail, 1xPoulet Texan Demi', '2023-09-28 07:33:09', 'FAYE7974', 'facture_jean_3544.pdf', 10000, b'1', 1, 50000, 40000, 1),
(76, 'rr', '2xEau minerale, 1xCoca-Cola', '2023-09-30 10:45:59', 'FAYE7974', 'facture_rr_9058.pdf', 3000, b'1', 1, 5000, 2000, 1),
(77, 'olive', '1xEau minerale, 3xCoca-Cola, 2xBoeuf-Poulet', '2023-09-30 12:44:58', 'TCHOMAN3180', 'facture_olive_9113.pdf', 64000, b'1', 2, 50000, -14000, 1),
(78, 'emilie', '2xCoca-Cola, 2xBrochettes De Poulet, 1xAlloco', '2023-09-30 17:04:13', 'TCHOMAN3180', 'facture_emilie_3597.pdf', 6000, b'1', 1, 20000, 14000, 1),
(79, 'olive', '1xEau minerale, 1xCoca-Cola', '2023-09-30 17:26:29', 'TCHOMAN3180', 'facture_olive_7126.pdf', 2000, b'1', 1, 5000, 3000, 1),
(80, 'jean', '2xEau minerale', '2023-10-02 09:16:36', 'FAYE7974', 'facture_jean_4754.pdf', 2000, b'1', 1, 5000, 3000, 1),
(81, 'tanoh eliezer', '1xEau minerale, 2xCoca-Cola', '2023-10-02 13:32:00', 'FAYE7974', 'facture_tanoh eliezer_6605.pdf', 3000, b'1', 2, 5000, 2000, 1),
(82, 'jean', '1xSteak Filet De Boeuf', '2023-10-02 13:41:20', 'FAYE7974', 'facture_jean_2369.pdf', 9000, b'1', 3, 10000, 1000, 1),
(83, 'jean', '2xCocktail', '2023-10-02 13:42:58', 'FAYE7974', 'facture_jean_8015.pdf', 5000, b'1', 4, 5000, 0, 1),
(84, 'jean', '1xEau minerale', '2023-10-03 09:27:06', 'FAYE7974', 'facture_jean_7288.pdf', 1000, b'1', 1, 2000, 1000, 1),
(85, 'tanoh eliezer', '2xCocktail', '2023-10-03 09:28:00', 'FAYE7974', 'facture_tanoh eliezer_9588.pdf', 5000, b'1', 2, 5000, 0, 1),
(86, 'Tanoh Eliezer Bonny', '1xEau minerale', '2023-10-03 16:37:03', 'FAYE7974', 'facture_Tanoh Eliezer Bonny_2268.pdf', 1000, b'1', 3, 5000, 4000, 1);

-- --------------------------------------------------------

--
-- Structure de la table `employe`
--

CREATE TABLE `employe` (
  `id_employe` int NOT NULL,
  `nom_employe` varchar(255) NOT NULL,
  `prenom_employe` varchar(255) DEFAULT NULL,
  `email_employe` varchar(255) NOT NULL,
  `poste_employe` varchar(255) NOT NULL,
  `numero_telephone` varchar(30) NOT NULL,
  `ville_employe` varchar(255) NOT NULL,
  `date_naissance_employe` varchar(10) DEFAULT NULL,
  `password_employe` varchar(255) NOT NULL,
  `acces` enum('admin','employe') DEFAULT NULL,
  `image_employe` varchar(255) DEFAULT NULL,
  `matricule_employe` varchar(50) NOT NULL,
  `date_embauche` datetime DEFAULT NULL,
  `actif` tinyint(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `employe`
--

INSERT INTO `employe` (`id_employe`, `nom_employe`, `prenom_employe`, `email_employe`, `poste_employe`, `numero_telephone`, `ville_employe`, `date_naissance_employe`, `password_employe`, `acces`, `image_employe`, `matricule_employe`, `date_embauche`, `actif`) VALUES
(9, 'tanoh', 'eliezer bonny', 'tanoheliezerbonny@gmail.com', 'administrateur', '0767293757', 'Abidjan', '2002-03-18', '$5$rounds=535000$..qn0whT6xMNONcy$H4uOFOGwo8MyoPlqLADI4VEhbNaqFdfieqr9B93w0.D', 'admin', 'tanoh.jpg', 'TANOH1548', NULL, 1),
(10, 'Faye', 'Emma', 'fayeemma@gmail.com', 'serveuse', '0708445544', 'yopougon', '2002-02-25', '$5$rounds=535000$h1DXPg38bORjeU8V$muhgUDLG4iChPbNKuxiRdTUchSaV8w5vqMBd9D9AFzD', 'employe', 'IMG-20230821-WA0018.jpg', 'FAYE7974', NULL, 0),
(11, 'Uchiwa', 'Madara', 'madara@gmail.com', 'Serveur', '0767741454', 'BINGERVILLE', '2001-01-16', '$5$rounds=535000$YOrSxSRsrqLVhymb$c44eal/3dD4PJt4vxtfMwuqGL9Hm1c3uRyb5/pIQQ04', 'employe', '665330.png', 'UCHIWA9676', '2023-09-21 00:00:00', 0),
(12, 'Tchoman', 'Josee', 'josee@gmail.com', 'Serveur(se)', '0787156821', 'Dabou', '2000-12-11', '$5$rounds=535000$2DVzeaTdqYzBzdK0$jmapv9hvhqmcZDjwYCn3awMzIeepWw8jlHEPAOvMtC8', 'employe', 'WhatsApp Image 2023-09-27 à 17.02.03.jpg', 'TCHOMAN3180', '2023-09-27 00:00:00', 0);

-- --------------------------------------------------------

--
-- Structure de la table `menu`
--

CREATE TABLE `menu` (
  `id_menu` int NOT NULL,
  `nom_plat` varchar(255) NOT NULL,
  `prix` int NOT NULL,
  `image` varchar(225) DEFAULT NULL,
  `categories` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `menu`
--

INSERT INTO `menu` (`id_menu`, `nom_plat`, `prix`, `image`, `categories`) VALUES
(13, 'Eau minerale', 1000, 'awa.png', 'Boissons'),
(14, 'Coca-Cola', 1000, 'coca-cola.png', 'Boissons'),
(15, 'Fanta-Cocktail', 1000, 'fanta-cocktail-last.png', 'Boissons'),
(16, 'Cocktail', 2500, 'cocktail.jpg', 'Boissons'),
(17, 'Fanta', 1000, 'fanta1-1.png', 'Boissons'),
(18, 'Steak Filet De Boeuf', 9000, 'filet-de-boeuf-sauce-forestiere.jpg', 'Menu Viande BBQ'),
(19, 'Poulet Texan Demi', 4000, 'poulet_texan.jpeg', 'Menu Viande BBQ'),
(20, 'Poulet Texan Entier', 7000, 'poulet_texan.jpeg', 'Menu Viande BBQ'),
(21, 'Cotes De Porc', 7000, 'cote_porc.jpg', 'Menu Viande BBQ'),
(22, 'Ribs O Ribs', 9000, 'ribs.jpg', 'Menu Viande BBQ'),
(23, 'Boeuf-Poulet', 30000, 'boeuf_poulet.jpg', 'Menu Mix Grill'),
(24, 'Boeuf-Poulet-Porc', 45000, 'boeuf_poulet_porc.jpg', 'Menu Mix Grill'),
(25, 'Boeuf-Poulet-Porc-Gambas', 60000, 'gambas-grillees-640.jpg', 'Menu Mix Grill'),
(26, 'Burger Grand Canyos', 8000, 'burger_canyos.jpeg', 'Menu Burgers'),
(27, 'Burger Juicy Simple', 4000, 'b_juicy.jpg', 'Menu Burgers'),
(28, 'Burger Juicy Double', 10000, 'b_juicy.jpg', 'Menu Burgers'),
(29, 'Burger Cheese', 4000, 'b_cheese.jpg', 'Menu Burgers'),
(30, 'Burger Crunchy Simple', 4000, 'b_crunchy.jpg', 'Menu Burgers'),
(31, 'Burger Crunchy Double', 9000, 'b_crunchy.jpg', 'Menu Burgers'),
(32, 'Brochettes De Boeuf', 1500, 'broch_boeuf.jpg', 'Menu Brochettes'),
(33, 'Brochettes De Poulet', 1500, 'broch_poulet.jpeg', 'Menu Brochettes'),
(34, 'Alloco', 1000, 'alloco.jpeg', 'Accompagnement'),
(35, 'Attieke', 500, 'attieke.jpeg', 'Accompagnement'),
(36, 'Frites', 1000, 'frites.jpeg', 'Accompagnement'),
(37, 'Salade', 2000, 'salade.jpeg', 'Accompagnement'),
(38, 'Tagliatelles', 2000, 'tagliatelle.jpeg', 'Accompagnement'),
(39, 'O Kiosque', 10000, 'okiosque.jpeg', 'Menu Saisonnier'),
(40, 'Frites Fromages Boeuf ou Poulet', 10000, 'frite_fromage_boeuf_poulet.jpg', 'Menu Saisonnier'),
(41, 'Surf N\'Turf', 13000, 'surf.jpg', 'Menu Saisonnier'),
(42, 'Dirty Burger', 12000, 'dirtyburger.jpg', 'Menu Saisonnier'),
(43, 'Steak Tagliatelles', 10000, 'steak_tagliatelle.jpg', 'Menu Saisonnier'),
(44, 'Gambas Tagiatelles', 12000, 'tagliatelles-aux-gambas-001.jpg', 'Menu Saisonnier'),
(45, 'Gambas', 12000, 'gambas-grillees-640.jpg', 'Menu Saisonnier'),
(46, 'porc', 5555, 'boeuf_poulet_porc_gambas.png', 'Menu Brochettes');

-- --------------------------------------------------------

--
-- Structure de la table `mois_correspondance`
--

CREATE TABLE `mois_correspondance` (
  `mois_anglais` varchar(10) NOT NULL,
  `mois_francais` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `mois_correspondance`
--

INSERT INTO `mois_correspondance` (`mois_anglais`, `mois_francais`) VALUES
('January', 'Janvier'),
('February', 'Février'),
('March', 'Mars'),
('April', 'Avril'),
('May', 'Mai'),
('June', 'Juin'),
('July', 'Juillet'),
('August', 'Août'),
('September', 'Septembre'),
('October', 'Octobre'),
('November', 'Novembre'),
('December', 'Décembre');

-- --------------------------------------------------------

--
-- Structure de la table `tables_restaurant`
--

CREATE TABLE `tables_restaurant` (
  `id_table` int NOT NULL,
  `numero_table` int NOT NULL,
  `nombre_place` int NOT NULL,
  `occupe` tinyint(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `tables_restaurant`
--

INSERT INTO `tables_restaurant` (`id_table`, `numero_table`, `nombre_place`, `occupe`) VALUES
(2, 1, 2, 0),
(3, 2, 5, 0),
(7, 3, 6, 0),
(8, 4, 8, 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `commande`
--
ALTER TABLE `commande`
  ADD PRIMARY KEY (`id_commande`);

--
-- Index pour la table `employe`
--
ALTER TABLE `employe`
  ADD PRIMARY KEY (`id_employe`);

--
-- Index pour la table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id_menu`);

--
-- Index pour la table `mois_correspondance`
--
ALTER TABLE `mois_correspondance`
  ADD PRIMARY KEY (`mois_anglais`);

--
-- Index pour la table `tables_restaurant`
--
ALTER TABLE `tables_restaurant`
  ADD PRIMARY KEY (`id_table`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `commande`
--
ALTER TABLE `commande`
  MODIFY `id_commande` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT pour la table `employe`
--
ALTER TABLE `employe`
  MODIFY `id_employe` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `menu`
--
ALTER TABLE `menu`
  MODIFY `id_menu` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT pour la table `tables_restaurant`
--
ALTER TABLE `tables_restaurant`
  MODIFY `id_table` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
