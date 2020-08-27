-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 27 Ağu 2020, 19:06:38
-- Sunucu sürümü: 5.7.31
-- PHP Sürümü: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `sinema`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `aksiyon`
--

DROP TABLE IF EXISTS `aksiyon`;
CREATE TABLE IF NOT EXISTS `aksiyon` (
  `yil17` int(11) NOT NULL,
  `yil18` int(11) NOT NULL,
  `yil19` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `drama`
--

DROP TABLE IF EXISTS `drama`;
CREATE TABLE IF NOT EXISTS `drama` (
  `yil17` int(11) NOT NULL,
  `yil18` int(11) NOT NULL,
  `yil19` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `komedi`
--

DROP TABLE IF EXISTS `komedi`;
CREATE TABLE IF NOT EXISTS `komedi` (
  `yil17` int(11) NOT NULL,
  `yil18` int(11) NOT NULL,
  `yil19` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `korku`
--

DROP TABLE IF EXISTS `korku`;
CREATE TABLE IF NOT EXISTS `korku` (
  `yil17` int(11) NOT NULL,
  `yil18` int(11) NOT NULL,
  `yil19` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
