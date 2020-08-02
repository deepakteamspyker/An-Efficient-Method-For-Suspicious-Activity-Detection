import os
import cv2


def convert_frames_to_video(input_list, output_file_name, fps, size):

    out = cv2.VideoWriter(output_file_name, fourcc, fps, size)
    num_frames = len(input_list)

    for i in range(num_frames):
        base_name = 'img'
        img_name = base_name + '_{:06d}'.format(i) + '.jpg'
        img_path = os.path.join(input_frame_path, img_name)

        try:
            img = cv2.imread(img_path)
            out.write(img)
        except:
            print(img_name + ' does not exist')

        if img is not None:
            cv2.imshow('img',img)
            cv2.waitKey(1)

    out.release()
    cv2.destroyAllWindows()
    print("The output video is {} is saved".format(output_file_name))


if __name__ == '__main__':

    path = os.getcwd()
    data_dir = 'DATA'
    data_subdir = 'New folder'
    output_vid_dir = 'output_video'

    if not os.path.exists(output_vid_dir):
        os.mkdir(output_vid_dir)

    input_frame_path = os.path.join(path, data_dir, data_subdir)

    img_list = os.listdir('F:/DATA/New folder/')

    frame = cv2.imread('F:/DATA/New folder/1.jpg')
    height, width, channels = frame.shape
    fps = 25
    output_file_name = 'F:/DATA/output_video/{0}_{1}fps.mp4'.format(data_subdir, fps)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    size = (width, height)
    convert_frames_to_video(img_list, output_file_name, fps, size)

