import cv2          # Import open cv
image_path = 'watch.jpg'
# Reading the image in colored format

color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
# this will return an array of pixel value 0 to 255 for RGB

grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Reading the image in grayscale format 0->black, 255->white

# Resizing the read image to display
color_image_resize = cv2.resize(color_image, (600, 400))
# Display the colored image
cv2.imshow("My Colored Image ", color_image_resize)

# Resizing the read image to display
grayscale_image_resize = cv2.resize(grayscale_image, (600, 400))
# Display the colored image
cv2.imshow("My Grayscaled Image ", grayscale_image_resize)

# Do not exit until I press any waitKey (it is like getch())
cv2.waitKey(0)
cv2.destroyAllWindows()  # Closes all displayed windows