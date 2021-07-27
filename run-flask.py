from flask import Flask, request
import json
import subprocess
import os  
 

app = Flask(__name__)
@app.route("/", methods=['POST'])
def main_translate():
    """
    Api function that will take file as input
    :return:
    """
    try:
        result=''
        json_dict = json.loads(request.data)
        text = json_dict["text"]     
        domain = json_dict["domain"]
        #write the text into a inpfile
        
        inputFile = "infile.txt"
        inf = open(inputFile, "w")
        inf.write(text)
        inf.close()
       
        if(domain == 'health'):
        	#call heath model
        	os.system('./run-health-gpu.sh {}' .format(str(inputFile)))
  
        elif(domain == 'nptel'):
        	#call NPTEL model
        	os.system('./run-nptel-gpu.sh {}' .format(str(inputFile)))
        	
        	
        else:
        	success = False
        	result = ' '
        	
        #read the output file
        outputFile = inputFile +'-output'
        if os.path.exists(outputFile) and os.path.getsize(outputFile) > 0:
            opf = open(outputFile, "r",encoding='utf-8')
            result = opf.read()
            success = True
        else:
            success = "File not found"
    		
    	       

    except Exception as e:
        success=False
        result=''

    return json.dumps({
    "success": success,
    "result": result
    })

    return result, success

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)





