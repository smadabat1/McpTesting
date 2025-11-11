import pynautobot

nautobot = pynautobot.api(
    url="https://10.130.106.50/",
    token="cb8f0c3be8ade9cdb4142b7d4c24d079d77def67"
)

devices = nautobot.wireless.models()
print(devices)