-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2024 a las 21:46:00
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_programacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `privacidad` enum('publica','privada','secreta') NOT NULL DEFAULT 'publica',
  `fecha_creacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `grupos`
--

INSERT INTO `grupos` (`id`, `nombre`, `descripcion`, `privacidad`, `fecha_creacion`) VALUES
(1, 'SSSSS', 'ZZZ', 'publica', '2024-11-18 19:03:46');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfiles`
--

CREATE TABLE `perfiles` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `genero` enum('Masculino','Femenino','Otro') NOT NULL,
  `correo_electronico` varchar(100) NOT NULL,
  `contrasena` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `perfiles`
--

INSERT INTO `perfiles` (`id`, `nombre`, `apellido`, `fecha_nacimiento`, `genero`, `correo_electronico`, `contrasena`) VALUES
(1, 'Juan', 'Guzman', '0000-00-00', 'Masculino', 'juan123@gmail.com', '123456'),
(2, 'AilaT ', 'Montes', '0000-00-00', 'Femenino', 'montes123@gmail.com', '1234567'),
(3, 'David', 'Perez', '2004-05-23', '', 'david123@gmail.com', '123456'),
(4, 'Laura', 'Gutierrez', '0000-00-00', 'Femenino', 'laura@gmail.com', '1234'),
(5, 'Yaaser', 'Coca', '2000-03-24', 'Femenino', 'yaaser123@gmail.com', '$2b$12$dotyu.5bDMTHKc7GFjk2z.so316zsR77b17hR4/QXgx5b595RxoOm'),
(6, 'John', 'Connor', '1900-05-24', 'Masculino', 'john123@gmail.com', '$2b$12$2KHgNQ6zhKzHUtgMB/N.ae0CXFL0Cd4pXPmCatOPzsthM27LOp60W'),
(7, 'Juan David', 'Guzman', '2004-04-26', 'Masculino', 'juanda123@gmail.com', '$2b$12$u9EvcFINNfOMcwaYkltSF.5Zxx3H2Nh3KHJON.SbV0gNV0W5Qbu.K'),
(8, 'Juan Da', 'Guzman', '2000-03-12', 'Masculino', 'juan1234@gmail.com', '$2b$12$fBnRGd3Cew01RpOKWpVuY.Fe.B2jmxfSqMHejfkfSL1wDmum21Lj.'),
(9, 'Saul', 'Ramos', '2000-06-11', 'Masculino', 'saul123@gmail.com', '$2b$12$f6Z4FisjnEeAcofCRZeXSuz1uxE0VIKI75/EKbvg7Tmgz0HrqO.hm'),
(10, 'Brayan', 'Rosales', '2004-05-24', 'Masculino', 'rosales123@gmail.com', '$2b$12$wxPnopt199pjSRfpNW9lh.UNhj5PD6pG0w/9U/OuD4VVpUf4nMHnu'),
(12, 'admin', '123', '2004-02-25', 'Masculino', 'admin@gmail.com', '$2b$12$oKAyvt1MYBJ0AwklCNjKiOvB0IsRR8ye2ufxxlp/WXYlgzG/f7k1m'),
(13, 'admin', '123', '2005-10-22', 'Masculino', 'admin1@gmail.com', '$2b$12$pFo0v8m9tVlnjAM1iDVRw.dlWW7F7r1sqBp.ZU6OXPF5YTkH3iTJW');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicaciones`
--

CREATE TABLE `publicaciones` (
  `id` int(11) NOT NULL,
  `id_perfil` int(11) NOT NULL,
  `contenido` text NOT NULL,
  `fecha_creacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `publicaciones`
--

INSERT INTO `publicaciones` (`id`, `id_perfil`, `contenido`, `fecha_creacion`) VALUES
(1, 1, 'Noticias', '2024-11-18 17:29:12'),
(2, 1, 'buenas', '2024-11-18 23:22:44');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `perfiles`
--
ALTER TABLE `perfiles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo_electronico` (`correo_electronico`);

--
-- Indices de la tabla `publicaciones`
--
ALTER TABLE `publicaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_perfil` (`id_perfil`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `grupos`
--
ALTER TABLE `grupos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `perfiles`
--
ALTER TABLE `perfiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `publicaciones`
--
ALTER TABLE `publicaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `publicaciones`
--
ALTER TABLE `publicaciones`
  ADD CONSTRAINT `publicaciones_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `perfiles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
