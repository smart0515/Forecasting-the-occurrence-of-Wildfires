import matplotlib
print(matplotlib.rcsetup.all_backends)
matplotlib.use('Agg')

def show_map(input_raster='', colormap='', image_size=1.5, return_figure=False):
    with rasterio.open(input_raster) as image_data:
        my_matrix = image_data.read(1)
        my_matrix = np.ma.masked_where(my_matrix == 32767, my_matrix)
        fig, ax = plt.subplots()
        image_hidden = ax.imshow(my_matrix, cmap=colormap)
        plt.close()

        fig, ax = plt.subplots()
        fig.set_facecolor("w")
        width = fig.get_size_inches()[0] * image_size
        height = fig.get_size_inches()[1] * image_size
        fig.set_size_inches(w=width, h=height)
        image = ax.imshow(my_matrix, cmap=colormap, vmin=0, vmax=1) # vmin,vmax로 칼라바의 범위를 지정
        # cbar = fig.colorbar(image_hidden, ax=ax, pad=0.01)
        plt.axis('off')
        if return_figure == False:
            plt.show()
            plt.savefig('test.png', bbox_inches='tight', transparent=True)
        else:
            return fig,ax

 show_map(input_raster='파일명.tif', colormap='원하는 colormap', image_size=1.5, return_figure=False)
