<html>
<head>
    <title>Python Encoder and Decoder</title>
</head>
<body>
    <h1>Python Encoder and Decoder</h1>
    <p>This is a Python project that encodes and decodes text files using a random substitution cipher. You can choose the file name and path, and the program will create new files with the encoded or decoded text.</p>
    <ul>
        <li>Uses random.shuffle to create a key from a list of characters</li>
        <li>Uses zip to pair each character with its corresponding substitute</li>
        <li>Uses replace to transform the text according to the key</li>
        <li>Uses input and print to interact with the user</li>
        <li>Uses open and write to create and save the new files</li>
    </ul>
    <p>Usage</p>
    <p>To run this project, you need Python 3 on your system. You can execute the project by typing this command in your terminal:</p>
    <pre><code>python encoder_decoder.py</code></pre>
    <p>You will be asked to choose an option: 1 for encoding, 2 for decoding, or 3 for exiting. If you choose 1 or 2, you will also be asked to enter the path and the file name of the text file you want to encode or decode. The program will display the original and the transformed text, and create a new file with the extension .txt in the same path. You can press enter to continue or choose another option.</p>
</body>
</html>
