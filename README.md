# FACE API Using YOLO 

### Step 1: Get all the requirements

Run the following commands to install all the requirements

    pip install -r requirements.txt

---

### Step 2: Get the yolo weights

- Option 1: From bash script

    Run the `get_models.sh` script in the _**model-weights**_ folder


- Option 2: Download files from GDrive, extract and save them to _**model-weights**_ folder.
    
    - yolov3-wider_16000.weights : [Download](https://drive.google.com/file/d/1xo_G2GK8Y7DuriRT8RYk9FzxCVjS3ZkO/view?usp=sharing)

    - YOLO_Face.h5 : [Download](https://docs.google.com/uc?export=download&id=1a_pbXPYNj7_Gi6OxUqNo_T23Dt_9CzOV)

---

### Step 3: Start the server

>Note: Check the ending of server.py file before running and set your config by uncommenting the lines.

Run:

    python server.py 


