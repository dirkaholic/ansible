# -*- coding: utf-8 -*-

from ansible.modules.database.mysql import mysql_user
from units.compat.mock import patch
from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args


class TestMySQLUserModule(ModuleTestCase):
    def setUp(self):
        super(TestMySQLUserModule, self).setUp()
        self.module = mysql_user

    def tearDown(self):
        super(TestMySQLUserModule, self).tearDown()

    def test_non_hash_password_is_no_hash(self):
        password = "Test42"
        result = self.module.is_hash(password)
        assert result == False

    def test_hash_password_is_hash(self):
        password = "*42434304F38173D0FC396F60C077C662FE6EE7DD"
        result = self.module.is_hash(password)
        assert result == True

    