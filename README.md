# clasificador-mnist
 Clasificador de Dígitos con MNIST

Este proyecto implementa una red neuronal simple para clasificar imágenes de dígitos escritos a mano utilizando el dataset MNIST.

---

## Tipo de Red

Se utiliza una **red neuronal multicapa (Multilayer Perceptron - MLP)** compuesta por:

- Una capa de entrada que aplana las imágenes 28x28 píxeles.
- Una capa oculta con 128 neuronas y activación ReLU.
- Una capa de salida con 10 neuronas (una por dígito) y activación softmax.

Este tipo de red es adecuada para tareas de clasificación simples como MNIST, aunque también podrían usarse redes convolucionales (CNN) para mejorar la precisión.

---

## Librerías Utilizadas

- `TensorFlow` y `Keras`: para definir, compilar y entrenar el modelo de red neuronal.
- `NumPy` (implícito): para manipular datos numéricos y matrices.
- (Opcionalmente) `Matplotlib`: para visualizar imágenes o resultados si se desea extender el proyecto.

---

## Objetivo de la Red

La red neuronal tiene como objetivo **clasificar imágenes en escala de grises** de 28x28 píxeles que representan dígitos del 0 al 9. Utiliza el dataset **MNIST**, que contiene:

- 60,000 imágenes para entrenamiento
- 10,000 imágenes para prueba

Es un ejemplo clásico para iniciarse en redes neuronales y aprendizaje automático.

---

## Archivos

- `mnist_clasificador.py`: script de Python que entrena y evalúa la red neuronal con TensorFlow.

---

## Cómo ejecutarlo

1. Asegurate de tener Python 3 instalado.
2. Instalá TensorFlow si no lo tenés:
   ```bash
   pip install tensorflow

---

## Ejecutá el script:

  python mnist_clasificador.py

---

👤 Autor

Trabajo realizado por Ezequiel Cerdan de la actividad sobre redes neuronales.
