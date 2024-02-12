import numpy as np

def normalization(data):
    """
    Normalize the given data
    Input:  data = a 2d numpy array of shape (n_samples, n_features).
    Output:  the normalized data on each column separately
    """
    scaler = np.zeros(data.shape)
    for i in range(data.shape[1]):
        if max (data[:,i]) ==  min(data[:,i]):
            scaler[:,i] = 0
        else:
            scaler[:,i] = (data[:,i] - min(data[:,i]))/(max(data[:,i]) - min(data[:,i]))
    return scaler


def standardization(data):
    """
    Standardize the given data
    Input:  data = a 2d numpy array of shape (n_samples, n_features).
    Output:  the standardized data on each column separately
    """
    std = np.zeros(data.shape)
    for i in range(data.shape[1]):
        mean = np.mean(data[:,i])
        std_dev = np.std(data[:,i])
        if std_dev == 0:
            std[:,i] = 0
        else:
            std[:,i] = (data[:,i] - mean)/std_dev
    return std

def label_encoding(data):
    """
    Label encoding the given categorial data in the alphabetical order
    Input:  data = a 1d numpy array of str.
    Output:  the 1d array of encoded labels and a 1d array of class label
    """
    label_array = np.zeros(data.shape)
    class_str = sorted(np.unique(data))
    for i in range(data.shape[0]):
        label_array[i] = class_str.index(data[i])
    return label_array, class_str


if __name__ == "__main__":
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

    # load iris features and target as numpy array 
    data = np.loadtxt('iris.data', delimiter=',', usecols=(0,1,2,3))
    target = np.loadtxt('iris.data', delimiter=',', usecols=(4), dtype='str')

    scaler = MinMaxScaler()
    skl = scaler.fit_transform(data[:,0:1])
    our = normalization(data[:,0:1])
    print(skl[-5:,:])
    print(our[-5:,:])
    assert np.allclose(skl, our)

    scaler = StandardScaler()
    skl = scaler.fit_transform(data[:,1:3])
    our = standardization(data[:,1:3])
    print(skl[-5:,:])
    print(our[-5:,:])
    assert np.allclose(skl, our)

    le = LabelEncoder()
    skl = le.fit_transform(target)
    our, cls = label_encoding(target)
    print(skl[-5:])
    print(our[-5:])
    print(le.classes_)
    print(cls)