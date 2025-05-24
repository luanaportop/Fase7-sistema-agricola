-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Sensores'
-- 
-- ---

DROP TABLE IF EXISTS `Sensores`;
		
CREATE TABLE `Sensores` (
  `id_sensor` INTEGER NOT NULL AUTO_INCREMENT,
  `tipo_sensor` VARCHAR(50) NOT NULL,
  `data_instalacao` DATETIME NOT NULL,
  PRIMARY KEY (`id_sensor`)
);

-- ---
-- Table 'Leitura_Sensor'
-- 
-- ---

DROP TABLE IF EXISTS `Leitura_Sensor`;
		
CREATE TABLE `Leitura_Sensor` (
  `id_leitura` INTEGER NOT NULL AUTO_INCREMENT,
  `id_sensor` INTEGER NOT NULL,
  `data_hora` DATETIME NOT NULL,
  `result_sensor` DOUBLE NOT NULL,
  PRIMARY KEY (`id_leitura`)
);

-- ---
-- Table 'Cultura'
-- 
-- ---

DROP TABLE IF EXISTS `Cultura`;
		
CREATE TABLE `Cultura` (
  `id_cultura` INTEGER NOT NULL AUTO_INCREMENT,
  `nome_cultura` VARCHAR(100) NOT NULL,
  `data_plantio` DATETIME NOT NULL,
  `area_plantio` DOUBLE NOT NULL,
  PRIMARY KEY (`id_cultura`)
);

-- ---
-- Table 'Irrigacao'
-- 
-- ---

DROP TABLE IF EXISTS `Irrigacao`;
		
CREATE TABLE `Irrigacao` (
  `id_cultura` INTEGER NOT NULL,
  `data_registro` DATETIME NOT NULL,
  `qtd_agua` DOUBLE NOT NULL,
  `id_irrigacao` INTEGER NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_irrigacao`)
);

-- ---
-- Table 'historico'
-- 
-- ---

DROP TABLE IF EXISTS `historico`;
		
CREATE TABLE `historico` (
  `id_historico` INTEGER NOT NULL AUTO_INCREMENT,
  `id_cultura` INTEGER NOT NULL,
  `data_plantio` DATE NOT NULL,
  `ultima_leitura_sensor` DOUBLE NOT NULL,
  `ultima_irrigacao` DATE NOT NULL,
  `total_agua_aplicada` DOUBLE NOT NULL,
  `qtd_nutrientes_aplicado` DOUBLE NOT NULL,
  `id_sensor` INTEGER NOT NULL DEFAULT NULL,
  PRIMARY KEY (`id_historico`)
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `Leitura_Sensor` ADD FOREIGN KEY (id_sensor) REFERENCES `Sensores` (`id_sensor`);
ALTER TABLE `Irrigacao` ADD FOREIGN KEY (id_cultura) REFERENCES `Cultura` (`id_cultura`);
ALTER TABLE `historico` ADD FOREIGN KEY (id_cultura) REFERENCES `Cultura` (`id_cultura`);
ALTER TABLE `historico` ADD FOREIGN KEY (id_sensor) REFERENCES `Sensores` (`id_sensor`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `Sensores` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Leitura_Sensor` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Cultura` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Irrigacao` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `historico` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `Sensores` (`id_sensor`,`tipo_sensor`,`data_instalacao`) VALUES
-- ('','','');
-- INSERT INTO `Leitura_Sensor` (`id_leitura`,`id_sensor`,`data_hora`,`result_sensor`) VALUES
-- ('','','','');
-- INSERT INTO `Cultura` (`id_cultura`,`nome_cultura`,`data_plantio`,`area_plantio`) VALUES
-- ('','','','');
-- INSERT INTO `Irrigacao` (`id_cultura`,`data_registro`,`qtd_agua`,`id_irrigacao`) VALUES
-- ('','','','');
-- INSERT INTO `historico` (`id_historico`,`id_cultura`,`data_plantio`,`ultima_leitura_sensor`,`ultima_irrigacao`,`total_agua_aplicada`,`qtd_nutrientes_aplicado`,`id_sensor`) VALUES
-- ('','','','','','','','');