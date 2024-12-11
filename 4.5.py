import math


def input_vector(size):
    vector = []
    for i in range(size):
        vector.append(float(input(f"Введите элемент {i+1}: ")))
    return vector


def vector_length(vector):
    return math.sqrt(sum(x**2 for x in vector))


def main():

    A = input_vector(8)
    B = input_vector(8)
    
    length_A = vector_length(A)
    length_B = vector_length(B)
    

    if length_A > length_B:
        R = 1
    else:
        R = 0
    

    print(f"Значение R: {R}")

if __name__ == "__main__":
    main()
