#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/SonarSource/sonarqube/blob/138171d657c57fe015c4dcc4be996973f87f5365/server/sonar-server/src/main/java/org/sonar/server/authentication/CredentialsLocalAuthentication.java#L159
"""
private static final class Sha1Function implements HashFunction {
@Override
public AuthenticationResult checkCredentials(UserDto user, String password) {
  if (user.getCryptedPassword() == null) {
    return new AuthenticationResult(false, "null password in DB");
  }
  if (user.getSalt() == null) {
    return new AuthenticationResult(false, "null salt");
  }
  if (!user.getCryptedPassword().equals(hash(user.getSalt(), password))) {
    return new AuthenticationResult(false, "wrong password");
  }
  return new AuthenticationResult(true, "");
}

private static String hash(String salt, String password) {
  return DigestUtils.sha1Hex("--" + salt + "--" + password + "--");
}
"""


import hashlib


def hash(salt, password):
    """calc sonar crypted_password
    """

    return hashlib.new(
        'sha1',
        bytes(f"--{salt}--{password}--", 'utf-8')
    ).hexdigest()



if __name__ == '__main__':
    # admin: admin

    password = 'admin'
    salt = '6522f3c5007ae910ad690bb1bdbf264a34884c6d'
    crypted_password = '88c991e39bb88b94178123a849606905ebf440f5'

    if crypted_password == hash(salt, password):
        print(f"{password} -> hash algorithm-> {crypted_password}")


# references
# https://stackoverflow.com/questions/18209054/how-to-recover-admin-password-for-sonar
# https://docs.sonarqube.org/latest/instance-administration/security/
# https://docs.sonarqube.org/7.4/setup/install-server/
# https://github.com/SonarSource/sonarqube/blob/2b0f05f4442cb3e3b9c798adf9d93f64e19a6b01/server/sonar-db-migration/src/test/resources/org/sonar/server/platform/db/migration/version/v62/AddIsRootColumnOnTableUsersTest/table_users.sql
# https://github.com/SonarSource/sonarqube/blob/138171d657c57fe015c4dcc4be996973f87f5365/server/sonar-db-migration/src/main/java/org/sonar/server/platform/db/migration/version/v72/IncreaseCryptedPasswordSize.java
# https://stackoverflow.com/questions/2898685/hashing-in-sha512-using-a-salt-python
# https://github.com/SonarSource/sonarqube/blob/138171d657c57fe015c4dcc4be996973f87f5365/server/sonar-db-migration/src/test/java/org/sonar/server/platform/db/migration/version/v72/PopulateHashMethodOnUsersTest.java#L57
# https://github.com/SonarSource/sonarqube/blob/138171d657c57fe015c4dcc4be996973f87f5365/server/sonar-server/src/main/java/org/sonar/server/user/NewUser.java#L127
# https://github.com/SonarSource/sonarqube/blob/138171d657c57fe015c4dcc4be996973f87f5365/server/sonar-db-dao/src/main/java/org/sonar/db/user/UserDto.java#L48
# https://github.com/SonarSource/sonarqube/blob/138171d657c57fe015c4dcc4be996973f87f5365/server/sonar-server/src/main/java/org/sonar/server/authentication/CredentialsLocalAuthentication.java#L159
