<center>
**ADDITIONAL METERIALS**
</center>

- [please read this notebook](---ThisDir---/sin.nb)
  - please don't run `Evaluate Notebook` 
  - please evaluate the cells one by one

<center>
**A**
</center>

<center>
(2 punkt)
</center>

The result obtained in the notebook from **ADDITIONAL MATERIALS** is far from perfect.
Even far from good. Please tinker with this example and try to improve the model.
Try different numbers of layers, different layer sizes, different activation functions.
Why is the `Ramp` function suboptimal when it comes to training neural networks?

<center>
**B**
</center>

<center>
(3 punkt)
</center>

Use `ResourceData` to download the `MNIST` dataset containing 
labeled samples of handwritten digits.
Use `NetTrain` and `NetModel` to train the `LeNet` model to recognize
the handwritten digits. What Mathematica functions can we use to 
quantify the quality of the trained model?

<center>
**C**
</center>

<center>
(4 punkt)
</center>

Write a Wolfram Language script that uses the model from **C** for some practical purpouse.

<center>
**D**
</center>

<center>
(3 punkt)
</center>

Fiven an artificial neural network composed from the following layers:
- linear layer with a 2x2 weight matrix and a 2 dimensional bias vector (two neurons, two inputs)
  - elementwise layer with the ramp funciton
- linear layer with a 1x2 weight matrix and a 1 dimensional bias vector (one neuron two inputs)
  - elementwise layer with the ramp funciton
Calculate the derivative of the final output with respect to a couple chosen weights and biases.
Please use dual numbers.


