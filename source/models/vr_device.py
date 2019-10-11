import openvr
import sys
import time


class VrDevice:
    def __init__(self):
        """hmd = head mounting device"""
        self.hmd = None
        self.vr_render_models = None
        self.render_width = 0
        self.render_height = 0

    def display(self):
        print("Render Height: ", self.render_height)
        print("Render Width: ", self.render_width)

    def init_vr_device(self):
        try:
            self.hmd = openvr.init(openvr.VRApplication_Scene)
            #self.vr_render_models = openvr.getGenericInterface(openvr.IVRRenderModels_Version)
            poses = []  # will be populated with proper type after first call
            for i in range(100):
                poses, _ = openvr.VRCompositor().waitGetPoses(poses, None)
                hmd_pose = poses[openvr.k_unTrackedDeviceIndex_Hmd]
                print(hmd_pose.mDeviceToAbsoluteTracking)
                sys.stdout.flush()
                time.sleep(0.2)
            openvr.shutdown()
        except openvr.error_code.InitError_Init_HmdNotFound:
            print("VR Device not found")
