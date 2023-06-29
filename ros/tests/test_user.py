from ros import Ros, UserModule
from ros.user import User, UserAAA, UserActive, UserGroup, UserSettings, UserSSHKey


class TestUser:
    def test_user(self, ros: Ros):
        assert isinstance(ros.user, UserModule)

    def test_get_user(self, ros: Ros):
        for i in ros.user():
            assert isinstance(i, User)


class TestUserAAA:
    def test_user_aaa(self, ros: Ros):
        assert isinstance(ros.user.aaa(), UserAAA)


class TestUserActive:
    def test_user_active(self, ros: Ros):
        for i in ros.user.active():
            assert isinstance(i, UserActive)


class TestUserGroup:
    def test_user_group(self, ros: Ros):
        for i in ros.user.group():
            assert isinstance(i, UserGroup)


class TestUserSettings:
    def test_user_settings(self, ros: Ros):
        assert isinstance(ros.user.settings(), UserSettings)


class TestUserSSHKey:
    def test_ssh_keys(self, ros: Ros):
        for i in ros.user.ssh_keys():
            assert isinstance(i, UserSSHKey)
