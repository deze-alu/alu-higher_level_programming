-- Creates the user user_0d_1 with all the privileges on the MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Drops the dynamic privileges that only recent MySQL releases register
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
       GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
       SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN
    ON *.* FROM 'user_0d_1'@'localhost';
