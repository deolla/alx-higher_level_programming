-- Script: Convert specified elements to UTF8 in MySQL server

-- Task: Convert database hbtn_0c_0 to UTF8
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Task: Convert table first_table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Task: Convert field name in table first_table to UTF8
ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
