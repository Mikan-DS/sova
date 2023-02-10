
-- Месяца
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('1', 'Январь');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('2', 'Февраль');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('3', 'Март');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('4', 'Апрель');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('5', 'Май');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('6', 'Июнь');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('7', 'Июль');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('8', 'Август');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('9', 'Сентябрь');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('10', 'Октябрь');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('11', 'Ноябрь');
INSERT INTO `sova`.`events_month` (`id`, `title`) VALUES ('12', 'Декабрь');


-- Типы
INSERT INTO `sova`.`events_eventtype` (`id`, `title`) VALUES ('1', 'Квест');
INSERT INTO `sova`.`events_eventtype` (`id`, `title`) VALUES ('2', 'Квиз');
INSERT INTO `sova`.`events_eventtype` (`id`, `title`) VALUES ('3', 'Олимпиада');
INSERT INTO `sova`.`events_eventtype` (`id`, `title`) VALUES ('4', 'Мастер-класс');
INSERT INTO `sova`.`events_eventtype` (`id`, `title`) VALUES ('5', 'Субботник');

-- Уровни
INSERT INTO `sova`.`events_eventlevel` (`title`) VALUES ('Колледж');
INSERT INTO `sova`.`events_eventlevel` (`title`) VALUES ('Город');
INSERT INTO `sova`.`events_eventlevel` (`title`) VALUES ('Республика');
INSERT INTO `sova`.`events_eventlevel` (`title`) VALUES ('Регион');
INSERT INTO `sova`.`events_eventlevel` (`title`) VALUES ('Федерация');
INSERT INTO `sova`.`events_eventlevel` (`title`) VALUES ('Международный');


-- Для админки
INSERT INTO `sova`.`auth_user` (`id`, `password`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES ('1', 'pbkdf2_sha256$390000$GPj81dO58psMKiQFMNyeeP$otIp3iFN3dReYDPURyrXz7fdSH7fds3C7d9xu2qRwnM=', '1', 'mikan', '', '', '', '1', '1', '2023-02-10 15:28:56.508918');
