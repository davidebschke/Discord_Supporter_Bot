import unittest

from tests.utils.test_embedded_messages import Test_embedded_welcome_messages
from tests.groupFeatures.test_tree_commands import Test_tree_commands
from tests.groupFeatures.test_member_join_system import Test_member_join_system
from tests.utils.test_load_jokes import Test_loadJokes
from tests.utils.test_load_settings import Test_load_settings


def run_suite():

    """
    Startet alle Tests im Projekt und gibt den Statuscode zurück.
    """
    suite = unittest.TestSuite()
    suite.addTests(Test_embedded_welcome_messages)
    suite.addTests(Test_tree_commands)
    suite.addTests(Test_member_join_system)
    suite.addTests(Test_loadJokes)
    suite.addTests(Test_load_settings)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_suite()