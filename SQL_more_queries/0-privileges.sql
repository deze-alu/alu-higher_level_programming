-- Drops the dynamic privileges that only recent MySQL releases register
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
       GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
       SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN
    ON *.* FROM 'user_0d_1'@'localhost';
-- Lists all the privileges of the MySQL user user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Drops the same recent dynamic privileges for the second user
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
       GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
       SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN
    ON *.* FROM 'user_0d_2'@'localhost';
-- Lists all the privileges of the MySQL user user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
