import numpy as np

def normalization(data):
    scaler = np.zeros(data.shape)
    for col in range(data.shape[1]):
        if max (data[:,col]) ==  min(data[:,col]):
            for row in range(data.shape[0]):
                scaler[row,col] = 0
        else:
            for row in range(data.shape[0]):
                scaler[row,col] = (data[row,col] - min(data[:,col]))/(max(data[:,col]) - min(data[:,col]))
    return scaler

def standardization(data):
    std_scaler = np.zeros(data.shape)
    for col in range(data.shape[1]):
        mean = np.mean(data[:,col])
        std = np.std(data[:,col])
        if std == 0:
            for row in range(data.shape[0]):
                std_scaler[row,col] = 0
        else:
            for row in range(data.shape[0]):
                std_scaler[row,col] = (data[row,col] - mean)/std
    return std_scaler

def label_encoding(data):
    label_array = np.zeros(data.shape)
    class_str = sorted(np.unique(data))
    for row in range(data.shape[0]):
        label_array[row] = class_str.index(data[row])
    return label_array,class_str

if __name__ == "__main__":
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

    # load iris features and target as numpy array
    data = np.loadtxt('iris.data', delimiter=',', usecols=(0,1,2,3))
    target = np.loadtxt('iris.data', delimiter=',', usecols=(4), dtype=str)
    skl = MinMaxScaler()
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
    our , cls = label_encoding(target)
    print(skl[-5:,:])
    print(our[-5:,:])
    assert np.allclose(skl, our)