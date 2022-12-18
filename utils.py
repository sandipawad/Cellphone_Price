import pickle
import json
import numpy as np
import config1


class MobilePrice():

    def __init__(self,user_data):

        self.user_data= user_data
        self.model_file_path= 'linear_reg.pkl'

    def load_save_data(self):

        with open (self.model_file_path ,'rb') as f:

            self.model = pickle.load(f)

        with open('project_data.json','r') as f:

            self.project_data = json.load(f)


        

    def get_mobile_price(self):

        self.load_save_data()

        col_len = len(self.project_data['columns'])


        test_array = np.zeros(col_len)

        test_array[0] =eval(self.user_data['Sale'])
        test_array[1] =eval(self.user_data['weight'])
        test_array[2] =eval(self.user_data['resoloution'])
        test_array[3] =eval(self.user_data['ppi'])
        test_array[4] =eval(self.user_data['cpu_core'])
        test_array[5] =eval(self.user_data['cpu_freq'])
        test_array[6] =eval(self.user_data['internal_mem'])
        test_array[7] = eval(self.user_data['ram'])
        test_array[8] =eval(self.user_data['RearCam'])
        test_array[9] =eval(self.user_data['Front_Cam'])
        test_array[10] =eval(self.user_data['battery'])
        test_array[11]=eval(self.user_data['thickness'])


        predict_price = self.model.predict([test_array])[0]


        return predict_price


if __name__ =='__main__':

    ins = MobilePrice()
    ins

