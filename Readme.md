# Image and Audio Captchas Solver

As a part of coursework related to the subject 'Scalable Computing' in Trinity College Dublin,
Project3 targets to solve large amount of image and audio captchas using convulation layer.

## Solving the image captchas
Steps performed:
1. Generated 100000 sample image captchas through generate.py by randomly generating the captchas out of the symbols (A-Z,0-9), depending on the inputs like width, height of captcha image, Length of captchas in characters, no. of captchas to generate, path to output folder, symbols file.
2. Split the data into train and validate in the 80/20 ratio.
3. Trained and tested the model using the generated captchas under train and validate data as input through train.py. Train code contains the training model using Keras neural network library that works on layers.
4. Conv2D(2D Convolution Layer) is used to create a convolution kernel that is wind with layers input which helps produce a tensor of outputs and scaling the input pixel values.
5. Trained model architecture is saved to .json file.
6. Now this .json file is used to classify the given captchas using classify.py.

## Solving the audio captchas
Steps performed:
1. For Audio captchas generation, first generated 200000, 8 chars text strings out of the symbols (A-Z,0-9), and simultaneously converted them to corresponding audio files through Google Text-to-Speech function (gTTS) and saving it.
2. 8 char audio files were converted to spectrograms through audiotospectra.py so that they can be passed to convulation 2d layer in keras training model. Here librosa function melspectrogram is used to convert and plot the audio files to time-frequency representation of a sound.
3. Spectrograms are split into train and validate data in 80/20 ratio.
4. Trained and classified the spectrograms in the same way as that of image captchas.

## Files contained
generate_audio.py - script to generate sample audio captchas
audiotospectra.py - convert audio captchas generated to spectrogram
train.py - script to train the model by inputting part of sample spectrograms that were generated
test.json - train.py trains the model and gives test.json as the output file that is used for classification
classify.py - Model trained is used to classify the new set of audio captchas through this script
trainimage.py - script to train the model by inputting part of sample image captchas that were generated
testimage.json - trainimage.py trains the model and gives testimage.json as the output file that is used for classification
classifyimage.py - Model trained is used to classify the new set of image captchas through this script
commands.txt - set of commands through which above scripts are executed defining batch size and epochs iterated for training and classification
stuff.csv - output file

###### Keywords
Image captcha, Audio captcha, tensor flow, keras, convulation layer, scalable computing, Audio to Spectra, gTTS
