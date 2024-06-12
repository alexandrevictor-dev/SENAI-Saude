-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12/06/2024 às 17:44
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `senai_saude`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `consulta`
--

CREATE TABLE `consulta` (
  `ID` int(11) NOT NULL,
  `COD_CONSULTA` char(7) NOT NULL,
  `DT_CONSULTA` date NOT NULL,
  `HR_CONSULTA` time NOT NULL,
  `VR_CONSULTA` decimal(6,2) NOT NULL,
  `ID_MEDICO` int(11) NOT NULL,
  `ID_PACIENTE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `consulta`
--

INSERT INTO `consulta` (`ID`, `COD_CONSULTA`, `DT_CONSULTA`, `HR_CONSULTA`, `VR_CONSULTA`, `ID_MEDICO`, `ID_PACIENTE`) VALUES
(30, 'CLIN001', '2024-06-10', '09:00:00', 150.00, 51, 2),
(31, 'ORTO001', '2024-06-10', '09:30:00', 200.00, 53, 5),
(32, 'CARD001', '2024-06-10', '10:15:00', 160.00, 54, 3),
(33, 'PSIQ001', '2024-06-10', '11:00:00', 90.00, 55, 4),
(34, 'OUTR001', '2024-06-10', '11:45:00', 120.00, 51, 1),
(35, 'CLIN002', '2024-07-11', '12:30:00', 50.00, 51, 6),
(36, 'ORTO002', '2024-07-11', '13:15:00', 140.00, 53, 1),
(37, 'CARD002', '2024-08-12', '14:00:00', 150.00, 54, 4),
(38, 'CLIN003', '2024-08-12', '14:45:00', 200.00, 51, 7),
(39, 'ORTO003', '2024-09-13', '15:30:00', 450.00, 53, 9),
(40, 'CARD003', '2024-09-13', '16:15:00', 320.00, 54, 5),
(41, 'PSIQ002', '2024-10-14', '16:00:00', 210.00, 55, 4),
(42, 'PEDI001', '2024-10-14', '13:45:00', 110.00, 52, 10),
(43, 'CLIN004', '2024-11-15', '10:00:00', 100.00, 51, 9),
(44, 'CARD004', '2024-11-15', '09:00:00', 150.00, 54, 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `medico`
--

CREATE TABLE `medico` (
  `ID` int(11) NOT NULL,
  `CPF` char(11) NOT NULL,
  `RG` varchar(9) NOT NULL,
  `NOME` varchar(60) NOT NULL,
  `ENDERECO` varchar(200) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `CEP` varchar(8) NOT NULL,
  `CRM` char(9) NOT NULL,
  `ESP_MEDICA` int(11) NOT NULL,
  `DT_NASC` date NOT NULL,
  `DT_ADMISSAO` date NOT NULL,
  `DT_DESLIGAMENTO` date DEFAULT NULL,
  `STATUS_MEDICO` varchar(7) GENERATED ALWAYS AS (case when coalesce(`DT_DESLIGAMENTO`,'0000-00-00') = '0000-00-00' then 'Ativo' else 'Inativo' end) VIRTUAL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `medico`
--

INSERT INTO `medico` (`ID`, `CPF`, `RG`, `NOME`, `ENDERECO`, `EMAIL`, `CEP`, `CRM`, `ESP_MEDICA`, `DT_NASC`, `DT_ADMISSAO`, `DT_DESLIGAMENTO`) VALUES
(51, '12345678901', '123456789', 'Dr. João Almeida', 'Rua das Acácias, 123 - Centro', 'joao.almeida@hospital.com', '12345000', 'CRM001', 1, '1970-05-10', '2000-01-15', NULL),
(52, '23456789012', '234567890', 'Dra. Ana Santos', 'Avenida Paulista, 456 - Bela Vista', 'ana.santos@hospital.com', '12346000', 'CRM002', 2, '1980-06-20', '2005-03-20', NULL),
(53, '34567890123', '345678901', 'Dr. Carlos Pereira', 'Rua das Flores, 789 - Jardim das Rosas', 'carlos.pereira@hospital.com', '12347000', 'CRM003', 3, '1990-07-30', '2010-05-10', NULL),
(54, '45678901234', '456789012', 'Dra. Fernanda Oliveira', 'Avenida Brasil, 101 - Zona Sul', 'fernanda.oliveira@hospital.com', '12348000', 'CRM004', 4, '1985-08-15', '2012-11-25', NULL),
(55, '56789012345', '567890123', 'Dr. Ricardo Mendes', 'Rua das Palmeiras, 202 - Alto da Boa Vista', 'ricardo.mendes@hospital.com', '12349000', 'CRM005', 5, '1975-09-25', '1999-09-01', NULL),
(56, '67890123456', '678901234', 'Dra. Mariana Lopes', 'Rua do Catete, 303 - Flamengo', 'mariana.lopes@hospital.com', '12350000', 'CRM006', 6, '1988-10-30', '2015-02-14', '2019-08-01'),
(57, '78901234567', '789012345', 'Dr. Pedro Henrique', 'Avenida Atlântica, 404 - Copacabana', 'pedro.henrique@hospital.com', '12351000', 'CRM007', 1, '1982-11-10', '2008-07-20', '2021-05-10'),
(58, '89012345678', '890123456', 'Dra. Gabriela Santos', 'Rua São Clemente, 505 - Botafogo', 'gabriela.santos@hospital.com', '12352000', 'CRM008', 2, '1978-12-15', '2003-10-05', '2020-01-01'),
(59, '90123456789', '901234567', 'Dr. Lucas Rocha', 'Rua da Lapa, 606 - Lapa', 'lucas.rocha@hospital.com', '12353000', 'CRM009', 3, '1984-01-20', '2011-06-18', NULL),
(60, '01234567890', '012345678', 'Dra. Camila Almeida', 'Rua das Camélias, 707 - Barra da Tijuca', 'camila.almeida@hospital.com', '12354000', 'CRM010', 4, '1992-02-28', '2018-08-22', NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `paciente`
--

CREATE TABLE `paciente` (
  `ID` int(11) NOT NULL,
  `CPF` char(11) NOT NULL,
  `RG` varchar(9) NOT NULL,
  `NOME` varchar(60) NOT NULL,
  `ENDERECO` varchar(200) NOT NULL,
  `CEP` char(8) NOT NULL,
  `DT_NASC` date NOT NULL,
  `GENERO` int(1) NOT NULL,
  `TELEFONE` varchar(11) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `RESPONSAVEL` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `paciente`
--

INSERT INTO `paciente` (`ID`, `CPF`, `RG`, `NOME`, `ENDERECO`, `CEP`, `DT_NASC`, `GENERO`, `TELEFONE`, `EMAIL`, `RESPONSAVEL`) VALUES
(1, '14578965325', '687544426', 'Maria de Souza', 'Av. Dr.Nilo Peçanha, 307-Centro', '24445300', '2001-03-20', 2, '21986697541', 'mariasouza22@gmail.com', 'não'),
(2, '25478965124', '787655533', 'Ana Pereira', 'Rua das Flores, 123 - Jardim das Rosas', '24445500', '1985-05-14', 2, '21987654321', 'anapereira85@gmail.com', 'não'),
(3, '36587965236', '887766644', 'Carlos Eduardo', 'Rua das Palmeiras, 456 - Alto da Boa Vista', '24445600', '1978-03-05', 1, '21986543210', 'carlosedu78@gmail.com', 'não'),
(4, '47896534785', '987877755', 'Mariana Lopes', 'Av. Brasil, 789 - Zona Sul', '24445700', '1992-08-12', 2, '21985432109', 'marianalopes92@gmail.com', 'não'),
(5, '58967432189', '108988866', 'Pedro Henrique', 'Rua dos Coqueiros, 101 - Barra da Tijuca', '24445800', '1988-02-20', 1, '21984321098', 'pedrohenrique88@gmail.com', 'não'),
(6, '69874513247', '119099977', 'Fernanda Oliveira', 'Av. Atlântica, 202 - Copacabana', '24445900', '1994-07-18', 2, '21983210987', 'fernandaoliveira94@gmail.com', 'não'),
(7, '78965421356', '129111088', 'Ricardo Mendes', 'Rua do Catete, 303 - Flamengo', '24446000', '1982-12-30', 1, '21982109876', 'ricardomendes82@gmail.com', 'não'),
(8, '89654213467', '139122199', 'Gabriela Santos', 'Av. Presidente Vargas, 404 - Centro', '24446100', '1989-09-25', 2, '21981098765', 'gabrielasantos89@gmail.com', 'não'),
(9, '97865421378', '149133210', 'Lucas Rocha', 'Rua da Lapa, 505 - Lapa', '24446200', '1996-06-15', 3, '21980987654', 'lucasrocha96@gmail.com', 'não'),
(10, '10654321239', '159144321', 'Camila Almeida', 'Rua São Clemente, 606 - Botafogo', '24446300', '2016-04-22', 2, '21979876543', 'camilaalmeida87@gmail.com', 'Ana Paula'),
(11, '19090191091', '919100019', 'Maria dos Testes em Python', 'Rua Dr.Alberto Torres, 555', '24910190', '1990-09-09', 2, '21991019001', 'mariadopython@outlook.com', NULL),
(12, '91001991010', '910011190', 'Jose do Python', 'Av. Dr Alberto Torres, 555', '90019909', '1990-09-09', 3, '21990111990', 'josefinodopython@outlook.com', NULL),
(13, '19019019019', '190190190', 'Mariana Pythiana', 'Av. Pythones, 776', '24901901', '2002-09-09', 4, '21919011901', 'marianapythiana@hotmail.com', 'Ana Rosalia Pythiana');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_MEDICO` (`ID_MEDICO`),
  ADD KEY `FK_PACIENTE` (`ID_PACIENTE`);

--
-- Índices de tabela `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`ID`);

--
-- Índices de tabela `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `consulta`
--
ALTER TABLE `consulta`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de tabela `medico`
--
ALTER TABLE `medico`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `paciente`
--
ALTER TABLE `paciente`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `FK_MEDICO` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`ID`),
  ADD CONSTRAINT `FK_PACIENTE` FOREIGN KEY (`ID_PACIENTE`) REFERENCES `paciente` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
