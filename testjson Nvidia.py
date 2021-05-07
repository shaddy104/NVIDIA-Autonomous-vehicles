import os
import json
import sys



def build_json(inputdir, fname):

    """
    inputdir: Give the input path for images
    fname:  Give the json file name to be created for sloth

    """

    indir = os.listdir(inputdir)

    print ("Input Directory is::", indir)

    output = []

    with open(fname, "w") as f:

        for i in range(len(indir)):

            data = {'annotations': [], 'class': "image", "filename": os.path.join(inputdir, indir[i])}
            data1 = {'shapes': [], 'class': "image", "filename": os.path.join(inputdir, indir[i])}
            output.append(data)

        json.dump(output, f, indent=2)

if __name__ == "__main__":

    print ("input",sys.argv[1],sys.argv[2])

    build_json(sys.argv[1], sys.argv[2])

