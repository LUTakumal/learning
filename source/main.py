from source.models.vr_device import VrDevice


def main():
    vr_device = VrDevice()
    vr_device.render_width = 100
    vr_device.render_height = 200
    vr_device.display()
    vr_device.init_vr_device()


if __name__ == "__main__":
    main()
