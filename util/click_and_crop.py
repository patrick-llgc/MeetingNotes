# import the necessary packages
import argparse
import cv2
import numpy as np

class ScreenPointGetter(object):
  def __init__(self, image):
    self.refPt = []
    self.orig = image
    self.ratio = 500.0 / image.shape[0]
    self.image = cv2.resize(image, (0, 0), fx=self.ratio, fy=self.ratio)

  def click_and_crop(self, event, x, y, flags, param):
    # grab references to the global variables
    # global refPt
    # print(param.__class__)

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
      self.refPt.append((x, y))
      print('Add point!')
   
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
      # record the ending (x, y) coordinates and indicate that
      # the cropping operation is finished
      # print(self.refPt[-1])
   
      # draw a rectangle around the region of interest
      cv2.circle(self.image, self.refPt[-1], 10, (0, 255, 0), 2)
      cv2.imshow("image", self.image)

  def get_points(self):
    # initialize the list of reference points and boolean indicating
    # whether cropping is being performed or not

    # load the image, clone it, and setup the mouse callback function

    clone = self.image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", self.click_and_crop)
     
    # keep looping until the 'q' key is pressed
    while True:
      # display the image and wait for a keypress
      cv2.imshow("image", self.image)
      key = cv2.waitKey(1) & 0xFF
     
      # if the 'r' key is pressed, reset the cropping region
      if key == ord("r"):
        self.image = clone.copy()
        self.refPt = []
     
      # if the 'c' key is pressed, break from the loop
      elif key == ord("c") or key == ord("q") or len(self.refPt) > 4:
        break
     
    # close all open windows
    cv2.destroyAllWindows()
    contour_pts = np.array([[[x, y]] for x, y in self.refPt[:4]]) / self.ratio
    return contour_pts

if __name__ == '__main__':
  # construct the argument parser and parse the arguments
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--image", required=True, help="Path to the image")
  args = vars(ap.parse_args())
  image = cv2.imread(args["image"])
  refPt = ScreenPointGetter(image).get_points()
  print(refPt)