import io
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'Mathpix-e6a478ab8826.json'
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
#Text recognition

for filename in sorted(os.listdir('/Users/matthewyang/PycharmProjects/MathPix3/preprocessed-data')):
    client = vision.ImageAnnotatorClient()
    File_Name=filename
    Folder_Path= r'/Users/matthewyang/PycharmProjects/MathPix3/preprocessed-data'
    with io.open(os.path.join(Folder_Path, File_Name), 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.web_detection(image=image)
    annotations = response.web_detection
    if annotations.best_guess_labels:
       for label in annotations.best_guess_labels:
           print('\nBest guess label: {}'.format(label.label))
    # if annotations.pages_with_matching_images:
    #    print('\n{} Pages with matching images found:'.format(
    #        len(annotations.pages_with_matching_images)))
    #    for page in annotations.pages_with_matching_images:
    #        print('\n\tPage url   : {}'.format(page.url))
    #        if page.full_matching_images:
    #            print('\t{} Full Matches found: '.format(
    #                   len(page.full_matching_images)))
    #            for image in page.full_matching_images:
    #                print('\t\tImage url  : {}'.format(image.url))
    #        if page.partial_matching_images:
    #            print('\t{} Partial Matches found: '.format(
    #                   len(page.partial_matching_images)))
    #            for image in page.partial_matching_images:
    #                print('\t\tImage url  : {}'.format(image.url))
    if annotations.web_entities:
       print('\n{} Web entities found: '.format(
           len(annotations.web_entities)))
       for entity in annotations.web_entities:
           print('\n\tScore      : {}'.format(entity.score))
           print(u'\tDescription: {}'.format(entity.description))
    # if annotations.visually_similar_images:
    #    print('\n{} visually similar images found:\n'.format(
    #        len(annotations.visually_similar_images)))
    #    for image in annotations.visually_similar_images:
    #        print('\tImage url    : {}'.format(image.url))