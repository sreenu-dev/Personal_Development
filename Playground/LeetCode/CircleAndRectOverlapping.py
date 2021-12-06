import matplotlib.pyplot as plt

figure,axes=plt.subplots()
drawing_color_circle=plt.Circle((6,6),2)

axes.set_aspect(1)
axes.add_artist(drawing_color_circle)
plt.title('Coloured Circle')
plt.show()