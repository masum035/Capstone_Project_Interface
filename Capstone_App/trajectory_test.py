import cv2
import numpy as np
from scipy.optimize import curve_fit

centers = []
time = []
timeCount = 0

frame_height = 480
frame_width = 480

left_part = True
saving_directory = ''
final_video_dir = ''

area_points = []
tmp_area = 0


area = [420, 550, 624, 700, 783, 896, 1044, 1292, 1628, 1968, 2491, 3410, 4672, 6468, 10476, 18460, 44421]
z_depth = [180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20]


x = []
y = []
z = []


def assumptionOfDepth(value_area):
    res = 0.0
    for i in range(len(area)):
        if value_area == area[i]:
            res = z_depth[i]
        elif value_area < area[i]:
            if i == 0:
                res = (area[i] / value_area) * z_depth[i]
            else:
                res = z_depth[i - 1] - (((value_area - area[i - 1]) *
                                        (z_depth[i - 1] - z_depth[i])) / (area[i] - area[i - 1]))
        else:
            if i == len(area) - 1:
                res = (area[i] / value_area) * z_depth[i]
            else:
                continue
    res = round(res, 2)

    return res


def assumptionZ(value_area):
    for i in range(len(area) - 1):
        if i == len(area) - 1:
            return int(area[i] / value_area * z_depth[i])
        elif value_area >= area[i] and value_area <= area[i + 1]:
            return (int((z_depth[i] + z_depth[i + 1]) / 2))


def assumptionZNew(value_area):
    for i in range(len(area) - 1):
        if i == len(area) - 1:
            return z_depth[i] * (1 - (area[i] / value_area))
        elif value_area >= area[i] and value_area <= area[i + 1]:
            return z_depth[i] - (z_depth[i] - z_depth[i + 1]) * ((value_area - area[i]) / (area[i + 1] - area[i]))
            # return (int((z_depth[i] + z_depth[i + 1]) / 2))
        elif value_area < area[i] and i == 0:
            return z_depth[i] * (1 + (value_area / area[i]))



saving_directory = "./exp"
prev = -1
results = []
area_points.sort()
for i in range(len(area_points)):
    if area_points[i] != prev:
        results.append(area_points[i])
        prev = area_points[i]

nameOfCoordinates = '\\centers.txt'

# cap = cv2.VideoCapture(str(saving_directory)+"//")

f = open(str(saving_directory) + nameOfCoordinates, 'w')

for i in range(len(x)):
    f.writelines(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + '\n')

new_final_video_dir = final_video_dir.replace(".mp4", "_traced.mp4")

cap = cv2.VideoCapture(final_video_dir)

# output = cv2.VideoWriter(new_final_video_dir, cv2.VideoWriter_fourcc(*'MPEG'),
#                          cv2.CAP_PROP_FPS, (int(frame_height), int(frame_width)))
output = cv2.VideoWriter(new_final_video_dir, -1, cv2.CAP_PROP_FPS, (int(cap.get(3)), int(cap.get(4))))

x_data = np.array(x)
y_data = np.array(y)

def model_f(x, a, b, c):
    return a * x**2 + b * x + c

popt, pcov = curve_fit(model_f, x_data, y_data, p0=[3, 2, -16])

a_opt, b_opt, c_opt = popt
x_model = np.linspace(min(x_data), max(x_data), 100)
y_model = model_f(x_model, a_opt, b_opt, c_opt)

a_opt, b_opt, c_opt = popt
x_model = np.linspace(min(x_data), max(x_data) + 300, 300)
y_model = model_f(x_model, a_opt, b_opt, c_opt)

while(True):
    ret, frame = cap.read()
    if(ret):
        for i in range(len(x_model)):
            # adding filled rectangle on each frame
            cv2.circle(frame, (int(x_model[i]), int(frame_height - y_model[i])), 2,
                       (0, 255, 0), -1)

        # writing the new frame in output
        output.write(frame)
        cv2.imshow("output", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    else:
        break

cv2.destroyAllWindows()
output.release()
cap.release()
