import io
import os
from PIL import Image
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from pdf2image import convert_from_path
import mathpix
import json
import os


def pdftranslator():

    finalResult = []

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Mathpix-e6a478ab8826.json'

    def listprocessor(words, pageNum):
        # y-axis intervals A[p1by, p1ty] B[p2by, p2ty]
        lines = []
        currentLine = -1

        for i in range(0,len(words)-1):
            sameLine = None  # defaults to none
            if not ((words[i+1][1] - words[i][3] >= 0) or ( words[i][1] - words[i+1][3] >= 0)): #(p2by-p1ty>=0||p1by-p2ty>=0):
                oBot = max(words[i][1], words[i+1][1]) #max(p1by,p2by)
                oTop = min(words[i][3], words[i+1][3]) #min(p1ty,p2ty)
                overlap = oTop-oBot
                overlapConst = 0.2
                if overlap >= overlapConst*max(words[i][3]-words[i][1], words[i+1][3]-words[i+1][1]): # overlapConst*max(p1ty-p1by, p2ty-p2by)): # checks if the words overlap
                    sameLine = True
                else:
                    sameLine = False
            else:
                sameLine = False

            if(sameLine == True):
                # print("true") - for debugging purposes
                lines[currentLine] = [lines[currentLine][0], min(lines[currentLine][1], words[i+1][1]), words[i+1][2], max(lines[currentLine][3], words[i+1][3])] #[p1tx, max(p1ty, p2ty), p2bx, min(p1by, p2by)])
            else:# if not on the sameline
                lines.append([words[i+1][0], words[i+1][1], words[i+1][2], words[i+1][3]]) #([p2tx, p2ty, p2bx, p2by])
                currentLine += 1

        #print(lines)
        lines.pop(0)
        print(lines)

        # Opens a image in RGB mode
        im = Image.open(r"./preprocessed-data/preprocessed-data"+ str(pageNum)+".jpg")
        os.mkdir('/Users/matthewyang/PycharmProjects/MathPix3/processed-data'+str(pageNum))

        counter = 0
        for line in lines:
            im1 = im.crop((line[0]-5, line[1]-5, line[2]+5, line[3]+5))
            saveName = 'crop' + str(counter) + '.jpg'
            finalPath = os.path.join('/Users/matthewyang/PycharmProjects/MathPix3/processed-data'+str(pageNum), saveName)
            im1.save(finalPath, 'JPEG')
            counter +=1


    pages = convert_from_path('test.pdf', 750)

    counta = 0
    for page in pages:
        page.save('./preprocessed-data/preprocessed-data' + str(counta) + '.jpg', 'JPEG')
        counta += 1
        # now crop based on the list

    pageNum = 0
    for filename in sorted(os.listdir('./preprocessed-data')):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            #Text recognition
            client = vision.ImageAnnotatorClient()
            File_Name= filename
            Folder_Path= r'/Users/matthewyang/PycharmProjects/MathPix3/preprocessed-data'
            with io.open(os.path.join(Folder_Path, File_Name), 'rb') as image_file:
                content = image_file.read()

            image = vision.types.Image(content=content)
            response = client.text_detection(image=image)
            #print(response)
            texts = response.text_annotations
            #print('Texts:')
            bound_list=[]
            bound_list.append([100000,100001,99990,99999])
            i=1
            for text in texts:
              #print('\n"{}"'.format(text.description))
              vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
              #print('bounds: {}'.format(','.join(vertices)))
              bound_list.append('bounds: {}'.format(','.join(vertices)))
              bound_list[i] = bound_list[i].strip('bounds: ')
              bound_list[i] = bound_list[i].replace("(", "")
              bound_list[i] = bound_list[i].replace(")", "")
              bound_list[i] = [int(s) for s in bound_list[i].split(",")]
              bound_list[i].pop(2)
              bound_list[i].pop(2)
              bound_list[i].pop(4)
              bound_list[i].pop(4)
              i+=1

            # print(filename)
            # print("\n")
            print(bound_list)
            print("\n")

            listprocessor(bound_list, pageNum)
            pageNum+=1

    #!/usr/bin/env python3
    #
    # Example using Mathpix OCR with multiple result formats. We want to recognize
    # both math and text in the image, so we pass the ocr parameter set to
    # ['math', 'text']. This example returns the LaTeX text format, which
    # starts in text mode instead of math mode, the latex_styled format,
    # the asciimath format, and the mathml format. We define custom
    # math delimiters for the text result so that the math is surrounded
    # by dollar signs ("$").
    #
    #
    #
    #
    # Create a for loop to go through all pngs generated.
    for x in range(0, pageNum):
        for filename in sorted(os.listdir('./processed-data'+str(x))):
            r = mathpix.latex({
                'src': mathpix.image_uri(os.path.join('./processed-data'+str(x), filename)),
                'ocr': ['math', 'text'],
                'skip_recrop': True,
                'formats': ['latex_styled'],
                'format_options': {
                    'text': {
                        'transforms': ['rm_spaces', 'rm_newlines'],
                        'math_delims': ['$', '$']
                    }
                }
            })

            #
            # Note the actual results might be slighly different in LaTeX spacing or
            # MathML attributes.
            #
            #
            # print('Expected for r["text"]: "$-10 x^{2}+5 x-3$ and $-7 x+4$"')
            # print('Expected for r["latex_styled"]: "-10 x^{2}+5 x-3 \\text { and }-7 x+4"')
            # print('Expected for r["asciimath"]: "-10x^(2)+5x-3\\" and \\"-7x+4"')
            # print('Expected for r["mathml"]: "<math><mo>\u2212</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>\u2212</mo><mn>3</mn><mtext>\u00a0and\u00a0</mtext><mo>\u2212</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>4</mn></math>"')
            json_str = json.dumps(r, indent=4, sort_keys=True)
            #print("\nResult object:", json_str)
            output = json.loads(json_str)
            finalResult.append(output['latex_styled'])
    return finalResult
