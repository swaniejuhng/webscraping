from twitter import *

t = Twitter(auth = OAuth("700964843486998528-u0J6aLyTNBR10PWbBnjEtGwz6SBd2SN", "NPwcXF3sddMjeeeukn4kuECxHEb1BwP22BgdfuJfF2yTg", "0WLZmqBe80LLQf6VlOcRG9HLH", "LzaIoRQul3Cf0aV5rMhH60qSuoHrXGBt1dbsDPta7Cl53ZqXeH"))
statusUpdate = t.statuses.update(status = 'Hello, world!')
print(statusUpdate)
