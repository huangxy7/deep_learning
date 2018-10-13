#_*_coding:utf-8_*_


import argparse
import sys
import os

MODEL_TRAIN = 'train'
MODEL_VAL = 'val'


IMAGE_TYPE = {'jpg','png'}

class GenerateTxtForCaffe:


    def __init__(self,input_dir,output_path):


        self.__input_dir = input_dir
        self.__output_path = output_path



    def get_photo_list_for_val(self):
        '''
        Get all picture names in the picture directory.

        :param None
        :return: list  (include photo_name), like ['1.jpg','2.jpg']
        '''

        res_list = []

        photo_list = os.listdir(self.__input_dir)


        for p_name in photo_list:

            abs_path = os.path.join(self.__input_dir, p_name)

            if not os.path.isfile(abs_path):
                continue

            type = p_name.split('.')[-1].lower()

            if type in IMAGE_TYPE:
                res_list.append(p_name)




        return res_list


    def get_photo_list_for_train(self):
        '''
        Get all picture names in the picture directory.

        :param not
        :return: list  (include photo_name), like ['red/1.jpg','green/2.jpg']
        '''

        res_list = []


        chile_path = os.listdir(self.__input_dir)


        for dir_path in chile_path:
            abs_dir_path = os.path.join(self.__input_dir,dir_path)

            if not os.path.isdir(abs_dir_path):
                continue



            for p_name in os.listdir(abs_dir_path):
                abs_p_path = os.path.join(abs_dir_path,p_name)

                if os.path.isfile(abs_p_path):

                    p_type = p_name.split('.')[-1].lower()
                    if p_type not in IMAGE_TYPE:
                        continue

                    else:
                        res_list.append('/'.join([dir_path,p_name])+' '+dir_path)





        return res_list




    def write_file(self,photo_list,parser):
        '''
        write the name of the picture in the list to the file.
        :param photo_list:
        :param parser:
        :return: None
        '''
        #print(photo_list)
        if len(photo_list) == 0:
            print('ERROT: Not find image.\n')

            parser.print_help()
            sys.exit(1)

        with open(self.__output_path,'w') as f:
            for p in photo_list:
                f.write(p+'\n')
        print('save file in :',self.__output_path)


def check_directory(directory,parser):
    '''
    check the directory is valid.

    :param directory:
    :param parser:
    :return:
    '''
    if not os.path.exists(directory):
        print('ERROR: Images\' directory is not exists.\n')
        parser.print_help()

        sys.exit(1)



def check_model(model,parser):

    '''
    check the model is valid.

    :param model:
    :param parser:
    :return:
    '''

    model = model.lower()

    if model!='train' and model!='val':
        print('ERROR: model is invalid.\n')
        parser.print_help()

        sys.exit(1)

def check_output_path(output_path,parser):
    '''
    check the output_path is valid.

    :param output_path:
    :param parser:
    :return:
    '''

    filepath, filename = os.path.split(output_path)


    if not os.path.exists(filepath):
        print('ERROR: output path is invalid.\n')
        parser.print_help()

        sys.exit(1)

    if os.path.splitext(filename)[-1] != '.txt':

        print('ERROR: file type must be txt.\n')
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = '''generate train or val txt for deeplearning.\n
                         image type is jpg or png.\n
                         content like this: \n
                              train/1.jpg \n
                              train/2.jpg \n'''

    parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
    parser.add_argument('-d','--directory',help='select images directory',default='./')
    parser.add_argument('-m','--model',help='select train or val',default='val')
    parser.add_argument('-o','--output',help="txt output path,like \'./train.txt\'",default='./res.txt',nargs='?')

    args = parser.parse_args() #get args list


    images_dir = args.directory #get image directory
    model = args.model    #get category , tarin or val
    output_path = args.output    #file output path

    #check arguments is validity.
    check_directory(images_dir,parser)
    check_model(model,parser)
    check_output_path(output_path,parser)

    input_path = os.path.abspath(images_dir)    #get input abspath
    output_path = os.path.abspath(output_path)  #get output abspath

    app = GenerateTxtForCaffe(input_path,output_path)
    photo_list = []

    if model == MODEL_TRAIN:
        photo_list = app.get_photo_list_for_train()
    else:
        photo_list = app.get_photo_list_for_val()

    app.write_file(photo_list,parser)
