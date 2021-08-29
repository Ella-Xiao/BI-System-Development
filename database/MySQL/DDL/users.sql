DELETE FROM `dev.daily_overall_data`

DROP TABLE IF EXISTS `dev.users`;
CREATE TABLE `dev.users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gender` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `height` json DEFAULT NULL,
  `weight` json DEFAULT NULL,
  `ideal_sleep_time` smallint(5) unsigned DEFAULT NULL,
  `total_sleep_time` smallint(5) unsigned DEFAULT NULL,
  `passed_questionnaire` tinyint(1) NOT NULL DEFAULT '0',
  `to_improve` json DEFAULT NULL,
  `allow_notifications` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
)



delete FROM `dev.users`;

INSERT INTO `dev.users` (`id`, `name`, `email`, `email_verified_at`, `password`, `gender`, `date_of_birth`, `height`, `weight`, `ideal_sleep_time`, `total_sleep_time`, `passed_questionnaire`, `to_improve`, `allow_notifications`, `created_at`, `updated_at`) VALUES
(110, 'testUser2', 'testUser2@gmail.com', NULL, '$2y$10$uIiRkIV/76lrs.eApvMuEuiHIxkqshK3WKUhVQHN0adtZXiXGgOPG','female', '1999-01-01', '{"unit": "cm", "value": 170}', '{"unit": "kg", "value": 65}', 500, 480, 1, '[\"sleep\", \"focus\", \"stress\"]', 0, '2021-07-06 14:44:16', '2021-07-06 14:45:26'),
(61, 'testUser1', 'testUser1@qwe.com', NULL, '$2y$10$uIiRkIV/76lrs.eApvMuEuiHIxkqshK3WKUhVQHN0adtZXiXGgOPG', 'male', '2000-02-01', '{\"unit\": \"cm\", \"value\": 146}', '{\"unit\": \"kg\", \"value\": 51}', 308, 430, 1, '[]', 0, '2021-06-18 20:25:17', '2021-07-15 09:30:11'),
(111, 'testUser3', 'testUser3@gmail.co', NULL, '$2y$10$AWOEp58iilK80poZTp9HuO0ZbcKfUYUKuosdBJeti6oxp7t5GV1x2', 'male', '1992-03-01', '{"unit": "cm", "value": 180}', '{"unit": "kg", "value": 75}', 420, 390, 1, '[\"sleep\", \"stress\"]', 0, '2021-07-06 20:49:33', '2021-07-14 22:47:58'),
(112, 'testUser1', 'testUser4@gmail.com', NULL, '$2y$10$8ax08ez4Nsvzt/DhzKazf.pjOR6kO19Jd5KYbw2ATeCLvxl.7C2cG', 'female', '1987-11-04', '{\"unit\": \"cm\", \"value\": 157.48}', '{\"unit\": \"kg\", \"value\": 51.255896}', 360, 240, 1, '[]', 0, '2021-07-07 18:22:37', '2021-07-10 15:19:55');

SELECT * FROM `dev.users`