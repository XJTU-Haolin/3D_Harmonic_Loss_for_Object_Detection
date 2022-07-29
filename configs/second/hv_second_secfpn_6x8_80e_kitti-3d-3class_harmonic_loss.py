_base_ = [
    '../_base_/models/hv_second_secfpn_kitti_harmonic_loss.py',
    '../_base_/datasets/kitti-3d-3class.py',
    '../_base_/schedules/cyclic_40e.py', '../_base_/default_runtime.py'
]

# load_from = './work_dirs/point_rcnn_2x8_kitti-3d-3classes/epoch_14.pth'
# resume_from = './work_dirs/point_rcnn_2x8_kitti-3d-3classes/epoch_14.pth'
