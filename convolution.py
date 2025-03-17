import numpy as np

def convolution(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    output_length = signal_length - kernel_length + 1
    output = np.zeros(output_length)
    
    for i in range(output_length):
        output[i] = np.sum(signal[i:i+kernel_length] * kernel[::-1])
    
    return output

# 예제 신호와 커널
signal = np.array([1, 2, 3, 4, 5])
kernel = np.array([1, 0, -1])

# 컨볼루션 적용
result = convolution(signal, kernel)
print("Convolution result:", result)
