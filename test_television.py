import unittest
from television import Television


class TestTelevision(unittest.TestCase):

    def test_default(self) -> None:
        tv = Television()
        self.assertEqual(str(tv), "Power = False, Channel = 0, Volume = 0")

    def test_power(self) -> None:
        tv = Television()
        tv.power()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 0")

    def test_channel_up(self) -> None:
        tv = Television()
        tv.power()
        tv.channel_up()
        self.assertEqual(str(tv), "Power = True, Channel = 1, Volume = 0")

    def test_channel_wrap(self) -> None:
        tv = Television()
        tv.power()
        tv.channel_down()
        self.assertEqual(str(tv), "Power = True, Channel = 3, Volume = 0")

    def test_volume_up(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 1")

    def test_volume_limit(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_up()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 2")

    def test_mute(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 0")

    def test_unmute_with_volume(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_up()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 2")
    
    def test_channel_down(self) -> None:
        tv = Television()
        tv.power()
        tv.channel_down()
        self.assertEqual(str(tv), "Power = True, Channel = 3, Volume = 0")


    def test_channel_down_when_off(self) -> None:
        tv = Television()
        tv.channel_down()
        self.assertEqual(str(tv), "Power = False, Channel = 0, Volume = 0")


    def test_volume_down(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_down()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 0")


    def test_volume_down_when_off(self) -> None:
        tv = Television()
        tv.volume_down()
        self.assertEqual(str(tv), "Power = False, Channel = 0, Volume = 0")


    def test_mute_toggle(self) -> None:
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.mute()
        self.assertEqual(str(tv), "Power = True, Channel = 0, Volume = 1")


    def test_channel_up_when_off(self) -> None:
        tv = Television()
        tv.channel_up()
        self.assertEqual(str(tv), "Power = False, Channel = 0, Volume = 0")


if __name__ == "__main__":
    unittest.main()