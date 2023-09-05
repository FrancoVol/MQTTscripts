import numpy as np
import matplotlib.pyplot as plt
import tflite_runtime.interpreter as tflite
from zipfile import ZipFile
import os




def set_input_tensor(interpreter, input):
  input_details = interpreter.get_input_details()[0]
  tensor_index = input_details['index']
  input_tensor = interpreter.tensor(tensor_index)()
  # Inputs for the TFLite model must be uint8, so we quantize our input data.
  scale, zero_point = input_details['quantization']
  quantized_input = np.uint8(input / scale + zero_point)
  input_tensor[:, :, :] = quantized_input

def predict_weather(interpreter, input):
  set_input_tensor(interpreter, input)
  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = interpreter.get_tensor(output_details['index'])
  # Outputs from the TFLite model are uint8, so we dequantize the results:
  scale, zero_point = output_details['quantization']
  output = scale * (output - zero_point)
  return output



def main():

    interpreter = tflite.Interpreter('weather_forecast_quant.tflite', experimental_delegates=[tflite.load_delegate('libedgetpu.so.1')])
    interpreter.allocate_tensors()

    

    

    for x, y in dataset_test.take(5):
        prediction = predict_weather(interpreter, x)
        print('prediction:', prediction[0])
        print('truth:', y[0].numpy())


if __name__ == "__main__":
    main()