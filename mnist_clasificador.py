import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos (pasar valores de 0-255 a 0-1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Definir el modelo de red neuronal
model = Sequential([
    Flatten(input_shape=(28, 28)),          # Aplanar las imágenes 28x28 en vectores
    Dense(128, activation='relu'),          # Capa oculta con 128 neuronas y activación ReLU
    Dense(10, activation='softmax')         # Capa de salida para 10 clases (dígitos del 0 al 9)
])

# Compilar el modelo
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Precisión en datos de prueba: {test_accuracy:.4f}")
