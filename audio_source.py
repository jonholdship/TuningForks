import sounddevice as sd
import discord

DEFAULT = 0
sd.default.channels = 2
sd.default.dtype = "int16"
sd.default.latency = "high"
sd.default.samplerate = 48000


class PCMStream(discord.AudioSource):
    def __init__(self):
        discord.AudioSource.__init__(self)
        self.device = self.prepare_cable()
        self.frames = int(sd.default.samplerate / 50)
        self.stream = sd.RawInputStream(device=self.device, blocksize=self.frames)

        self.stream.start()

    def read(self):
        if self.stream is None:
            return

        data = self.stream.read(self.frames)[0]
        return bytes(data)

    def change_device(self, num):
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()
        self.stream = sd.RawInputStream(device=num)
        self.stream.start()

    def prepare_cable(self):
        device_list = sd.query_devices()
        cable_list = [x for x in device_list if "VoiceMeeter Output" in x["name"]]
        try:
            device = cable_list[0]
        except:
            raise ValueError("missing device")
        return device["index"]


class DeviceNotFoundError(Exception):
    def __init__(self):
        self.devices = sd.query_devices()
        self.host_apis = sd.query_hostapis()
        super().__init__("No Devices Found")

    def __str__(self):
        return (
            f"Devices \n"
            f"{self.devices} \n "
            f"Host APIs \n"
            f"{pformat(self.host_apis)}"
        )


def query_devices():
    options = {
        device.get("name"): index
        for index, device in enumerate(sd.query_devices())
        if (device.get("max_input_channels") > 0 and device.get("hostapi") == DEFAULT)
    }

    if not options:
        raise DeviceNotFoundError()

    return
