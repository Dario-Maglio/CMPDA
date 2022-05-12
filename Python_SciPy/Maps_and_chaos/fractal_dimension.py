import numpy as np
import matplotlib.pyplot as plt



def fractal_dimension(image):
    """ Calculates the fractal dimension of an image - 2D numpy array.

    The algorithm is a modified box-counting algorithm as described by Wen-Li
    Lee and Kai-Sheng Hsieh.
    @author: brian-xu
    https://github.com/brian-xu/FractalDimension

    Args:
        image: A 2D array containing a grayscale image. Format should be
               equivalent to cv2.imread(flags=0). The size of the image has no
               constraints, but it needs to be square (m×m array).
    Returns:
        D: The fractal dimension Df, as estimated by the modified box-counting
           algorithm.
    """
    M = image.shape[0]  # image shape
    G_min = image.min()  # lowest gray level (0=white)
    G_max = image.max()  # highest gray level (255=black)
    G = G_max - G_min + 1  # number of gray levels, typically 256
    prev = -1  # used to check for plateaus
    r_Nr = []

    for L in range(2, (M // 2) + 1):
        h = max(1, G // (M // L))  # minimum box height is 1
        N_r = 0
        r = L / M
        for i in range(0, M, L):
            boxes = [[]] * ((G + h - 1) // h)  # create enough boxes with height h to fill the fractal space
            for row in image[i:i + L]:  # boxes that exceed bounds are shrunk to fit
                for pixel in row[i:i + L]:
                    height = (pixel - G_min) // h  # lowest box is at G_min and each is h gray levels tall
                    boxes[height].append(pixel)  # assign the pixel intensity to the correct box
            stddev = np.sqrt(np.var(boxes, axis=1))  # calculate the standard deviation of each box
            stddev = stddev[~np.isnan(stddev)]  # remove boxes with NaN standard deviations (empty)
            nBox_r = 2 * (stddev // h) + 1
            N_r += sum(nBox_r)
        if N_r != prev:  # check for plateauing
            r_Nr.append([r, N_r])
            prev = N_r
    x = np.array([np.log(1 / point[0]) for point in r_Nr])  # log(1/r)
    y = np.array([np.log(point[1]) for point in r_Nr])  # log(Nr)
    D = np.polyfit(x, y, 1)[0]  # D = lim r -> 0 log(Nr)/log(1/r)
    return D

def fractal_dimension_3D(array, max_box_size=None, min_box_size=1, n_samples=20,
                         n_offsets=0, plot=False):
    """Calculates the fractal dimension of a 3D numpy array.

    @author: daniel
    https://github.com/ChatzigeorgiouGroup/FractalDimension


    Args:
        array (np.ndarray): The array to calculate the fractal dimension of.
        max_box_size (int): The largest box size, given as the power of 2 so
                            that 2**max_box_size gives the sidelength of the
                            largest box.
        min_box_size (int): The smallest box size, given as the power of 2 so
                            that 2**min_box_size gives the sidelength of the
                            smallest box. Default value 1.
        n_samples (int): number of scales to measure over.
        n_offsets (int): number of offsets to search over to find the smallest
                         set N(s) to cover  all voxels>0.
        plot (bool): set to true to see the analytical plot of a calculation.
    """
    #determine the scales to measure on
    if max_box_size == None:
        #default max size is the largest power of 2 that fits in the smallest dimension of the array:
        max_box_size = int(np.floor(np.log2(np.min(array.shape))))
    scales = np.floor(np.logspace(max_box_size,min_box_size, num=n_samples, base=2))
    scales = np.unique(scales) #remove duplicates that could occur as a result of the floor

    #get the locations of all non-zero pixels
    locs = np.where(array > 0)
    voxels = np.array([(x,y,z) for x,y,z in zip(*locs)])

    #count the minimum amount of boxes touched
    Ns = []
    #loop over all scales
    for scale in scales:
        touched = []
        if n_offsets == 0:
            offsets = [0]
        else:
            offsets = np.linspace(0, scale, n_offsets)
        #search over all offsets
        for offset in offsets:
            bin_edges = [np.arange(0, i, scale) for i in array.shape]
            bin_edges = [np.hstack([0-offset,x + offset]) for x in bin_edges]
            H1, e = np.histogramdd(voxels, bins = bin_edges)
            touched.append(np.sum(H1>0))
        Ns.append(touched)
    Ns = np.array(Ns)

    #From all sets N found, keep the smallest one at each scale
    Ns = Ns.min(axis=1)

    #Only keep scales at which Ns changed
    scales  = np.array([np.min(scales[Ns==x]) for x in np.unique(Ns)])

    Ns = np.unique(Ns)
    Ns = Ns[Ns > 0]
    scales = scales[:len(Ns)]
    #perform fit
    coeffs = np.polyfit(np.log(1/scales), np.log(Ns),1)

    #make plot
    if plot:
        fig, ax = plt.subplots(figsize = (8,6))
        ax.scatter(np.log(1/scales), np.log(np.unique(Ns)), c="teal", label="Measured ratios")
        ax.set_ylabel("$\log N(\epsilon)$")
        ax.set_xlabel("$\log 1/ \epsilon$")
        fitted_y_vals = np.polyval(coeffs, np.log(1/scales))
        ax.plot(np.log(1/scales), fitted_y_vals, "k--", label = f"Fit: {np.round(coeffs[0],3)}X+{np.round(coeffs[1],3)}")
        ax.legend();
    return coeffs[0]
